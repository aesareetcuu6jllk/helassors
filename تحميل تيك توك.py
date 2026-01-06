import __main__ as main_module
from telethon import events
import requests
import os
import tempfile
import time

# ربط المحرك (هيلاس)
hellas = main_module.hellas

def download_tiktok(url):
    """وظيفة جلب الفيديو بدون علامة مائية"""
    try:
        api_url = f"https://www.tikwm.com/api/?url={url}"
        response = requests.get(api_url).json()
        if response.get("code") == 0:
            video_url = "https://www.tikwm.com" + response["data"]["play"]
            res = requests.get(video_url, stream=True)
            temp_file = os.path.join(tempfile.gettempdir(), f"tk_{int(time.time())}.mp4")
            with open(temp_file, 'wb') as f:
                for chunk in res.iter_content(chunk_size=8192):
                    f.write(chunk)
            return temp_file, response["data"].get("title", "بدون عنوان")
    except:
        return None, None
    return None, None

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^\.تحميل تيك(?:\s|$)([\s\S]*)"))
async def tiktok_downloader(event):
    link = event.pattern_match.group(1).strip()
    reply = await event.get_reply_message()
    
    # التحقق إذا كان الرابط في الرسالة أو بالرد
    if not link and reply:
        link = reply.text
    
    if not link or "tiktok.com" not in link:
        return await event.edit("**᯽︙ يرجى وضع رابط تيك توك أو الرد على رابط!**")

    await event.edit("**᯽︙ جاري جلب الفيديو من تيك توك... 📥**")
    
    path, title = download_tiktok(link)
    
    if path:
        try:
            await event.client.send_file(
                event.chat_id, 
                path, 
                caption=f"🎬 **تم تحميل الفيديو بنجاح!**\n📝 **العنوان:** {title}\n**•───── HELLAS ─────•**",
                reply_to=reply.id if reply else None
            )
            await event.delete()
        except Exception as e:
            await event.edit(f"**❌ فشل إرسال الملف:** `{str(e)}`")
        finally:
            if os.path.exists(path):
                os.remove(path)
    else:
        await event.edit("**❌ فشل تحميل الفيديو، تأكد من صحة الرابط أو أن الحساب ليس خاصاً.**")
