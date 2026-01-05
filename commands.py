import __main__ as main_module
from telethon import events, Button

# ربط المحركين من الملف الرئيسي
hellas = main_module.hellas
tg_bot = main_module.tg_bot

# 1. أمر اليوزر بوت (عندما تكتب .اوامري)
@hellas.on(events.NewMessage(outgoing=True, pattern=r"^\.اوامري$"))
async def my_menu(event):
    bot_me = await tg_bot.get_me()
    try:
        # إرسال طلب انلاين للبوت بكلمة "start"
        results = await hellas.inline_query(bot_me.username, "start")
        await results[0].click(event.chat_id)
        await event.delete()
    except Exception as e:
        await event.edit(f"**❌ خطأ في استجابة البوت:**\n`{e}`")

# 2. معالج الانلاين (داخل البوت المساعد) - هذا اللي يحل مشكلة الـ Timeout
@tg_bot.on(events.InlineQuery(pattern=r"start"))
async def inline_handler(event):
    builder = event.builder
    # تصميم الأزرار
    buttons = [
        [Button.inline("🔐 الأوامر", data="cmds"), Button.inline("⚙️ الإعدادات", data="sett")],
        [Button.url("📢 قناة السورس", "https://t.me/HELLASUserBot")]
    ]
    # الرد الفوري لمنع الـ Timeout
    result = builder.article(
        title="HELLAS MENU",
        text="**♰ هـذه هي قائمة اوامـر سـورس 𝐇𝐞𝐥𝐥𝐚𝐬 ♰**",
        buttons=buttons
    )
    await event.answer([result])

# 3. معالج ضغطات الأزرار
@tg_bot.on(events.CallbackQuery)
async def callback(event):
    if event.data == b"cmds":
        await event.edit("**📚 قائمة الأوامر قيد التطوير...**", buttons=[Button.inline("⬅️ رجوع", data="back")])
    elif event.data == b"back":
        # إعادة القائمة الرئيسية
        buttons = [
            [Button.inline("🔐 الأوامر", data="cmds"), Button.inline("⚙️ الإعدادات", data="sett")],
            [Button.url("📢 قناة السورس", "https://t.me/HELLASUserBot")]
        ]
        await event.edit("**♰ هـذه هي قائمة اوامـر سـورس 𝐇𝐞لّا𝐬 ♰**", buttons=buttons)
