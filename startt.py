from main import hellas
from telethon import events

# أمر بسيط للتجربة
@hellas.on(events.NewMessage(outgoing=True, pattern=r"^\.فحص$"))
async def test_cmd(event):
    await event.edit("**✅ نظام HELLAS يعمل بنجاح!**\n**تم استدعاء ملف start.py تلقائياً.**")

# أمر ترحيب
@hellas.on(events.NewMessage(outgoing=True, pattern=r"^\.هلو$"))
async def hello_cmd(event):
    await event.reply("اهلا بك في نظام هيلاس المطور 🚀")
