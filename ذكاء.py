import __main__ as main_module
import cloudscraper
import urllib.parse
from telethon import events

# ربط المحرك
hellas = main_module.hellas

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^\. ذكاء ([\s\S]*)"))
async def ai_handler(event):
    user_text = event.pattern_match.group(1)
    await event.edit("**🔍 جاري تجاوز حماية الموقع وجلب الرد...**")
    
    query = urllib.parse.quote(user_text)
    api_url = f"https://sonnet3-5.free.nf/api/reasoning.php?text={query}"
    
    # استخدام سكرابر متطور لتجاوز الـ JS Challenge
    scraper = cloudscraper.create_scraper()
    
    try:
        # الطلب باستخدام السكرابر
        response = scraper.get(api_url, timeout=30)
        
        if response.status_code == 200:
            try:
                # محاولة فك الشفرة كـ JSON
                data = response.json()
                result = data.get("response", "لم يتم العثور على رد.")
            except:
                # إذا كان الرد نص مباشر
                result = response.text
                
            # تنظيف الرد من أي تاغات HTML إذا ظهرت
            if "<html>" in result:
                await event.edit("**❌ الموقع يطلب تشغيل ملفات تعريف الارتباط (Cookies) يدوياً، جرب API آخر.**")
            else:
                await event.edit(f"**💡 النتيجة:**\n\n{result}")
        else:
            await event.edit(f"**❌ فشل الموقع في الرد. الكود: {response.status_code}**")
            
    except Exception as e:
        await event.edit(f"**❌ حدث خطأ أثناء التجاوز:**\n`{e}`")
