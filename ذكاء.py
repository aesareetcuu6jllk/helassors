import __main__ as main_module
import asyncio
import urllib.parse
from telethon import events
from DrissionPage import ChromiumPage, ChromiumOptions

# ربط المحرك
hellas = main_module.hellas

def get_ai_response(text):
    """وظيفة تفتح متصفح حقيقي لتجاوز الحماية"""
    # إعدادات المتصفح (بدون واجهة رسومية ليعمل على السيرفر)
    co = ChromiumOptions().set_browser_path('') # اتركها فارغة إذا كان الكروم مثبت تلقائياً
    co.set_argument('--no-sandbox')
    co.set_argument('--headless') # تشغيل مخفي
    
    page = ChromiumPage(co)
    try:
        query = urllib.parse.quote(text)
        url = f"https://sonnet3-5.free.nf/api/reasoning.php?text={query}"
        
        # فتح الموقع والانتظار حتى يتم فك التشفير تلقائياً
        page.get(url)
        
        # الانتظار حتى يظهر الرد (تخطي حماية AES)
        # الموقع يحتاج حوالي 5-8 ثواني ليفك التشفير
        page.wait(5, 10) 
        
        # الحصول على النص الظاهر في الصفحة (الذي هو الرد)
        result = page.json or page.html
        
        # إذا كان الرد JSON داخل الصفحة، نقوم بتنظيفه
        if '"response":' in page.text:
            import json
            data = json.loads(page.text)
            return data.get("response")
        else:
            return page.text
            
    except Exception as e:
        return f"خطأ في المتصفح: {str(e)}"
    finally:
        page.quit()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^\. ذكاء ([\s\S]*)"))
async def ai_handler(event):
    user_text = event.pattern_match.group(1)
    await event.edit("**🌐 جاري فتح متصفح كروم وتجاوز الحماية...**")
    
    # تشغيل المتصفح في خيط (Thread) منفصل لكي لا يتوقف السورس
    loop = asyncio.get_event_loop()
    result = await loop.run_in_executor(None, get_ai_response, user_text)
    
    if "<html>" in result or "Javascript" in result:
        await event.edit("**❌ فشل التجاوز حتى بالمتصفح، الموقع يكتشف السيرفرات.**")
    else:
        await event.edit(f"**💡 النتيجة النهائية:**\n\n{result}")
