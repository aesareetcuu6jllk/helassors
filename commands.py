import __main__ as main_module # استيراد الملف الرئيسي
from telethon import events, Button

# ربط المحركين
hellas = main_module.hellas # الحساب
tg_bot = main_module.tg_bot # البوت المساعد

# أمر يكتبه الحساب لإظهار الأزرار
@hellas.on(events.NewMessage(outgoing=True, pattern=r"^\.الأوامر$"))
async def my_menu(event):
    # إنشاء الأزرار
    buttons = [
        [Button.inline("قسم الإدارة", data="admin"), Button.inline("قسم الحماية", data="security")],
        [Button.url("قناة السورس", "https://t.me/HELLASUserBot")]
    ]
    # البوت يرسل الرسالة نيابة عن الحساب لتظهر الأزرار
    bot_me = await tg_bot.get_me()
    results = await hellas.inline_query(bot_me.username, "menu")
    await results[0].click(event.chat_id)
    await event.delete()

# معالج ضغطات الأزرار
@tg_bot.on(events.CallbackQuery)
async def callback(event):
    if event.data == b"admin":
        await event.edit("**🔐 أوامر الإدارة:**\n- `.طرد`\n- `.حظر`")
