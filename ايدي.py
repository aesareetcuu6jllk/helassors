import __main__ as main_module
from telethon import events
from telethon.tl.types import User
from telethon.tl.functions.users import GetFullUserRequest
import requests
import json

# ربط المحرك (هيلاس)
hellas = main_module.hellas

# هيدرز الـ API الخاص بتأريخ الإنشاء
HEADERS = {
    'Host': 'restore-access.indream.app',
    'x-api-key': 'e758fb28-79be-4d1c-af6b-066633ded128',
    'Content-Type': 'application/json',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'
}

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^\.(ايدي|ا|كشف)$"))
async def get_full_user_info(event):
    await event.edit("**᯽︙ جاري كشف المعلومات الكاملة...**")
    
    # تحديد الهدف (رد أو صاحب الحساب)
    reply = await event.get_reply_message()
    user_target = reply.sender_id if reply else event.sender_id

    try:
        # 1. جلب بيانات المستخدم الكاملة
        full_user = await event.client(GetFullUserRequest(user_target))
        user = full_user.users[0]
        full_info = full_user.full_user
        
        xname = user.first_name or "ماكو"
        xid = user.id
        xbio = full_info.about or "لا يوجد بايو"
        
        # جلب كافة اليوزرات
        usernames = [f"@{user.username}"] if user.username else []
        if hasattr(user, 'usernames') and user.usernames:
            for u in user.usernames:
                if f"@{u.username}" not in usernames:
                    usernames.append(f"@{u.username}")
        xuser = " ".join(usernames) if usernames else "ماكو"
        
        # 2. جلب تاريخ الإنشاء من الـ API
        reg_date = "غير متوفر"
        try:
            payload = json.dumps({"telegramId": xid})
            response = requests.post('https://restore-access.indream.app/regdate', headers=HEADERS, data=payload, timeout=5)
            if response.status_code == 200:
                reg_date = response.json().get('data', {}).get('date', "غير متوفر")
        except:
            reg_date = "فشل الجلب"

        # تحديد الرتبة
        rank = "صاحب السورس 💎" if xid == event.sender_id else "مستخدم 🧸"
        xlink = f"[{xname}](tg://user?id={xid})"

        # 3. تنسيق الرسالة
        msg = (
            "🧸 **تم كشف المعلومات بنجاح**\n\n"
            f"🧑🏻‍💻 ↜ اسمه : {xlink}\n"
            f"📂 ↜ يوزره : {xuser}\n"
            f"📝 ↜ البايو : {xbio}\n"
            f"🆔 ↜ ايديه : ` {xid} `\n"
            f"📅 ↜ الإنشاء : **{reg_date}**\n"
            f"🧰 ↜ رتبته : {rank}\n\n"
            "**•───── HELLAS ─────•**"
        )

        # 4. إرسال الصورة والمعلومات
        photos = await event.client.get_profile_photos(xid, limit=1)
        if photos:
            await event.client.send_file(event.chat_id, photos[0], caption=msg)
            await event.delete()
        else:
            await event.edit(msg)

    except Exception as e:
        await event.edit(f"**❌ حدث خطأ:** `{str(e)}`")
