import __main__ as main_module
import os
import asyncio
from telethon import events

# ربط المحركات الأساسية
hellas = main_module.hellas
tg_bot = main_module.tg_bot

# مسار ملف التخزين البديل لضمان عدم النسيان بعد التحديث
STATUS_FILE = "self_save_status.txt"

def is_enabled():
    # فحص قاعدة البيانات أولاً، ثم الملف النصي
    try:
        from JoKeRUB.sql_helper.globals import gvarstatus
        if gvarstatus("save_self_media"): return True
    except:
        pass
    return os.path.exists(STATUS_FILE)

# --- تفعيل وتعطيل ---
@hellas.on(events.NewMessage(outgoing=True, pattern=r"^\.(الذاتية تشغيل|ذاتية تشغيل)$"))
async def turn_on(event):
    # حفظ في قاعدة البيانات (للاحتياط)
    try:
        from JoKeRUB.sql_helper.globals import addgvar
        addgvar("save_self_media", "true")
    except:
        pass
    # حفظ في ملف نصي (لضمان البقاء بعد التحديث)
    with open(STATUS_FILE, "w") as f:
        f.write("on")
    
    await event.edit("**᯽︙ تم تفعيل حفظ الذاتيات بنجاح ✓**\n**᯽︙ سيبقى التفعيل شغالاً حتى بعد التحديث والريستارت.**")

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^\.(الذاتية تعطيل|ذاتية تعطيل)$"))
async def turn_off(event):
    try:
        from JoKeRUB.sql_helper.globals import delgvar
        delgvar("save_self_media")
    except:
        pass
    if os.path.exists(STATUS_FILE):
        os.remove(STATUS_FILE)
    await event.edit("**᯽︙ تم تعطيل حفظ الذاتيات بنجاح ✓**")

# --- محرك الحفظ التلقائي الشامل (ميديا + بصمات) ---
@hellas.on(events.NewMessage(incoming=True, func=lambda e: e.is_private))
async def auto_save_handler(event):
    if is_enabled():
        # دعم كامل: صور، فيديو، بصمات، ملفات صوتية
        if event.photo or event.video or event.voice or event.audio or event.media:
            try:
                media = await event.download_media()
                if media:
                    sender = await event.get_sender()
                    m_type = "بصمة صوتية 🎤" if event.voice else "ميديا 🖼"
                    date_str = event.date.strftime("%Y-%m-%d %I:%M %p")
                    
                    caption = f"**♡ تم حفظ {m_type} ✓**\n**♡ المرسل :** [{sender.first_name}](tg://user?id={event.sender_id})\n**♡ الوقت :** `{date_str}`"
                    
                    await hellas.send_file("me", media, caption=caption)
                    if os.path.exists(media):
                        os.remove(media)
            except Exception as e:
                print(f"Save Error: {str(e)}")

# --- الجلب اليدوي ---
@hellas.on(events.NewMessage(outgoing=True, pattern=r"^\.(جلب|ذاتية)$"))
async def manual_save(event):
    if not event.is_reply:
        return await event.edit("**᯽︙ رد على الميديا أولاً!**")
    
    reply_msg = await event.get_reply_message()
    await event.edit("**᯽︙ جاري الجلب...**")
    media = await reply_msg.download_media()
    if media:
        await hellas.send_file("me", media, caption="**᯽︙ تم جلب الميديا بنجاح ✓**")
        await event.delete()
        if os.path.exists(media): os.remove(media)
    else:
        await event.edit("**᯽︙ فشل الجلب!**")
