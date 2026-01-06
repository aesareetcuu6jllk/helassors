import __main__ as main_module
from telethon import events
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.tl.functions.messages import DeleteHistoryRequest
import asyncio
import re

# ربط محرك السورس
hellas = main_module.hellas

@hellas.on(events.NewMessage(outgoing=True, pattern=r'^\.يوت (.+)'))
async def youtube_audio_dl(event):
    query = event.pattern_match.group(1).strip()
    
    if query.startswith("."):
        query = query[1:].strip()
        
    search_query = "يوت " + query
    await event.edit(f"**᯽︙ جاري جلب المقطع الصوتي... 🎧**")
    
    try:
        async with hellas.conversation('@ALMAS_bbot', timeout=30) as conv:
            # إرسال الطلب
            await conv.send_message(search_query)
            
            # انتظار رد البوت
            response = await conv.get_response()
            
            # التحقق من الاشتراك الإجباري
            if "عليك الأشتراك" in response.message:
                channel = re.search(r"(@\w+)", response.message)
                if channel:
                    await hellas(JoinChannelRequest(channel.group(1)))
                    await conv.send_message(search_query)
                    response = await conv.get_response()

            # التأكد أن الرد يحتوي على صوت
            if response.audio or response.voice:
                # إرسال الملف الصوتي بدون أي وصف (caption)
                await hellas.send_file(
                    event.chat_id, 
                    response.media, 
                    reply_to=event.reply_to_msg_id
                )
                await event.delete()
            else:
                # محاولة ثانية في حال تأخر البوت
                response = await conv.get_response()
                if response.audio or response.voice:
                    await hellas.send_file(event.chat_id, response.media)
                    await event.delete()
                else:
                    await event.edit("**❌ لم يتم العثور على صوت.**")

            # تنظيف المحادثة مع البوت المساعد نهائياً
            await hellas(DeleteHistoryRequest(peer='@ALMAS_bbot', max_id=0, just_clear=False, revoke=True))

    except Exception as e:
        await event.edit(f"**❌ البوت المساعد لا يستجيب حالياً.**")

