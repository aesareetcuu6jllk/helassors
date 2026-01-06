import __main__ as main_module
from telethon import events
import subprocess
import os
import tempfile
import json
import asyncio

# ربط محرك السورس
hellas = main_module.hellas

# دالة التحميل العامة باستخدام yt-dlp
async def download_and_send_file(event, url, platform):
    if not url or "http" not in url:
        return await event.edit("**᯽︙ يرجى وضع رابط صحيح أو الرد على رسالة تحتوي رابط!**")

    await event.edit(f"**᯽︙ جاري التحميل من {platform}... 📥**")

    try:
        with tempfile.TemporaryDirectory() as tmpdir:
            output_template = os.path.join(tmpdir, '%(title)s.%(ext)s')

            # جلب معلومات الملف أولاً
            info_command = ['yt-dlp', '--no-warnings', '--dump-json', url]
            process = await asyncio.create_subprocess_exec(
                *info_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE
            )
            stdout, stderr = await process.communicate()
            
            if process.returncode != 0:
                return await event.edit("**❌ فشل جلب معلومات الرابط، تأكد من صحته!**")

            video_info = json.loads(stdout.decode())
            title = video_info.get('title', 'بدون عنوان')

            # التحميل
            await event.edit(f"**᯽︙ جاري سحب الملف: ( {title[:30]}... )**")
            
            download_command = [
                'yt-dlp', '--no-warnings', '-f', 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
                '--output', output_template, url
            ]
            
            proc = await asyncio.create_subprocess_exec(*download_command, cwd=tmpdir)
            await proc.wait()

            # البحث عن الملف المحمل
            files = [os.path.join(tmpdir, f) for f in os.listdir(tmpdir)]
            if not files:
                return await event.edit("**❌ لم يتم العثور على ملفات صالحة للتحميل.**")

            file_path = files[0]
            await event.edit("**᯽︙ جاري الرفع إلى التليجرام... ⬆️**")

            # إرسال الملف (للمحادثة الحالية)
            caption = f"🎬 **تم التحميل بنجاح!**\n📝 **العنوان:** {title}\n📌 **الموقع:** {platform}\n**•───── HELLAS ─────•**"
            await hellas.send_file(event.chat_id, file_path, caption=caption)
            await event.delete()
            
    except Exception as e:
        await event.edit(f"**❌ حدث خطأ أثناء العملية:** `{str(e)[:100]}`")

# --- الأوامر ---

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^\.اوامر التنزيل$"))
async def dl_help(event):
    help_msg = (
        "**📥 أوامر تنزيل هيلاس المدعومة:**\n"
        "**•───── HELLAS ─────•**\n"
        "⥾ `.يوتيوب` + الرابط أو بالرد\n"
        "⥾ `.تيكتوك` + الرابط أو بالرد\n"
        "⥾ `.انستا` + الرابط أو بالرد\n"
        "⥾ `.فيس` + الرابط أو بالرد\n"
        "⥾ `.تويتر` + الرابط أو بالرد\n"
        "⥾ `.ساوند` + الرابط أو بالرد\n"
        "**•───── HELLAS ─────•**\n"
        "✨ **ملاحظة:** الأوامر تعمل بالرد على الرابط أيضاً."
    )
    await event.edit(help_msg)

# دالة ذكية لجلب الرابط سواء كان بجانب الأمر أو بالرد
async def get_url(event):
    link = event.pattern_match.group(1)
    if not link:
        reply = await event.get_reply_message()
        if reply: link = reply.text
    return link.strip() if link else None

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^\.تيكتوك(?:\s|$)([\s\S]*)"))
async def tk_dl(event):
    url = await get_url(event)
    await download_and_send_file(event, url, "TikTok")

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^\.يوتيوب(?:\s|$)([\s\S]*)"))
async def yt_dl(event):
    url = await get_url(event)
    await download_and_send_file(event, url, "YouTube")

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^\.انستا(?:\s|$)([\s\S]*)"))
async def ig_dl(event):
    url = await get_url(event)
    await download_and_send_file(event, url, "Instagram")

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^\.فيس(?:\s|$)([\s\S]*)"))
async def fb_dl(event):
    url = await get_url(event)
    await download_and_send_file(event, url, "Facebook")

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^\.تويتر(?:\s|$)([\s\S]*)"))
async def tw_dl(event):
    url = await get_url(event)
    await download_and_send_file(event, url, "Twitter")

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^\.ساوند(?:\s|$)([\s\S]*)"))
async def sc_dl(event):
    url = await get_url(event)
    await download_and_send_file(event, url, "SoundCloud")
