import __main__ as main_module
import os
import re
import asyncio
from telethon import events, Button

# ربط المحركات
hellas = main_module.hellas
tg_bot = main_module.tg_bot

# تصحيح مسار قاعدة البيانات
try:
    from JoKeRUB.sql_helper.globals import addgvar, delgvar, gvarstatus
except Exception:
    try:
        from sql_helper.globals import addgvar, delgvar, gvarstatus
    except Exception:
        def addgvar(a, b): pass
        def delgvar(a): pass
        def gvarstatus(a): return None

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
        
    await event.edit("**᯽︙ جاري الحفظ...**")
    media = await reply_msg.download_media()
    
    if media:
        await hellas.send_file("me", media, caption="**᯽︙ تم حفظ الذاتية بنجاح ✓**")
        await event.delete()
        if os.path.exists(media): os.remove(media)
    else:
        await event.edit("**᯽︙ فشل تحميل الملف، قد تكون مدة الذاتية انتهت!**")

# --- تفعيل وتعطيل الحفظ التلقائي ---
@hellas.on(events.NewMessage(outgoing=True, pattern=r"^\.(الذاتية تشغيل|ذاتية تشغيل)$"))
async def turn_on_save(event):
    addgvar("savepicforme", "true")
    await event.edit("**᯽︙ تم تفعيل حفظ الذاتيات بنجاح ✓**")

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^\.(الذاتية تعطيل|ذاتية تعطيل)$"))
async def turn_off_save(event):
    delgvar("savepicforme")
    await event.edit("**᯽︙ تم تعطيل حفظ الذاتيات بنجاح ✓**")

# --- محرك الحفظ التلقائي المصحح ---
# استخدمنا sender_id != (await hellas.get_me()).id لتجنب خطأ الـ uid
@hellas.on(events.NewMessage(func=lambda e: e.is_private and e.media_unread and (e.photo or e.video)))
async def auto_save_handler(event):
    # نتأكد أن الرسالة مو من عندي
    me = await hellas.get_me()
    if event.sender_id == me.id:
        return

    if gvarstatus("savepicforme"):
        try:
            media = await event.download_media()
            if not media:
                return
                
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
            print(f"Error: {e}")

# --- الألعاب والمساعدة ---
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

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^\.م27$"))
async def help_27(event):
    await event.edit("**᯽︙ أوامر الحفظ والألعاب:**\n`.ذاتية تشغيل`\n`.ذاتية تعطيل`\n`.ذاتية` (بالرد)\n`.اكس او`\n`.لايك`")
