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
GH_OWNER = "aesareetcuu6jllk"
GH_REPO = "helassors"
GH_BRANCH = "HuRe"
REPO_URL = f"https://{GIT_TOKEN}@github.com/{GH_OWNER}/{GH_REPO}.git"

# --- نظام الجلسة ---
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
    """تحميل وإعادة تحميل الملفات برمجياً دون توقف"""
    files = glob.glob("*.py")
    for name in files:
        module_name = name.replace(".py", "")
        if module_name in ["main", "__init__"]:
            continue
        try:
            if module_name in sys.modules:
                importlib.reload(sys.modules[module_name])
                print(f"🔄 تم تحديث تشغيل: {module_name}")
            else:
                importlib.import_module(module_name)
                print(f"✅ تم تفعيل ملف جديد: {module_name}")
        except Exception as e:
            print(f"❌ خطأ في {module_name}: {e}")

async def auto_updater():
    """وظيفة تعمل في الخلفية لسحب التحديثات فوراً"""
    while True:
        try:
            run_dir = os.getcwd()
            # أمر سحب التحديثات بهدوء
            cmd = (
                f"cd {run_dir} && "
                f"git fetch origin {GH_BRANCH} && "
                f"git reset --hard origin/{GH_BRANCH}"
            )
            # إذا حدث تغيير فعلي في الملفات
            process = os.popen(cmd)
            output = process.read()
            
            if "Updating" in output or "Files changed" in output or "Aborting" not in output:
                print("📡 تم اكتشاف تحديث جديد في GitHub.. جاري التحميل...")
                load_plugins()
        except Exception as e:
            print(f"⚠️ خطأ في المحدث التلقائي: {e}")
        
        # يفحص كل 30 ثانية (يمكنك تقليلها أو زيادتها)
        await asyncio.sleep(30)

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^\.تحديث$"))
async def manual_update(event):
    await event.edit("**🔄 جاري فحص التحديثات يدوياً...**")
    os.system(f"git fetch --all && git reset --hard origin/{GH_BRANCH}")
    load_plugins()
    await event.edit("**✅ تم تحديث كافة الملفات وتشغيلها فوراً!**")

if __name__ == "__main__":
    print("🚀 نظام HELLAS يعمل الآن بنظام التحديث الفوري...")
    hellas.start()
    
    # تحميل الملفات لأول مرة
    load_plugins()
    
    # تشغيل المحدث التلقائي في الخلفية
    hellas.loop.create_task(auto_updater())
    
    print("✅ البوت يراقب GitHub الآن.. أي تعديل سيُنفذ فوراً.")
    hellas.run_until_disconnected()
