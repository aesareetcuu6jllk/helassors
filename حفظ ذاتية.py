import __main__ as main_module
import os
import asyncio
from telethon import events

# ربط المحركات الأساسية
hellas = main_module.hellas
tg_bot = main_module.tg_bot

# استيراد قاعدة البيانات
try:
    from JoKeRUB.sql_helper.globals import addgvar, delgvar, gvarstatus
except:
    try:
        from sql_helper.globals import addgvar, delgvar, gvarstatus
    except:
        def addgvar(k, v): globals()[k] = v
        def delgvar(k): globals().pop(k, None)
        def gvarstatus(k): return globals().get(k)

# --- تفعيل وتعطيل ---
@hellas.on(events.NewMessage(outgoing=True, pattern=r"^\.(الذاتية تشغيل|ذاتية تشغيل)$"))
async def turn_on(event):
    addgvar("save_self_media", "true")
    await event.edit("**᯽︙ تم تفعيل حفظ الذاتيات بنجاح ✓**\n**᯽︙ سأقوم الآن بحفظ أي صورة أو فيديو يصلك بالخاص تلقائياً.**")

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^\.(الذاتية تعطيل|ذاتية تعطيل)$"))
async def turn_off(event):
    delgvar("save_self_media")
    await event.edit("**᯽︙ تم تعطيل حفظ الذاتيات بنجاح ✓**")

# --- محرك الحفظ التلقائي الصاروخي ---
@hellas.on(events.NewMessage(incoming=True, func=lambda e: e.is_private))
async def auto_save_handler(event):
    # التأكد من التفعيل من قاعدة البيانات
    if gvarstatus("save_self_media"):
        # التحقق إذا كانت الرسالة تحتوي على ميديا (صورة أو فيديو)
        if event.photo or event.video or event.media:
            try:
                # محاولة تحميل الميديا فوراً
                media = await event.download_media()
                if media:
                    sender = await event.get_sender()
                    # جلب الوقت واليوم
                    date_str = event.date.strftime("%Y-%m-%d %I:%M %p")
                    
                    caption = f"**♡ تم حفظ ميديا (ذاتية/عادية) ✓**\n\n**♡ المرسل :** [{sender.first_name}](tg://user?id={event.sender_id})\n**♡ الوقت :** `{date_str}`"
                    
                    # الإرسال للرسائل المحفوظة
                    await hellas.send_file("me", media, caption=caption)
                    
                    # مسح الملف من السيرفر بعد الإرسال
                    if os.path.exists(media):
                        os.remove(media)
            except Exception as e:
                print(f"Error saving media: {str(e)}")

# --- الجلب اليدوي بالرد ---
@hellas.on(events.NewMessage(outgoing=True, pattern=r"^\.(جلب الصورة|جلب الصوره|ذاتيه|ذاتية)$"))
async def manual_save(event):
    if not event.is_reply:
        return await event.edit("**᯽︙ رد على الميديا أولاً!**")
    
    reply_msg = await event.get_reply_message()
    await event.edit("**᯽︙ جاري الجلب...**")
    media = await reply_msg.download_media()
    if media:
        await hellas.send_file("me", media, caption="**᯽︙ تم جلب الميديا بنجاح ✓**")
        await event.delete()
        if os.path.exists(media):
            os.remove(media)
    else:
        await event.edit("**᯽︙ فشل الجلب! قد تكون الميديا منتهية.**")
