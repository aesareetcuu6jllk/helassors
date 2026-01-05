hereimport __main__ as main_module
import urllib.request
import re
import os
from telethon import events

# ربط المحرك الأساسي
hellas = main_module.hellas

@hellas.on(events.NewMessage(outgoing=True, pattern=r'^\.حساب تيك (.+)'))
async def tiktok_scraper(event):
    user = event.pattern_match.group(1).replace('@', '')
    url = f'https://www.tiktok.com/@{user}'
    
    await event.edit(f"**᯽︙ جاري جلب معلومات الحساب: `@{user}` ...**")
    
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
    
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req) as response:
            content = response.read().decode('utf-8')
        
        # استخراج البيانات باستخدام Regex (مطوّر قليلاً)
        user_id = re.search(r'"id":"(\d+)"', content)
        nickname = re.search(r'"nickname":"([^"]+)"', content)
        follower_count = re.search(r'"followerCount":(\d+)', content)
        following_count = re.search(r'"followingCount":(\d+)', content)
        bio = re.search(r'"signature":"([^"]+)"', content)
        video_count = re.search(r'"videoCount":(\d+)', content)
        avatar_url = re.search(r'"avatarLarger":"([^"]+)"', content)
        
        # التحقق من وجود البيانات
        u_id = user_id.group(1) if user_id else 'غير متاح'
        u_nick = nickname.group(1) if nickname else user
        u_followers = follower_count.group(1) if follower_count else '0'
        u_following = following_count.group(1) if following_count else '0'
        u_bio = bio.group(1) if bio else 'لا يوجد بايو'
        u_videos = video_count.group(1) if video_count else '0'
        
        # تحضير الرد
        response_msg = f"""**᯽︙ معلومات حساب تيك توك :**
        
🏷 **الأسـم :** `{u_nick}`
🆔 **الآيـدي :** `{u_id}`
👥 **المتابِـعين :** `{u_followers}`
🔄 **يتابعهم :** `{u_following}`
🎬 **الفيديوهات :** `{u_videos}`
📝 **البايو :** `{u_bio}`

**᯽︙ بواسطـة سـورس هـيلاس ⚡️**"""

        # تحميل وإرسال الصورة الشخصية إذا وجدت
        if avatar_url:
            img_url = avatar_url.group(1).replace(r'\u002F', '/')
            avatar_filename = f'tiktok_{user}.jpg'
            urllib.request.urlretrieve(img_url, avatar_filename)
            await hellas.send_file(event.chat_id, avatar_filename, caption=response_msg)
            os.remove(avatar_filename) # حذف الصورة بعد الإرسال
            await event.delete()
        else:
            await event.edit(response_msg)

    except Exception as e:
        await event.edit(f"**❌ فشل جلب الحساب، قد يكون الحساب خاص أو غير موجود.**")

