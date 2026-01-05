import os
import sys
import glob
import importlib
import asyncio
import shlex
from telethon import TelegramClient, events
from telethon.sessions import StringSession

# --- الإعدادات الأساسية ---
API_ID = 29827519 
API_HASH = "9afadf1ec94457c6bb383139555a2bdc"
GIT_TOKEN = "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" 
GH_OWNER = "aesareetcuu6jllk"
GH_REPO = "helassors"
GH_BRANCH = "HuRe"
REPO_URL = f"https://{GIT_TOKEN}@github.com/{GH_OWNER}/{GH_REPO}.git"

# --- التحقق من ملف الإعدادات ---
if os.path.exists("config.txt"):
    with open("config.txt", "r") as f:
        data = f.read().splitlines()
        SESSION_STRING, BOT_TOKEN = data[0], data[1]
else:
    SESSION_STRING = input("أدخل كود الجلسة (String Session): ")
    BOT_TOKEN = input("أدخل توكن البوت (Bot Token): ")
    with open("config.txt", "w") as f:
        f.write(f"{SESSION_STRING}\n{BOT_TOKEN}")

# تعريف المحرك (hellas) ككائن عالمي ليكون متاحاً لكل الملفات
hellas = TelegramClient(StringSession(SESSION_STRING), API_ID, API_HASH)

def load_all_plugins():
    """البحث عن كافة ملفات البايثون في المجلد وتشغيلها ديناميكياً"""
    # جلب كل الملفات التي تنتهي بـ .py
    path = "*.py"
    files = glob.glob(path)
    
    for file in files:
        module_name = file.replace(".py", "")
        # استثناء الملفات الأساسية لكي لا يحدث تكرار في التشغيل
        if module_name in ["main", "__init__"]:
            continue
            
        try:
            # إذا كان الملف محملاً سابقاً نقوم بعمل reload لتحديث الأوامر
            if module_name in sys.modules:
                importlib.reload(sys.modules[module_name])
            else:
                importlib.import_module(module_name)
            print(f"✅ تم تشغيل الملف المنفصل: {module_name}")
        except Exception as e:
            print(f"❌ خطأ في تشغيل الملف {module_name}: {e}")

async def run_git_update():
    """تحديث شامل: يسحب كل الملفات من GitHub ويعيد تشغيل النظام"""
    run_dir = os.getcwd()
    cmd = (
        f"git init && "
        f"git remote remove origin || true && "
        f"git remote add origin {REPO_URL} && "
        f"git fetch --all && "
        f"git reset --hard origin/{GH_BRANCH}"
    )
    # تنفيذ الأمر وإرجاع النتيجة
    return os.system(cmd) == 0

# --- أوامر الإدارة الأساسية (داخل main لضمان العمل دائماً) ---

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^\.تحديث$"))
async def update_handler(event):
    await event.edit("**🔄 جاري تحديث كافة ملفات السورس من GitHub...**")
    if await run_git_update():
        await event.edit("**✅ تم التحديث بنجاح! جاري إعادة تحميل كافة الملفات...**")
        # إعادة تشغيل البايثون بالكامل لضمان تشغيل كل شيء جديد
        os.execl(sys.executable, sys.executable, *sys.argv)
    else:
        await event.edit("**❌ فشل التحديث: تأكد من الرابط أو اسم الفرع (HuRe).**")

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^\.اطفاء$"))
async def shutdown_handler(event):
    await event.edit("**᯽︙ تم إيقاف تشغيل المحرك بنجاح ✓**")
    sys.exit(0)

if __name__ == "__main__":
    print("🚀 محرك HELLAS قيد الإقلاع...")
    # بدء تشغيل الحساب
    hellas.start()
    
    # استدعاء كافة الملفات الأخرى الموجودة في المجلد (مهما كان اسمها)
    load_all_plugins()
    
    print("✅ النظام جاهز والملفات المنفصلة تعمل.")
    hellas.run_until_disconnected()
