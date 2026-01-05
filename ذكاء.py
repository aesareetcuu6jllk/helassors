import __main__ as main_module
import requests
from telethon import events

# ربط المحرك من الملف الرئيسي
hellas = main_module.hellas

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^\. ذكاء ([\s\S]*)"))
async def ai_handler(event):
    # جلب النص اللي كتبته بعد كلمة ذكاء
    user_text = event.pattern_match.group(1)
    
    # رسالة مؤقتة بين ما يجي الرد
    await event.edit("**🔍 جاري التفكير...**")
    
    # الرابط اللي طلبته مع النص
    api_url = f"https://sonnet3-5.free.nf/api/reasoning.php?text={user_text}"
    
    try:
        # طلب النتيجة من الموقع
        response = requests.get(api_url)
        
        if response.status_code == 200:
            data = response.json()
            
            # سحب النتيجة من حقل response
            # ملاحظة: إذا كان الرد نص مباشر نستخدم response.text 
            # هنا افترضت أن الرد JSON وفيه حقل اسمه response
            result = data.get("response", "لم يتم العثور على رد.")
            
            # إرسال النتيجة النهائية
            await event.edit(f"**الـرد:**\n\n{result}")
        else:
            await event.edit("**❌ حدث خطأ في الاتصال بالموقع.**")
            
    except Exception as e:
        # إذا واجهنا مشكلة بالكود أو الموقع
        await event.edit(f"**❌ فشل جلب البيانات:**\n`{e}`")

