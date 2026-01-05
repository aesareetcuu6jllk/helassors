import __main__ as main_module
import requests
import urllib.parse
from telethon import events

# ربط المحرك
hellas = main_module.hellas

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^\. ذكاء ([\s\S]*)"))
async def ai_handler(event):
    user_text = event.pattern_match.group(1)
    
    await event.edit("**🔍 جاري الاتصال بخوادم الذكاء الاصطناعي...**")
    
    # تحويل النص العربي إلى صيغة تفهمها الروابط (URL Encoding)
    query = urllib.parse.quote(user_text)
    api_url = f"https://sonnet3-5.free.nf/api/reasoning.php?text={query}"
    
    # إضافة Headers ليوهم الموقع أننا متصفح حقيقي (يمنع الـ Disconnect)
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Accept": "application/json"
    }
    
    try:
        # إرسال الطلب مع مهلة زمنية (Timeout)
        response = requests.get(api_url, headers=headers, timeout=20)
        
        if response.status_code == 200:
            # محاولة قراءة الرد كـ JSON، وإذا فشل نقرأه كنص عادي
            try:
                data = response.json()
                result = data.get("response", "لم أجد حقل 'response' في الرد.")
            except:
                result = response.text
            
            # إرسال النتيجة (تقسيمها إذا كانت طويلة جداً)
            if len(result) > 4090:
                result = result[:4090] + "..."
            
            await event.edit(f"**💡 النتيجة:**\n\n{result}")
        else:
            await event.edit(f"**❌ الموقع رد بخطأ رقم: {response.status_code}**")
            
    except requests.exceptions.Timeout:
        await event.edit("**⏳ انتهى وقت الانتظار، الموقع بطيء جداً حالياً.**")
    except Exception as e:
        await event.edit(f"**❌ فشل جلب البيانات:**\n`{e}`")
