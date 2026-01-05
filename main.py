import os
import sys
import glob
import importlib
import asyncio
import shlex
from telethon import TelegramClient, events
from telethon.sessions import StringSession

# --- الإعدادات الثابتة والقوية ---
API_ID = 29827519 
API_HASH = "9afadf1ec94457c6bb383139555a2bdc"
GIT_TOKEN = "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" 
GH_OWNER = "aesareetcuu6jllk"
GH_REPO = "helassors"
GH_BRANCH = "HuRe"
REPO_URL = f"https://{GIT_TOKEN}@github.com/{GH_OWNER}/{GH_REPO}.git"

# --- نظام الجلسة والبيانات المحلية ---
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

def load_plugins():
    """تحميل وتشغيل كافة الملفات من مجلد hellas وإعادة تحميل المعدل منها"""
    if not os.path.exists("hellas"):
        os.makedirs("hellas")
    
    if not os.path.exists("hellas/__init__.py"):
        with open("hellas/__init__.py", "w") as f: pass

    path = "hellas/*.py"
    files = glob.glob(path)
    for name in files:
        if name.endswith("__init__.py"):
            continue
        
        module_path = name.replace(".py", "").replace(os.sep, ".")
        
        try:
            # إذا كان الملف محملاً مسبقاً، نقوم بعمل Reload لتطبيق التعديلات
            if module_path in sys.modules:
                importlib.reload(sys.modules[module_path])
                print(f"🔄 [HELLAS] تـم تحديث: {module_path}")
            else:
                importlib.import_module(module_path)
                print(f"✅ [HELLAS] تـم تفعيل: {module_path}")
        except Exception as e:
            print(f"❌ [HELLAS] خطأ في {module_path}: {e}")

async def run_update():
    """سحب الملفات الجديدة من GitHub واستبدالها محلياً"""
    run_dir = os.getcwd()
    run_dir_q = shlex.quote(run_dir)
    
    os.system(f"rm -rf TempHellas")
    clone_cmd = f"git clone -b {shlex.quote(GH_BRANCH)} {shlex.quote(REPO_URL)} TempHellas"
    os.system(clone_cmd)

    if os.path.exists("TempHellas/hellas"):
        # استبدال المجلد القديم بالجديد
        os.system(f"rm -rf hellas && cp -r TempHellas/hellas ./")
        os.system("rm -rf TempHellas")
        return True
    return False

# --- أوامر التحكم الأساسية ---
@hellas.on(events.NewMessage(outgoing=True, pattern=r"^\.تحديث$"))
async def update_cmd(event):
    await event.edit("**🔄 جاري فحص وتحديث ملفات مجلد HELLAS...**")
    
    # 1. سحب الملفات الجديدة من GitHub
    success = await run_update()
    
    if success:
        # 2. إعادة تحميل الملفات برمجياً بدون إعادة تشغيل البوت
        load_plugins()
        await event.edit("**✅ تم تحديث وتحميل الملفات الجديدة بنجاح!**")
    else:
        await event.edit("**❌ فشل التحديث: تأكد من الرابط أو اسم المستودع.**")

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^\.اطفاء$"))
async def shutdown_cmd(event):
    await event.edit("**᯽︙ تـم إيقـاف تشغيـل النظـام ✓**")
    sys.exit(0)

if __name__ == "__main__":
    print("🚀 محرك HELLAS قيد التشغيل...")
    hellas.start()
    load_plugins()
    print("✅ النظام جاهز.")
    hellas.run_until_disconnected()
