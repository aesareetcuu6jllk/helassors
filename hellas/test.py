from main import hellas  # استدعاء المحرك الأساسي من الملف الرئيسي
from telethon import events

@hellas.on(events.NewMessage(outgoing=True, pattern=r"\.تجربة"))
async def check_hellas(event):
    """أمر بسيط للتأكد من أن النظام يعمل بنجاح"""
    await event.edit("**✅ نظام hellas يعمل بنجاح!**\n\n**᯽︙ الحساب الآن متصل بالكامل وبإمكانك استخدام كافة الإضافات.**")
