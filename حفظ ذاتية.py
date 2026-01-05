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
    await event.edit("**᯽︙ تم تفعيل الحفظ التلقائي بنجاح ✓**\n**᯽︙ سيتم حفظ (الصور، الفيديوهات، والبصمات) التي تصلك بالخاص.**")

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^\.(الذاتية تعطيل|ذاتية تعطيل)$"))
async def turn_off(event):
    delgvar("save_self_media")
    await event.edit("**᯽︙ تم تعطيل الحفظ التلقائي بنجاح ✓**")

# --- محرك الحفظ الشامل (بصمات + ميديا) ---
@hellas.on(events.NewMessage(incoming=True, func=lambda e: e.is_private))
async def auto_save_handler(event):
    if gvarstatus("save_self_media"):
        # التحقق إذا كانت الرسالة ميديا (صورة، فيديو، أو بصمة صوتية)
        if event.photo or event.video or event.voice or event.audio:
            try:
                # تحميل الميديا
                media = await event.download_media()
                if media:
                    sender = await event.get_sender()
                    # تحديد نوع الميديا للرسالة
                    media_type = "بصمة صوتية 🎤" if event.voice else "ميديا (صورة/فيديو) 🖼"
                    
                    caption = f"**♡ تم حفظ {media_type} ✓**\n\n**♡ المرسل :** [{sender.first_name}](tg://user?id={event.sender_id})"
                    
                    # الإرسال للمحفوظات
                    await hellas.send_file("me", media, caption=caption)
                    
                    # حذف الملف المؤقت من السيرفر
                    if os.path.exists(media):
                        os.remove(media)
            except Exception as e:
                print(f"Error saving media/voice: {str(e)}")

# --- جلب يدوي لأي ميديا (بالرد) ---
@hellas.on(events.NewMessage(outgoing=True, pattern=r"^\.(جلب|ذاتية)$"))
async def manual_save(event):
    if not event.is_reply:
        return await event.edit("**᯽︙ رد على (صورة، فيديو، أو بصمة) أولاً!**")
    
    reply_msg = await event.get_reply_message()
    await event.edit("**᯽︙ جاري الجلب...**")
    media = await reply_msg.download_media()
    if media:
        await hellas.send_file("me", media, caption="**᯽︙ تم الجلب بنجاح ✓**")
        await event.delete()
        if os.path.exists(media):
            os.remove(media)
    else:
        await event.edit("**᯽︙ فشل الجلب!**")
