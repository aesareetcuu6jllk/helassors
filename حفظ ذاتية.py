import __main__ as main_module
import os
import re
from telethon import events

# ربط المحركات الأساسية لسورسك
hellas = main_module.hellas
tg_bot = main_module.tg_bot

# استيراد نظام التخزين الدائم (SQL)
try:
    from JoKeRUB.sql_helper.globals import addgvar, delgvar, gvarstatus
except:
    try:
        from sql_helper.globals import addgvar, delgvar, gvarstatus
    except:
        # تعريف يدوي في حال لم يجد الملف لضمان عدم توقف السورس
        def addgvar(k, v): pass
        def delgvar(k): pass
        def gvarstatus(k): return None

# --- أمر التفعيل الدائم ---
@hellas.on(events.NewMessage(outgoing=True, pattern=r"^\.(الذاتية تشغيل|ذاتية تشغيل)$"))
async def turn_on(event):
    # إضافة القيمة لقاعدة البيانات
    addgvar("save_self_media", "true")
    await event.edit("**᯽︙ تم تفعيل حفظ الذاتيات بنجاح ✓**\n**᯽︙ ستبقى الميزة تعمل دائماً حتى بعد التحديث.**")

# --- أمر التعطيل ---
@hellas.on(events.NewMessage(outgoing=True, pattern=r"^\.(الذاتية تعطيل|ذاتية تعطيل)$"))
async def turn_off(event):
    # حذف القيمة من قاعدة البيانات
    delgvar("save_self_media")
    await event.edit("**᯽︙ تم تعطيل حفظ الذاتيات بنجاح ✓**")

# --- محرك الحفظ التلقائي (يفحص الحالة من القاعدة) ---
@hellas.on(events.NewMessage(func=lambda e: e.is_private))
async def auto_save_handler(event):
    # فحص هل الميزة مفعلة في قاعدة البيانات؟
    if gvarstatus("save_self_media"):
        # التأكد من أنها ميديا ذاتية (لم تُفتح بعد) ومن شخص آخر
        if event.media and event.media_unread:
            me = await hellas.get_me()
            if event.sender_id == me.id:
                return
            
            try:
                # تحميل وحفظ
                media = await event.download_media()
                if media:
                    sender = await event.get_sender()
                    caption = f"**᯽︙ تم حفظ ذاتية تلقائياً ✓**\n**᯽︙ المرسل :** [{sender.first_name}](tg://user?id={event.sender_id})"
                    await hellas.send_file("me", media, caption=caption)
                    if os.path.exists(media):
                        os.remove(media)
            except Exception as e:
                print(f"Error in saving self media: {e}")

# --- أمر جلب يدوي (بالرد) ---
@hellas.on(events.NewMessage(outgoing=True, pattern=r"^\.(جلب الصورة|جلب الصوره|ذاتيه|ذاتية)$"))
async def manual_save(event):
    if not event.is_reply:
        return await event.edit("**᯽︙ رد على الميديا الذاتية أولاً!**")
    
    reply_msg = await event.get_reply_message()
    if not reply_msg.media:
        return await event.edit("**᯽︙ هذا ليس ملف وسائط!**")

    await event.edit("**᯽︙ جاري الجلب...**")
    media = await reply_msg.download_media()
    if media:
        await hellas.send_file("me", media, caption="**᯽︙ تم جلب الميديا بنجاح ✓**")
        await event.delete()
        if os.path.exists(media):
            os.remove(media)
    else:
        await event.edit("**᯽︙ فشل! الميديا قد تكون منتهية الصلاحية.**")
