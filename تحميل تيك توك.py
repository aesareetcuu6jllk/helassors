import __main__ as main_module
from telethon import events
import yt_dlp
import os
import tempfile
import asyncio
import json

# ربط محرك السورس
hellas = main_module.hellas

# دالة التحميل الاحترافية باستخدام المكتبة مباشرة
async def download_and_send_file(event, url, platform):
    if not url or "http" not in url:
        return await event.edit("**᯽︙ يرجى وضع رابط صحيح أو الرد على رسالة تحتوي رابط!**")

    await event.edit(f"**᯽︙ جاري التحميل من {platform}... 📥**")

    try:
        with tempfile.TemporaryDirectory() as tmpdir:
            # إعدادات التحميل
            ydl_opts = {
                'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
                'outtmpl': os.path.join(tmpdir, '%(title)s.%(ext)s'),
                'quiet': True,
                'no_warnings': True,
                'nocheckcertificate': True,
            }

            # تشغيل التحميل في Loop لعدم تعليق السورس
            def run_dl():
                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    info = ydl.extract_info(url, download=True)
                    return ydl.prepare_filename(info), info.get('title', 'بدون عنوان')

            loop = asyncio.get_event_loop()
            file_path, title = await loop.run_in_executor(None, run_dl)

            if not os.path.exists(file_path):
                return await event.edit("**❌ فشل العثور على الملف بعد التحميل.**")

            await event.edit("**᯽︙ جاري الرفع إلى التليجرام... ⬆️**")

            # إرسال الملف
            caption = (
                f"🎬 **تم التحميل بنجاح!**\n"
                f"📝 **العنوان:** {title}\n"
                f"📌 **الموقع:** {platform}\n"
                f"**•───── HELLAS ─────•**"
            )
            
            await hellas.send_file(event.chat_id, file_path, caption=caption)
            await event.delete()
            
    except Exception as e:
        error_msg = str(e)[:150]
        await event.edit(f"**❌ حدث خطأ أثناء العملية:**\n`{error_msg}`")

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

async def get_url(event):
    # محاولة جلب الرابط من نص الأمر
    link = event.pattern_match.group(1)
    # إذا لم يوجد، نحاول جلب الرابط من الرسالة المردود عليها
    if not link:
        reply = await event.get_reply_message()
        if reply:
            link = reply.text
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
