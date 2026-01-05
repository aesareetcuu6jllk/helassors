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

# توكن الوصول الخاص بك (للمستودعات الخاصة والعامة)
GIT_TOKEN = "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" 

# إعدادات المستودع
GH_OWNER = "aesareetcuu6jllk"
GH_REPO = "helassors"
GH_BRANCH = "HuRe"

# الرابط المشفر لتجاوز طلبات تسجيل الدخول
REPO_URL = f"https://{GIT_TOKEN}@github.com/{GH_OWNER}/{GH_REPO}.git"

# --- نظام الجلسة والبيانات المحلية ---
if os.path.exists("config.txt"):
    with open("config.txt", "r") as f:
        data = f.read().splitlines()
        SESSION_STRING, BOT_TOKEN = data[0], data[1]
else:
    print("首次运行: يرجى إدخال البيانات المطلوبة في الشاشة")
    SESSION_STRING = input("أدخل كود الجلسة (String Session): ")
    BOT_TOKEN = input("أدخل توكن البوت (Bot Token): ")
    with open("config.txt", "w") as f:
        f.write(f"{SESSION_STRING}\n{BOT_TOKEN}")

# المحرك الأساسي (Userbot)
hellas = TelegramClient(StringSession(SESSION_STRING), API_ID, API_HASH)

def load_plugins():
    """تحميل وتشغيل كافة الملفات من مجلد hellas كجزء من النظام"""
    if not os.path.exists("hellas"):
        os.makedirs("hellas")
    
    # ضمان وجود ملف التهيئة ليعمل المجلد كمكتبة
    if not os.path.exists("hellas/__init__.py"):
        with open("hellas/__init__.py", "w") as f: pass

    # البحث عن جميع ملفات البايثون داخل المجلد
    path = "hellas/*.py"
    files = glob.glob(path)
    for name in files:
        if name.endswith("__init__.py"):
            continue
        
        # تحويل المسار إلى صيغة برمجية قابلة للاستدعاء (hellas.filename)
        module_path = name.replace(".py", "").replace(os.sep, ".")
        
        try:
            # استدعاء الملف وتفعيله فوراً
            importlib.import_module(module_path)
            print(f"✅ [HELLAS] تـم تفعيل: {module_path}")
        except Exception as e:
            print(f"❌ [HELLAS] خطأ في {module_path}: {e}")

async def run_update():
    """تحديث مجلد hellas بالكامل من GitHub"""
    run_dir = os.getcwd()
    run_dir_q = shlex.quote(run_dir)
    
    # تنظيف المجلد المؤقت
    os.system(f"rm -rf TempHellas")
    
    # عملية السحب باستخدام التوكن والفرع المحدد
    clone_cmd = f"git clone -b {shlex.quote(GH_BRANCH)} {shlex.quote(REPO_URL)} TempHellas"
    os.system(clone_cmd)

    if os.path.exists("TempHellas/hellas"):
        # حذف المجلد القديم واستبداله بالجديد
        os.system(f"rm -rf hellas && cp -r TempHellas/hellas ./")
        
        # تحديث المكتبات إذا لزم الأمر
        if os.path.exists("TempHellas/requirements.txt"):
            os.system("pip install --no-cache-dir -r TempHellas/requirements.txt")
        
        os.system("rm -rf TempHellas")
        return True
    return False

# --- أوامر التحكم الأساسية ---
@hellas.on(events.NewMessage(outgoing=True, pattern=r"^\.تحديث$"))
async def update_cmd(event):
    await event.edit("**🔄 جاري تحديث مجلد HELLAS من السحابة...**")
    success = await run_update()
    if success:
        await event.edit("**✅ تم تحديث المجلد بنجاح! جاري إعادة تشغيل الإضافات...**")
        os.execl(sys.executable, sys.executable, *sys.argv)
    else:
        await event.edit("**❌ فشل التحديث: تأكد من اسم المستودع (helassors) والفرع (HuRe).**")

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^\.اطفاء$"))
async def shutdown_cmd(event):
    await event.edit("**᯽︙ تـم إيقـاف تشغيـل النظـام ✓**")
    sys.exit(0)

if __name__ == "__main__":
    print("🚀 محرك HELLAS قيد التشغيل...")
    # بدء اتصال التليجرام
    hellas.start()
    
    # تشغيل كافة ملفات المجلد
    load_plugins()
    
    print("✅ النظام جاهز الآن. يمكنك استخدام أوامر مجلد hellas.")
    hellas.run_until_disconnected()
