# start.py
from main import hellas
from telethon import events

# نقوم بحذف الهاندلر القديم قبل إضافة الجديد لتجنب تكرار الاستجابة
@hellas.on(events.NewMessage(outgoing=True, pattern=r"^\.فحص$"))
async def check(event):
    await event.edit("**🤖 النظام يعمل ومحدث فورا!**")

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^\.المطور$"))
async def check(event):
    await event.edit("**🤖 المطور هيلاس: @t00t0**")
