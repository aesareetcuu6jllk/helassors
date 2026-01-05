import os
import sys
import glob
import importlib
import asyncio
import shlex
from telethon import TelegramClient, events
from telethon.sessions import StringSession

# --- الإعدادات الثابتة ---
API_ID = 29827519 
API_HASH = "9afadf1ec94457c6bb383139555a2bdc"
GIT_TOKEN = "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" 

# إعدادات المستودع من الرابط الذي أرسلته
GH_OWNER = "aesareetcuu6jllk"
GH_REPO = "helassors"
GH_BRANCH = "HuRe"  # تأكد أن هذا هو اسم الفرع في حسابك
REPO_URL = f"https://{GIT_TOKEN}@github.com/{GH_OWNER}/{GH_REPO}.git"

# --- نظام الجلسة وحفظ الإعدادات ---
if os.path.exists("config.txt"):
    with open("config.txt", "r") as f:
        data = f.read().splitlines()
        SESSION_STRING, BOT_TOKEN = data[0], data[1]
else:
    SESSION_STRING = input("أدخل كود الجلسة (String Session): ")
    BOT_TOKEN = input("أدخل توكن البوت (Bot Token): ")
    with open("config.txt", "w") as f:
        f.write(f"{SESSION_STRING}\n{BOT_TOKEN}")

hellas = TelegramClient(StringSession(SESSION_STRING), API_ID, API_HASH)

def load_all_files():
    """البحث عن كافة ملفات البايثون في المجلد وتشغيلها"""
    # جلب كافة ملفات .py بجانب ملف main.py
    files = glob.glob("*.py")
    for name in files:
        module_name = name.replace(".py", "")
        # استثناء الملف الرئيسي لكي لا يدخل في حلقة تكرار
        if module_name in ["main", "__init__"]:
            continue
        
        try:
            if module_name in sys.modules:
                importlib.reload(sys.modules[module_name])
                print(f"🔄 تم إعادة تحميل: {module_name}")
            else:
                importlib.import_module(module_name)
                print(f"✅ تم تفعيل الملف: {module_name}")
        except Exception as e:
            print(f"❌ خطأ في تشغيل {module_name}: {e}")

async def run_git_update():
    """منطق التحديث المباشر من الرابط"""
    run_dir = os.getcwd()
    run_dir_q = shlex.quote(run_dir)
    
    # أوامر Git لتحديث الملفات الحالية من المستودع
    cmd = (
        f"cd {run_dir_q} && "
        f"git remote set-url origin {REPO_URL} || git remote add origin {REPO_URL} && "
        f"git fetch --all && "
        f"git reset --hard origin/{GH_BRANCH}"
    )
    return os.system(cmd) == 0

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^\.تحديث$"))
async def update_handler(event):
    await event.edit("**🔄 جاري فحص التحديثات في المستودع...**")
    
    if await run_git_update():
        await event.edit("**✅ تم سحب الملفات الجديدة! جاري إعادة تشغيل النظام...**")
        # إعادة تشغيل كاملة لضمان تفعيل التعديلات
        os.execl(sys.executable, sys.executable, *sys.argv)
    else:
        await event.edit("**❌ فشل التحديث: تأكد من اسم الفرع HuRe في GitHub.**")

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^\.اطفاء$"))
async def shutdown_handler(event):
    await event.edit("**᯽︙ تـم إيقـاف تشغيـل البـوت بنجـاح ✓**")
    sys.exit(0)

if __name__ == "__main__":
    print("🚀 محرك HELLAS يبدأ العمل الآن...")
    hellas.start()
    
    # تشغيل كل ملفات البايثون الموجودة في الرابط
    load_all_files()
    
    print("✅ النظام جاهز ومتصل.")
    hellas.run_until_disconnected()
