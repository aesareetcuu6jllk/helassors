import os
import sys
import glob
import importlib
import asyncio
from telethon import TelegramClient, events
from telethon.sessions import StringSession

# --- الإعدادات الثابتة ---
API_ID = 29827519 
API_HASH = "9afadf1ec94457c6bb383139555a2bdc"

def get_cfg(key: str, default: str = None):
    return os.environ.get(key, default)

# إعدادات الجيت هاب
GH_OWNER = "aesareetcuu6jllk"
GH_REPO = "hellassors"
GH_BRANCH = "HuRe"
# استخدام رابط HTTPS المباشر
REPO_URL = f"https://github.com/{GH_OWNER}/{GH_REPO}.git"

# --- نظام حفظ البيانات (config.txt) ---
if os.path.exists("config.txt"):
    with open("config.txt", "r") as f:
        data = f.read().splitlines()
        SESSION_STRING = data[0]
        BOT_TOKEN = data[1]
else:
    print("--- إعداد التشغيل الأول ---")
    SESSION_STRING = input("أدخل كود الجلسة (String Session): ")
    BOT_TOKEN = input("أدخل توكن البوت (Bot Token): ")
    with open("config.txt", "w") as f:
        f.write(f"{SESSION_STRING}\n{BOT_TOKEN}")

# تعريف المحرك كـ Userbot
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
            if module_name in sys.modules:
                importlib.reload(sys.modules[module_name])
            else:
                importlib.import_module(module_name)
            print(f"✅ تم تفعيل الملف: {module_name}")
        except Exception as e:
            print(f"❌ خطأ في ملف {module_name}: {e}")

async def start_system():
    # تشغيل الحساب الشخصي
    await hellas.start()
    print("🚀 نظام hellas يعمل الآن كـ Userbot على حسابك...")
    load_plugins()

    # --- أمر التحديث التلقائي المعدل لحل مشكلة طلب الرمز ---
    @hellas.on(events.NewMessage(outgoing=True, pattern=r"\.تحديث"))
    async def updater(event):
        await event.edit(f"**🔄 جاري التحديث... يتم الآن تجاوز طلب الرمز للمستودع العام.**")
        
        # 1. تنظيف أي محاولات سابقة
        os.system("rm -rf temp_update")
        
        # 2. السحب مع إجبار Git على عدم طلب كلمة مرور (للمستودعات العامة)
        # تم استخدام بروتوكول يمنع التوقف لطلب الهوية
        cmd = (
            f"git -c core.askpass=true clone --branch {GH_BRANCH} "
            f"--depth 1 {REPO_URL} temp_update"
        )
        os.system(cmd)
        
        # 3. التأكد من نجاح عملية السحب ونقل الملفات
        if os.path.exists("temp_update/hellas"):
            os.system("rm -rf hellas")
            os.system("cp -r temp_update/hellas ./")
            
            # تثبيت المتطلبات إذا وجدت
            if os.path.exists("temp_update/requirements.txt"):
                os.system("pip install --no-cache-dir -r temp_update/requirements.txt")
                
            os.system("rm -rf temp_update")
            await event.edit("**✅ تم التحديث بنجاح دون طلب رمز! جاري إعادة التشغيل الآن...**")
            
            # 4. إعادة تشغيل العملية بالكامل
            os.execl(sys.executable, sys.executable, *sys.argv)
        else:
            await event.edit(
                "**❌ فشل التحديث!**\n"
                "تأكد من أن المستودع عام (Public) وأن الرابط صحيح.\n"
                "إذا استمرت المشكلة، جرب تنفيذ `git config --global --unset user.password` في شاشة السيرفر."
            )

    await hellas.run_until_disconnected()

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(start_system())
