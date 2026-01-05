# بدلاً من الاستيراد من main بشكل مباشر قد يسبب تعليق، نستخدم الطريقة التالية:
import __main__ as main_module
from telethon import events

# الوصول للعميل hellas الموجود في الملف الرئيسي
hellas = main_module.hellas

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^\.فحص$"))
async def test_cmd(event):
    await event.edit("**✅ نظام HELLAS يعمل بنجاح!**\n**تم تفعيل ملف start.py.**")

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^\.هلو$"))
async def hello_cmd(event):
    await event.reply("اهلا بك في نظام هيلاس المطور 🚀")
