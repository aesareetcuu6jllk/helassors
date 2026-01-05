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

# إعدادات المستودع
GH_OWNER = "aesareetcuu6jllk"
GH_REPO = "helassors"
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

def load_all_files():
    """تحميل كافة الملفات البرمجية بجانب المحرك"""
    files = glob.glob("*.py")
    for name in files:
        module_name = name.replace(".py", "")
        if module_name in ["main", "__init__"]:
            continue
        try:
            if module_name in sys.modules:
                importlib.reload(sys.modules[module_name])
            else:
                importlib.import_module(module_name)
            print(f"✅ تم تفعيل: {module_name}")
        except Exception as e:
            print(f"❌ خطأ في {module_name}: {e}")

async def run_git_update():
    """تحديث ذكي يكتشف الفرع تلقائياً ويجبر التحديث"""
    run_dir = os.getcwd()
    run_dir_q = shlex.quote(run_dir)
    
    # أوامر Git المحدثة: تقوم بتنظيف الإعدادات وجلب الفرع الافتراضي تلقائياً
    cmd = (
        f"cd {run_dir_q} && "
        f"git config --global user.email 'hellas@bot.com' && "
        f"git config --global user.name 'HellasBot' && "
        f"git init && "
        f"git remote remove origin || true && "
        f"git remote add origin {REPO_URL} && "
        f"git fetch --all && "
        f"git reset --hard origin/$(git remote show origin | grep 'HEAD branch' | cut -d' ' -f5)"
    )
    return os.system(cmd) == 0

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^\.تحديث$"))
async def update_handler(event):
    await event.edit("**🔄 جاري تحديث نظام HELLAS (سحب ذكي)...**")
    
    if await run_git_update():
        await event.edit("**✅ تم التحديث بنجاح! جاري إعادة تشغيل المحرك...**")
        os.execl(sys.executable, sys.executable, *sys.argv)
    else:
        # إذا فشل السحب الذكي، نجرب السحب البسيط (للطوارئ)
        await event.edit("**⚠️ فشل السحب الذكي، جاري محاولة السحب المباشر...**")
        os.system(f"git pull {REPO_URL}")
        os.execl(sys.executable, sys.executable, *sys.argv)

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^\.اطفاء$"))
async def shutdown_handler(event):
    await event.edit("**᯽︙ تـم إيقـاف التشغيـل ✓**")
    sys.exit(0)

if __name__ == "__main__":
    print("🚀 محرك HELLAS يبدأ العمل...")
    hellas.start()
    load_all_files()
    print("✅ النظام جاهز.")
    hellas.run_until_disconnected()
