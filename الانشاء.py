import __main__ as main_module
from telethon import events
import requests
import json

# ربط المحرك (هيلاس)
hellas = main_module.hellas

# الهيدرز الخاصة بـ API الإنشاء
HEADERS = {
    'Host': 'restore-access.indream.app',
    'x-api-key': 'e758fb28-79be-4d1c-af6b-066633ded128',
    'Content-Type': 'application/json',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'
}

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^\.الانشاء$"))
async def get_reg_date(event):
    # تحديد الهدف (رد أو صاحب الحساب)
    reply = await event.get_reply_message()
    user_target = reply.sender_id if reply else event.sender_id

    try:
        # طلب تاريخ الإنشاء من الـ API
        payload = json.dumps({"telegramId": user_target})
        response = requests.post(
            'https://restore-access.indream.app/regdate', 
            headers=HEADERS, 
            data=payload, 
            timeout=7
        )
        
        if response.status_code == 200:
            res_data = response.json()
            reg_date = res_data.get('data', {}).get('date', "غير متوفر")
            
            # الرد المختصر المطلوب
            await event.edit(f"**انشاء حسابه: {reg_date}**")
        else:
            await event.edit("**❌ عذراً، الـ API لا يستجيب حالياً.**")

    except Exception:
        await event.edit("**❌ حدث خطأ أثناء جلب التاريخ.**")
