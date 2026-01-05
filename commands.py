import re
import __main__ as main_module
from telethon import Button, events

# استدعاء المحرك والبوت المساعد من الملف الرئيسي
hellas = main_module.hellas
# ملاحظة: يجب أن يكون tg_bot معرفاً في main.py كما فعلنا سابقاً
tgbot = getattr(main_module, 'tg_bot', None)

# --- نصوص القوائم ---
ROE = "**♰ هـذه هي قائمة اوامـر سـورس 𝐇𝐞𝐥𝐥𝐚𝐬  ♰**"

l313l0 = """** قائمة اوامر الادمن لسورس HELLAS  **:\n ★•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•★\n ᯽︙ اختر احدى هذه القوائم\n\n- ( `.اوامر الحظر` )\n- ( `.اوامر الكتم` )\n- ( `.اوامر التثبيت` )\n- ( `.اوامر الاشراف` )\n★•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•★\n⌔︙CH : @HELLASUserBot"""
rozbot = """** قائمة اوامر المجـموعه لسورس HELLAS  **:\n ★•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•★\n ᯽︙ اختر احدى هذه القوائم\n\n- ( `.اوامر التفليش` )\n- ( `.اوامر المحذوفين` )\n- ( `.اوامر الكروب` )\n★•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•★\n⌔︙CH : @HELLASUserBot"""
Jmrz = """ ** قائمة اوامر الحساب و الترفيه **:\n ★•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•★\n ᯽︙ اختر احدى هذه القوائم\n\n- ( `.اوامر الترفيه` )\n- ( `.اوامر الحساب` ) \n★•┉ ┉ ┉ ┉ ┉ ┉  ┉ ┉ ┉ ┉•★\n⌔︙CH : @HELLASUserBot"""
# يمكنك إضافة بقية النصوص (t1, t2, t3...) هنا بنفس الطريقة

# مصفوفة الأزرار الرئيسية
MAIN_BUTTONS = [
    [Button.inline("🔐 اوامر الادمن", data="l313l0")],
    [Button.inline("👥 اوامر المجموعة", data="rozbot"), Button.inline("🎭 الحساب والترفيه", data="Jmrz")],
    [Button.inline("📣 النشر التلقائي", data="t8"), Button.inline("🎯 صيد يوزرات", data="t9")],
    [Button.url("📢 قناة السورس", "https://t.me/HELLASUserBot")]
]

# --- معالجة طلب الأوامر من الحساب (Userbot) ---
@hellas.on(events.NewMessage(outgoing=True, pattern=r"^\.اوامري$"))
async def open_menu(event):
    # جلب يوزر البوت المساعد من ملف الإعدادات
    # تأكد أنك وضعت يوزر بوتك هنا أو استخرجه ديناميكياً
    bot_username = (await tgbot.get_me()).username
    
    # مسح رسالة الأمر وإرسال الاستعلام المباشر (Inline Query)
    results = await hellas.inline_query(bot_username, "اوامري")
    await results[0].click(event.chat_id)
    await event.delete()

# --- معالجة الاستعلام المباشر (Inline Handler) عبر البوت المساعد ---
if tgbot:
    @tgbot.on(events.InlineQuery(pattern=r"اوامري"))
    async def inline_handler(event):
        if event.query.user_id == (await hellas.get_me()).id:
            builder = event.builder
            result = builder.article(
                title="Hellas Menu",
                text=ROE,
                buttons=MAIN_BUTTONS
            )
            await event.answer([result])

    # --- معالجة ضغطات الأزرار (Callback Queries) ---
    @tgbot.on(events.CallbackQuery)
    async def callback_handler(event):
        # التأكد أن صاحب الحساب فقط هو من يضغط
        owner_id = (await hellas.get_me()).id
        if event.sender_id != owner_id:
            return await event.answer("⚠️ عذراً، هذه الأزرار تخص صاحب الحساب فقط.", alert=True)

        data = event.data.decode("utf-8")
        
        if data == "l313l0":
            await event.edit(l313l0, buttons=[Button.inline("⬅️ رجوع", data="main_menu")])
        
        elif data == "rozbot":
            await event.edit(rozbot, buttons=[Button.inline("⬅️ رجوع", data="main_menu")])
            
        elif data == "Jmrz":
            await event.edit(Jmrz, buttons=[Button.inline("⬅️ رجوع", data="main_menu")])

        elif data == "main_menu":
            await event.edit(ROE, buttons=MAIN_BUTTONS)
