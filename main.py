import os
import sys
import glob
import importlib
import asyncio
from telethon import TelegramClient, events
from telethon.sessions import StringSession

# --- الإعدادات الثابتة ---
API_ID = 29827519  # ضع هنا الـ API_ID الخاص بك
API_HASH = "9afadf1ec94457c6bb383139555a2bdc"  # ضع هنا الـ API_HASH الخاص بك

def get_cfg(key: str, default: str = None):
    return os.environ.get(key, default)

# إعدادات الجيت هاب
GH_OWNER = get_cfg("HELLAS_GH_OWNER", "aesareetcuu6jllk")
GH_REPO = get_cfg("HELLAS_REPO", "hellassors")
GH_BRANCH = get_cfg("HELLAS_BRANCH", "HuRe")
REPO_URL = get_cfg("HELLAS_REPO_URL", f"https://github.com/{GH_OWNER}/{GH_REPO}.git")

# --- طلب البيانات عند التشغيل الأول ---
# سيتم حفظها في ملف نصي لكي لا يطلبها كل مرة
if os.path.exists("config.txt"):
    with open("config.txt", "r") as f:
        data = f.read().splitlines()
        SESSION_STRING = data[0]
        BOT_TOKEN = data[1]
else:
    SESSION_STRING = input("أدخل كود الجلسة (String Session): ")
    BOT_TOKEN = input("أدخل توكن البوت (Bot Token): ")
    with open("config.txt", "w") as f:
        f.write(f"{SESSION_STRING}\n{BOT_TOKEN}")

# --- تعريف المحرك باسم hellas ---
# StringSession تجعل البوت يعمل بحسابك الشخصي (Userbot)
hellas = TelegramClient(StringSession(SESSION_STRING), API_ID, API_HASH)

def load_plugins():
    """تحميل الملفات من مجلد hellas"""
    if not os.path.exists("hellas"):
        os.makedirs("hellas")
    
    path = "hellas/*.py"
    files = glob.glob(path)
    for name in files:
        module_name = name.replace(".py", "").replace(os.sep, ".")
        try:
            # حذف الموديول من الذاكرة إذا كان موجوداً لإعادة تحميله
            if module_name in sys.modules:
                importlib.reload(sys.modules[module_name])
            else:
                importlib.import_module(module_name)
            print(f"✅ تم تفعيل الملف: {module_name}")
        except Exception as e:
            print(f"❌ خطأ في ملف {module_name}: {e}")

async def start_system():
    # تشغيل الحساب (Userbot)
    await hellas.start()
    
    # تشغيل البوت المساعد في الخلفية (اختياري)
    # await hellas.start(bot_token=BOT_TOKEN) 
    
    print("🚀 نظام hellas يعمل الآن كـ Userbot على حسابك...")
    load_plugins()

    # --- أمر التحديث (يكتب في الحساب الشخصي) ---
    @hellas.on(events.NewMessage(outgoing=True, pattern=r"\.تحديث"))
    async def updater(event):
        await event.edit(f"**🔄 جاري التحديث من GitHub...**\n**الفرع:** `{GH_BRANCH}`")
        
        os.system("rm -rf temp_update")
        os.system(f"git clone -b {GH_BRANCH} {REPO_URL} temp_update")
        
        if os.path.exists("temp_update/hellas"):
            os.system("rm -rf hellas")
            os.system("cp -r temp_update/hellas ./")
            os.system("rm -rf temp_update")
            await event.edit("**✅ تم التحديث بنجاح! جاري إعادة التشغيل...**")
            os.execl(sys.executable, sys.executable, *sys.argv)
        else:
            await event.edit("**❌ فشل التحديث: تأكد من وجود مجلد hellas في المستودع.**")

    await hellas.run_until_disconnected()

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(start_system())

