import __main__ as main_module
import os
import re
import asyncio
from telethon import events, Button

# ربط المحركات الأساسية لسورسك
hellas = main_module.hellas
tg_bot = main_module.tg_bot

# محاولة استيراد قاعدة البيانات بالمسار الصحيح لتجنب خطأ الـ relative import
try:
    from JoKeRUB.sql_helper.globals import addgvar, delgvar, gvarstatus
except Exception:
    try:
        from sql_helper.globals import addgvar, delgvar, gvarstatus
    except Exception:
        # تعريف دوال وهمية في حال عدم وجود قاعدة بيانات لعدم توقف السورس
        def addgvar(a, b): pass
        def delgvar(a): pass
        def gvarstatus(a): return None

# أيام الأسبوع بالعربي
Days_Ar = {
    'Monday': 'الاثنين', 'Tuesday': 'الثلاثاء', 'Wednesday': 'الأربعاء',
    'Thursday': 'الخميس', 'Friday': 'الجمعة', 'Saturday': 'السبت', 'Sunday': 'الأحد'
}

# --- قسم حفظ الصور الذاتية (يدوي) ---
@hellas.on(events.NewMessage(outgoing=True, pattern=r"^\.(جلب الصورة|جلب الصوره|ذاتيه|ذاتية)$"))
async def manual_save(event):
    if not event.is_reply:
        return await event.edit("**᯽︙ يرجى الرد على الصورة/الفيديو الذاتي أولاً!**")
    
    reply_msg = await event.get_reply_message()
    if not reply_msg or not reply_msg.media:
        return await event.edit("**᯽︙ هذا ليس ملف وسائط ذاتي!**")
        
    await event.edit("**᯽︙ جاري الحفظ في الرسائل المحفوظة...**")
    media = await reply_msg.download_media()
    await hellas.send_file("me", media, caption="**᯽︙ تم حفظ الذاتية بنجاح ✓**")
    await event.delete()
    if os.path.exists(media): os.remove(media)

# --- تفعيل وتعطيل الحفظ التلقائي (تخزين دائم بالـ SQL) ---
@hellas.on(events.NewMessage(outgoing=True, pattern=r"^\.(الذاتية تشغيل|ذاتية تشغيل)$"))
async def turn_on_save(event):
    if gvarstatus("savepicforme"):
        return await event.edit("**᯽︙ ميزة حفظ الذاتيات مفعلة بالفعل ✓**")
    addgvar("savepicforme", "true")
    await event.edit("**᯽︙ تم تفعيل حفظ الذاتيات بنجاح ✓ (سيبقى شغالاً حتى بعد التحديث)**")

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^\.(الذاتية تعطيل|ذاتية تعطيل)$"))
async def turn_off_save(event):
    if not gvarstatus("savepicforme"):
        return await event.edit("**᯽︙ ميزة حفظ الذاتيات معطلة بالفعل!**")
    delgvar("savepicforme")
    await event.edit("**᯽︙ تم تعطيل حفظ الذاتيات بنجاح ✓**")

# --- محرك الحفظ التلقائي عند استلام ذاتية ---
@hellas.on(events.NewMessage(func=lambda e: e.is_private and e.media_unread and (e.photo or e.video) and e.sender_id != hellas.uid))
async def auto_save_handler(event):
    if gvarstatus("savepicforme"):
        try:
            media = await event.download_media()
            sender = await event.get_sender()
            date_str = event.date.strftime("%Y-%m-%d")
            day_str = Days_Ar.get(event.date.strftime("%A"), "غير معروف")
            
            caption = f"""**
♡ تم حفظ الذاتية تلقائياً ✓
♡ أسم المرسل : [{sender.first_name}](tg://user?id={event.sender_id})
♡ تاريخ الذاتية : `{date_str}`
♡ أرسلت في يوم `{day_str}`
            **"""
            await hellas.send_file("me", media, caption=caption)
            if os.path.exists(media): os.remove(media)
        except Exception as e:
            print(f"Error in saving self-destruct media: {e}")

# --- قسم الألعاب واللايك ---
@hellas.on(events.NewMessage(outgoing=True, pattern=r"^\.لايك ?(.*)"))
async def like_inline(event):
    query = event.pattern_match.group(1)
    results = await hellas.inline_query("@like", query) 
    await results[0].click(event.chat_id)
    await event.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^\.اكس او$"))
async def xo_inline(event):
    results = await hellas.inline_query("@xoBot", "play")
    await results[0].click(event.chat_id)
    await event.delete()

# --- قسم المساعدة ---
@hellas.on(events.NewMessage(outgoing=True, pattern=r"^\.م27$"))
async def help_27(event):
    help_text = """**᯽︙ أوامر الملف الحالي :**
    
⌔︙الامر • `.ذاتية تشغيل` : لتفعيل الحفظ التلقائي
⌔︙الامر • `.ذاتية تعطيل` : لتعطيل الحفظ التلقائي
⌔︙الامر • `.ذاتية` : لجلب الميديا بالرد
⌔︙الامر • `.همسة` : لعرض شرح الهمسة
⌔︙الامر • `.اكس او` : لبدء لعبة XO
⌔︙الامر • `.لايك` : لعمل زر لايك انلاين"""
    await event.edit(help_text)

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^\.الهمسة$"))
async def whisper_how(event):
    await event.edit("**᯽︙ شـرح كـتابة همـسة سـرية :**\n\nاكتب `.همسة` ثم الرسالة ثم معرف الشخص.\nمثال: `.همسة هلا @معرف_الشخص`")
