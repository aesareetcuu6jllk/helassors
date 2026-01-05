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

# جلب الإعدادات
GH_OWNER = os.getenv("HELLAS_GH_OWNER", "aesareetcuu6jllk")
GH_REPO = os.getenv("HELLAS_REPO", "helassors") # تأكد من الاسم (هل هو helassors بـ l واحدة؟)
GH_BRANCH = os.getenv("HELLAS_BRANCH", "HuRe")
REPO_URL = f"https://github.com/{GH_OWNER}/{GH_REPO}.git"

# --- نظام الجلسة والتوكن ---
if os.path.exists("config.txt"):
    with open("config.txt", "r") as f:
        data = f.read().splitlines()
        SESSION_STRING, BOT_TOKEN = data[0], data[1]
else:
    print("首次运行: 请输入必要信息")
    SESSION_STRING = input("أدخل كود الجلسة (String Session): ")
    BOT_TOKEN = input("أدخل توكن البوت (Bot Token): ")
    with open("config.txt", "w") as f:
        f.write(f"{SESSION_STRING}\n{BOT_TOKEN}")

# تعريف المحرك باسم hellas
hellas = TelegramClient(StringSession(SESSION_STRING), API_ID, API_HASH)

def load_plugins():
    """تحميل وتشغيل كافة الملفات من مجلد hellas فوراً"""
    if not os.path.exists("hellas"):
        os.makedirs("hellas")
        return

    # إضافة ملف __init__.py برمجياً لضمان التعرف على المجلد كمكتبة
    if not os.path.exists("hellas/__init__.py"):
        with open("hellas/__init__.py", "w") as f:
            pass

    path = "hellas/*.py"
    files = glob.glob(path)
    for name in files:
        if name.endswith("__init__.py"):
            continue
        
        # تحويل المسار من hellas/test.py إلى hellas.test
        module_path = name.replace(".py", "").replace(os.sep, ".")
        
        try:
            # استيراد الموديول وتفعيله
            importlib.import_module(module_path)
            print(f"✅ تم تشغيل الإضافة: {module_path}")
        except Exception as e:
            print(f"❌ خطأ أثناء تشغيل {module_path}: {e}")

async def run_update():
    """منطق التحديث (Clone -> Move -> Restart)"""
    run_dir = os.getcwd()
    run_dir_q = shlex.quote(run_dir)

    os.system(f"rm -rf TempHellas")
    cmd_clone = (
        f"git clone -b {shlex.quote(GH_BRANCH)} {shlex.quote(REPO_URL)} TempHellas"
    )
    os.system(cmd_clone)

    if os.path.exists("TempHellas/hellas"):
        os.system(f"rm -rf hellas && cp -r TempHellas/hellas ./")
        if os.path.exists("TempHellas/requirements.txt"):
            os.system("pip install --no-cache-dir -r TempHellas/requirements.txt")
        
        os.system("rm -rf TempHellas")
        return True
    return False

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^\.تحديث$"))
async def update_cmd(event):
    await event.edit("**🔄 جاري تحديث الملفات وتشغيل الإضافات الجديدة...**")
    success = await run_update()
    if success:
        await event.edit("**✅ تم التحديث بنجاح! جاري إعادة التشغيل لتفعيل الملفات...**")
        os.execl(sys.executable, sys.executable, *sys.argv)
    else:
        await event.edit("**❌ فشل التحديث: تأكد من رابط المستودع ومجلد hellas.**")

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^\.اطفاء$"))
async def shutdown_cmd(event):
    await event.edit("**᯽︙ تـم إيقـاف تشغيـل البـوت بنجـاح ✓**")
    sys.exit(0)

if __name__ == "__main__":
    print("🚀 Hellas Userbot is Starting...")
    # تشغيل العميل (Client)
    hellas.start()
    
    # تحميل الملفات من المجلد فوراً بعد تشغيل العميل
    load_plugins()
    
    print("✅ تم تحميل كافة الملفات في مجلد hellas.")
    hellas.run_until_disconnected()
