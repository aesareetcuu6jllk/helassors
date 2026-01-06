import __main__ as main_module
from telethon import events
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.tl.functions.messages import DeleteHistoryRequest
from telethon.errors import MessageIdInvalidError
import asyncio
import re

# ربط محرك السورس
hellas = main_module.hellas

@hellas.on(events.NewMessage(outgoing=True, pattern=r'^\.يوت (.+)'))
async def youtube_audio_dl(event):
    chat = await event.get_chat()
    query = event.pattern_match.group(1).strip()
    
    # تنظيف النص إذا بدأ بنقطة
    if query.startswith("."):
        query = query[1:].strip()
        
    search_query = "يوت " + query
    await event.edit(f"**᯽︙ جاري طلب ( {query} ) من اليوتيوب... 🎧**")
    
    try:
        # بدء المحادثة مع البوت المساعد
        async with hellas.conversation('@ALMAS_bbot') as conv:
            # إرسال طلب البحث
            x = await hellas.send_message('@ALMAS_bbot', search_query)
            
            audio_clip = None
            timeout = 30  # زيادة وقت الانتظار قليلاً لضمان الاستجابة
            start_time = asyncio.get_event_loop().time()
            
            while asyncio.get_event_loop().time() - start_time < timeout:
                # انتظار الرد
                response = await conv.get_response()
                await hellas.send_read_acknowledge(conv.chat_id)
                
                # التعامل مع الاشتراك الإجباري
                if "عليك الأشتراك في قناة البوت" in response.message:
                    try:
                        channel_match = re.search(r"(@\w+)", response.message)
                        if channel_match:
                            channel_name = channel_match.group(1)
                            await hellas(JoinChannelRequest(channel_name))
                            # إعادة إرسال الطلب بعد الاشتراك
                            x = await hellas.send_message('@ALMAS_bbot', search_query)
                            continue
                    except Exception as e:
                        print(f"Error joining channel: {e}")
                
                # التحقق إذا كان الرد يحتوي على ملف صوتي
                if response.audio or response.voice:
                    audio_clip = response
                    break
                
                # إذا أرسل البوت رسالة "لم يتم العثور"
                if "لم يتم العثور" in response.message or "لا يوجد" in response.message:
                    break

            if audio_clip:
                # إرسال الملف الصوتي للمحادثة الأصلية
                await hellas.send_file(
                    event.chat_id, 
                    audio_clip.media, 
                    caption=f"🎧 **تم تحميل طلبك بنجاح**\n**•───── HELLAS ─────•**",
                    reply_to=event.reply_to_msg_id
                )
                await event.delete()
                
                # تنظيف المحادثة مع البوت المساعد
                try:
                    await hellas(DeleteHistoryRequest(peer='@ALMAS_bbot', max_id=0, just_clear=False, revoke=True))
                except Exception:
                    pass
            else:
                await event.edit("**❌ عذراً، لم يتم العثور على المقطع المطلوب أو البوت المساعد لا يستجيب.**")
                
    except Exception as e:
        print(f"Error in YouTube Audio: {e}")
        await event.edit(f"**❌ حدث خطأ في العملية:** `{str(e)[:50]}`")

