import __main__ as main_module
from telethon import events
from telethon.tl.types import DocumentAttributeVideo
import os

# ربط محرك السورس
hellas = main_module.hellas

@hellas.on(events.NewMessage(pattern=r'^\.(حفظ|احفظ) (https?://[^\s]+)$', outgoing=True))
async def save_from_link(event):
    link = event.pattern_match.group(2)
    await event.edit("**᯽︙ جاري سحب المحتوى من الرابط... 📥**")

    try:
        # تحليل الرابط
        if "/c/" in link:
            # قناة خاصة
            parts = link.split("/")
            chat_id = int("-100" + parts[-2])
            msg_id = int(parts[-1].split("?")[0])
        else:
            # قناة عامة
            parts = link.split("/")
            chat_id = parts[-2]
            msg_id = int(parts[-1].split("?")[0])

        # استخدام الطريقة المختصرة والأضمن في Telethon
        messages = await hellas.get_messages(chat_id, ids=msg_id)
        
        if not messages:
            return await event.edit("**❌ فشل جلب الرسالة، تأكد من وجودك في القناة.**")
        
        msg = messages

        if msg.media:
            # تحميل الميديا
            file_path = await hellas.download_media(msg)
            
            kwargs = {
                "file": file_path,
                "caption": msg.text or "",
            }

            # دعم تشغيل الفيديو أثناء التحميل
            if hasattr(msg, "document") and msg.document:
                for attr in msg.document.attributes:
                    if isinstance(attr, DocumentAttributeVideo):
                        kwargs["supports_streaming"] = True

            await hellas.send_file(event.chat_id, **kwargs)
            
            if os.path.exists(file_path):
                os.remove(file_path)
            await event.delete()
        
        elif msg.text:
            # إذا كان نص فقط
            await event.edit(msg.text)
        else:
            await event.edit("**❌ نوع الرسالة غير مدعوم.**")

    except Exception as e:
        await event.edit(f"**❌ حدث خطأ أثناء الحفظ:**\n`{str(e)}`")
