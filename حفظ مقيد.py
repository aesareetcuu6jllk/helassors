import __main__ as main_module
from telethon import events
from telethon.tl.functions.messages import GetMessagesRequest
from telethon.tl.types import DocumentAttributeVideo
import os

# ربط محرك السورس
hellas = main_module.hellas

@hellas.on(events.NewMessage(pattern=r'^\.(حفظ|احفظ) (https?://[^\s]+)$', outgoing=True))
async def save_from_link(event):
    link = event.pattern_match.group(2)
    await event.edit("**᯽︙ جاري سحب المحتوى من الرابط... 📥**")

    try:
        # تحليل الرابط (قناة خاصة أو عامة)
        if "/c/" in link:
            # روابط القنوات الخاصة
            parts = link.split("/")
            chat_id = int("-100" + parts[-2])
            msg_id = int(parts[-1].split("?")[0])
        else:
            # روابط القنوات العامة
            parts = link.split("/")
            username = parts[-2]
            msg_id = int(parts[-1].split("?")[0])
            entity = await hellas.get_entity(username)
            chat_id = entity.id

        # جلب الرسالة المطلوبة
        res = await hellas(GetMessagesRequest(chat_id, [msg_id]))
        if not res.messages or res.messages[0].id == 0:
            return await event.edit("**❌ لم يتم العثور على الرسالة أو الرابط غير صحيح.**")
        
        msg = res.messages[0]

        if msg.media:
            # تحميل الميديا (صورة، فيديو، الخ)
            file_path = await hellas.download_media(msg)
            
            kwargs = {
                "file": file_path,
                "caption": msg.text or "",
            }

            # دعم تشغيل الفيديو أثناء التحميل (Streaming)
            if hasattr(msg.media, "document") and msg.media.document:
                for attr in msg.media.document.attributes:
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
            await event.edit("**❌ هذا النوع من الرسائل غير مدعوم.**")

    except Exception as e:
        await event.edit(f"**❌ حدث خطأ أثناء الحفظ:**\n`{str(e)[:150]}`")
