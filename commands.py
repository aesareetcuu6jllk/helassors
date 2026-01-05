from telethon import events, Button
import __main__ as main_module

# استدعاء المحرك من الملف الرئيسي
hellas = main_module.hellas

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^\.اوامري$"))
async def my_commands(event):
    # مصفوفة الأزرار
    buttons = [
        [
            Button.inline("👤 أوامر الحساب", data="acc_cmds"),
            Button.inline("🛡️ أوامر الحماية", data="sec_cmds")
        ],
        [
            Button.inline("⚙️ إعدادات النظام", data="sys_cmds"),
            Button.url("📢 قناة السورس", "https://t.me/your_channel")
        ]
    ]
    
    await event.edit("Welcome to **HELLAS** System 🚀\nإليك قائمة التحكم بالأوامر، اختر القسم المطلوب:", buttons=buttons)

# معالج ضغطات الأزرار (Callback Queries)
@hellas.on(events.CallbackQuery)
async def callback_handler(event):
    sender = await event.get_sender()
    
    # التأكد أن صاحب الحساب فقط هو من يتحكم بالأزرار
    if event.sender_id != hellas.uid:
        return await event.answer("⚠️ عذراً، هذه الأزرار تخص صاحب الحساب فقط.", alert=True)

    if event.data == b"acc_cmds":
        text = (
            "**👤 قسم أوامر الحساب:**\n\n"
            "• `.فحص` : للتأكد من عمل النظام.\n"
            "• `.هلو` : إرسال رسالة ترحيب.\n"
            "• `.ايدي` : لجلب معرفك الشخصي."
        )
        await event.edit(text, buttons=[Button.inline("⬅️ رجوع", data="main_menu")])

    elif event.data == b"sec_cmds":
        text = (
            "**🛡️ قسم أوامر الحماية:**\n\n"
            "• `.حظر` : لحظر مستخدم من الحساب.\n"
            "• `.الغاء_حظر` : لفك الحظر.\n"
            "• `.تنظيف` : لمسح الرسائل غير المرغوب بها."
        )
        await event.edit(text, buttons=[Button.inline("⬅️ رجوع", data="main_menu")])

    elif event.data == b"sys_cmds":
        text = (
            "**⚙️ إعدادات النظام:**\n\n"
            "• `.تحديث` : لجلب آخر التحديثات من GitHub.\n"
            "• `.اطفاء` : لإيقاف تشغيل النظام بالكامل."
        )
        await event.edit(text, buttons=[Button.inline("⬅️ رجوع", data="main_menu")])

    elif event.data == b"main_menu":
        # العودة للقائمة الرئيسية
        buttons = [
            [Button.inline("👤 أوامر الحساب", data="acc_cmds"), Button.inline("🛡️ أوامر الحماية", data="sec_cmds")],
            [Button.inline("⚙️ إعدادات النظام", data="sys_cmds")]
        ]
        await event.edit("قائمة التحكم الرئيسية:", buttons=buttons)
