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

# --- التحقق من الإعدادات ---
if os.path.exists("config.txt"):
    with open("config.txt", "r") as f:
        data = f.read().splitlines()
        SESSION_STRING, BOT_TOKEN = data[0], data[1]
else:
    SESSION_STRING = input("أدخل كود الجلسة (String Session): ")
    BOT_TOKEN = input("أدخل توكن البوت (Bot Token): ")
    with open("config.txt", "w") as f:
        f.write(f"{SESSION_STRING}\n{BOT_TOKEN}")

# تعريف المحركين (الحساب + البوت المساعد للأزرار)
hellas = TelegramClient(StringSession(SESSION_STRING), API_ID, API_HASH)
tg_bot = TelegramClient("bot_session", API_ID, API_HASH)

def load_all_plugins():
    """تحميل الملفات الخارجية ديناميكياً"""
    files = glob.glob("*.py")
    for file in files:
        module_name = file.replace(".py", "")
        if module_name in ["main", "__init__"]:
            continue
        try:
            if module_name in sys.modules:
                importlib.reload(sys.modules[module_name])
            else:
                importlib.import_module(module_name)
            print(f"✅ تم تشغيل: {module_name}")
        except Exception as e:
            print(f"❌ خطأ في {module_name}: {e}")

async def run_git_update():
    cmd = (
        f"git init && git remote remove origin || true && "
        f"git remote add origin {REPO_URL} && git fetch --all && "
        f"git reset --hard origin/{GH_BRANCH}"
    )
    return os.system(cmd) == 0

# --- أوامر الإدارة ---
@hellas.on(events.NewMessage(outgoing=True, pattern=r"^\.تحديث$"))
async def update_handler(event):
    await event.edit("**🔄 جاري تحديث كافة ملفات السورس...**")
    if await run_git_update():
        await event.edit("**✅ تم التحديث! جاري إعادة التشغيل...**")
        os.execl(sys.executable, sys.executable, *sys.argv)
    else:
        await event.edit("**❌ فشل التحديث.**")

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^\.اطفاء$"))
async def shutdown_handler(event):
    await event.edit("**᯽︙ تم إيقاف التشغيل ✓**")
    sys.exit(0)

async def start_hellas():
    # تشغيل الحساب
    await hellas.start()
    # تشغيل البوت المساعد (ضروري للأزرار)
    await tg_bot.start(bot_token=BOT_TOKEN)
    # تحميل باقي الملفات (مثل ملف الأوامر)
    load_all_plugins()
    print("🚀 HELLAS System is Ready!")

if __name__ == "__main__":
    hellas.loop.run_until_complete(start_hellas())
    hellas.run_until_disconnected()
