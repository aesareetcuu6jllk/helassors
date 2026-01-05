import os
import sys
import glob
import importlib
import asyncio
from telethon import TelegramClient, events, functions, types
from telethon.sessions import StringSession

# --- الإعدادات الأساسية ---
API_ID = 29827519 
API_HASH = "9afadf1ec94457c6bb383139555a2bdc"
GIT_TOKEN = "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" 
GH_OWNER = "aesareetcuu6jllk"
GH_REPO = "helassors"
REPO_URL = f"https://{GIT_TOKEN}@github.com/{GH_OWNER}/{GH_REPO}.git"

# --- التحقق من الإعدادات ---
if os.path.exists("config.txt"):
    with open("config.txt", "r") as f:
        data = f.read().splitlines()
        SESSION_STRING, BOT_TOKEN = data[0], data[1]
else:
    SESSION_STRING = input("أدخل كود الجلسة: ")
    BOT_TOKEN = input("أدخل توكن البوت: ")
    with open("config.txt", "w") as f:
        f.write(f"{SESSION_STRING}\n{BOT_TOKEN}")

hellas = TelegramClient(StringSession(SESSION_STRING), API_ID, API_HASH)
tg_bot = TelegramClient("bot_session", API_ID, API_HASH)

async def auto_enable_inline():
    """تفعيل Inline Mode عبر BotFather تلقائياً"""
    try:
        bot_me = await tg_bot.get_me()
        print(f"🔄 محاولة تفعيل Inline للبوت @{bot_me.username}...")
        async with hellas.conversation("@BotFather") as conv:
            await conv.send_message("/setinline")
            await asyncio.sleep(1)
            await conv.send_message(f"@{bot_me.username}")
            await asyncio.sleep(1)
            await conv.send_message("HELLAS System")
            print("✅ تم التفعيل بنجاح!")
    except:
        print("⚠️ الـ Inline مفعل مسبقاً أو تعذر الوصول لـ BotFather.")

async def keep_online():
    """الحفاظ على الحساب متصلاً"""
    while True:
        try:
            await hellas(functions.account.UpdateStatusRequest(offline=False))
            await asyncio.sleep(120)
        except:
            await asyncio.sleep(30)

async def run_git_update():
    """تحديث السورس وتصحيح مشكلة الفرع (Branch)"""
    # هذا الأمر يجلب اسم الفرع الافتراضي تلقائياً سواء كان HuRe أو main
    cmd = (
        f"git remote remove origin || true && "
        f"git remote add origin {REPO_URL} && "
        f"git fetch --all && "
        f"git reset --hard origin/$(git remote show origin | grep 'HEAD branch' | cut -d' ' -f5)"
    )
    return os.system(cmd) == 0

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^\.تحديث$"))
async def update_handler(event):
    await event.edit("**🔄 جاري تحديث نظام HELLAS...**")
    if await run_git_update():
        await event.edit("**✅ تم التحديث! جاري إعادة التشغيل...**")
        os.execl(sys.executable, sys.executable, *sys.argv)
    else:
        await event.edit("**❌ فشل التحديث: تأكد من GIT_TOKEN أو وجود إنترنت.**")

def load_all_plugins():
    files = glob.glob("*.py")
    for file in files:
        module_name = file.replace(".py", "")
        if module_name in ["main", "__init__"]: continue
        try:
            if module_name in sys.modules:
                importlib.reload(sys.modules[module_name])
            else:
                importlib.import_module(module_name)
            print(f"✅ تم تفعيل: {module_name}")
        except Exception as e:
            print(f"❌ خطأ في {module_name}: {e}")

async def start_hellas():
    await hellas.start()
    await tg_bot.start(bot_token=BOT_TOKEN)
    await auto_enable_inline()
    load_all_plugins()
    hellas.loop.create_task(keep_online())
    print("🚀 HELLAS System is Ready!")

if __name__ == "__main__":
    hellas.loop.run_until_complete(start_hellas())
    hellas.run_until_disconnected()
