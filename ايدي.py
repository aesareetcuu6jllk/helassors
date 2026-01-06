import __main__ as main_module
from telethon import events
from telethon.tl.types import User
from telethon.tl.functions.users import GetFullUserRequest

# ربط المحرك (هيلاس)
hellas = main_module.hellas

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^\.(ايدي|ا|كشف)$"))
async def get_user_info(event):
    # جلب الرسالة المردود عليها أو استخدام صاحب الحساب
    reply = await event.get_reply_message()
    user_target = reply.sender_id if reply else event.sender_id

    try:
        # جلب معلومات المستخدم الكاملة (للحصول على البايو)
        full_user = await event.client(GetFullUserRequest(user_target))
        user = full_user.users[0]
        full_info = full_user.full_user
        
        # 1. جلب الاسم
        xname = user.first_name or "ماكو"
        
        # 2. جلب كافة اليوزرات (المعرفات) مثل الصورة
        usernames = []
        if user.username:
            usernames.append(f"@{user.username}")
        
        # التحقق من وجود معرفات إضافية (للحسابات المميزة أو المرتبطة)
        if hasattr(user, 'usernames') and user.usernames:
            for u in user.usernames:
                formatted_u = f"@{u.username}"
                if formatted_u not in usernames:
                    usernames.append(formatted_u)
        
        xuser = " ".join(usernames) if usernames else "ماكو"
        
        # 3. جلب البايو
        xbio = full_info.about or "لا يوجد بايو"
        
        xid = user.id
        xlink = f"[{xname}](tg://user?id={xid})"
        
        # تحديد الرتبة
        rank = "صاحب السورس 💎" if xid == event.sender_id else "مستخدم 🧸"

        # تنسيق الرسالة النهائي (نفس نمط الصورة)
        msg = (
            "🧸 **تم كشف المعلومات بنجاح**\n\n"
            f"🧑🏻‍💻 ↜ اسمه : {xlink}\n"
            f"📂 ↜ يوزره : {xuser}\n"
            f"📝 ↜ البايو : {xbio}\n"
            f"🆔 ↜ ايديه : ` {xid} `\n"
            f"🧰 ↜ رتبته : {rank}\n\n"
            "**•───── HELLAS ─────•**"
        )

        await event.edit(msg)

    except Exception as e:
        await event.edit(f"**❌ حدث خطأ أثناء جلب البيانات:** `{str(e)}`")
