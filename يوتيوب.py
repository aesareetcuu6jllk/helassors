import __main__ as main_module
from telethon import events
import aiohttp

# ربط محرك السورس
hellas = main_module.hellas

# إعدادات API يوتيوب
YOUTUBE_API_KEY = 'AIzaSyBfb8a-Ug_YQFrpWKeTc88zuI6PmHVdzV0'
YOUTUBE_API_URL = 'https://www.googleapis.com/youtube/v3/search'

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^\.بحث يوتيوب (.+)"))
async def youtube_search(event):
    query = event.pattern_match.group(1)
    await event.edit(f"**᯽︙ جاري البحث عن: ( {query} ) ... 🔍**")
    
    async with aiohttp.ClientSession() as session:
        params = {
            'part': 'snippet',
            'q': query,
            'key': YOUTUBE_API_KEY,
            'type': 'video',
            'maxResults': 1
        }
        async with session.get(YOUTUBE_API_URL, params=params) as response:
            if response.status != 200:
                return await event.edit("**❌ فشل الاتصال بـ API يوتيوب، تأكد من مفتاح الـ API.**")
            
            data = await response.json()
            
            if 'items' in data and data['items']:
                video_id = data['items'][0]['id']['videoId']
                video_title = data['items'][0]['snippet']['title']
                video_url = f"https://www.youtube.com/watch?v={video_id}"
                
                msg = (
                    f"📹 **نتائج البحث من يوتيوب:**\n"
                    f"**•───── HELLAS ─────•**\n"
                    f"📝 **العنوان:** {video_title}\n"
                    f"🔗 **الرابط:** {video_url}\n"
                    f"**•───── HELLAS ─────•**"
                )
                await event.edit(msg, link_preview=True)
            else:
                await event.edit("**⎙ لم يتم العثور على نتائج تتطابق مع بحثك.**")

