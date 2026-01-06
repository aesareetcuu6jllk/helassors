import __main__ as main_module
from telethon import events, errors
from telethon.tl.functions.channels import EditAdminRequest, EditBannedRequest, EditPhotoRequest
from telethon.tl.functions.messages import UpdatePinnedMessageRequest
from telethon.tl.types import ChatAdminRights, ChatBannedRights, InputChatPhotoEmpty, MessageMediaPhoto
import os
import asyncio

# ربط محرك سورس هيلاس
hellas = main_module.hellas

# إعدادات الحقوق (الحظر والكتم)
BANNED_RIGHTS = ChatBannedRights(
    until_date=None, view_messages=True, send_messages=True, send_media=True,
    send_stickers=True, send_gifs=True, send_games=True, send_inline=True, embed_links=True,
)
UNBAN_RIGHTS = ChatBannedRights(
    until_date=None, send_messages=None, send_media=None, send_stickers=None,
    send_gifs=None, send_games=None, send_inline=None, embed_links=None,
)
MUTE_RIGHTS = ChatBannedRights(until_date=None, send_messages=True)
UNMUTE_RIGHTS = ChatBannedRights(until_date=None, send_messages=False)

# --- 1. أوامر الصورة ---
@hellas.on(events.NewMessage(pattern=r"^\.الصورة\s+(-وضع|-حذف)$", outgoing=True))
async def group_photo(event):
    cmd = event.pattern_match.group(1)
    if cmd == "-وضع":
        if not event.is_reply: return await event.edit("❌ **رد على صورة أولاً!**")
        reply = await event.get_reply_message()
        if reply.photo:
            msg = await event.edit("⏳ **جاري تغيير صورة المجموعة...**")
            photo = await event.client.download_media(reply.photo)
            try:
                await event.client(EditPhotoRequest(event.chat_id, await event.client.upload_file(photo)))
                await msg.edit("✅ **تم تغيير صورة المجموعة بنجاح!**")
            except Exception as e: await msg.edit(f"❌ **خطأ:** `{str(e)}`")
            finally: os.remove(photo)
        else: await event.edit("❌ **عذراً، هذا الملف ليس صورة!**")
    else:
        try:
            await event.client(EditPhotoRequest(event.chat_id, InputChatPhotoEmpty()))
            await event.edit("✅ **تم حذف صورة المجموعة بنجاح.**")
        except Exception as e: await event.edit(f"❌ **خطأ:** `{str(e)}`")

# --- 2. الرفع والتنزيل ---
@hellas.on(events.NewMessage(pattern=r"^\.رفع مشرف$", outgoing=True))
async def promote(event):
    if not event.is_reply: return await event.edit("❌ **رد على المستخدم لرفعه!**")
    reply = await event.get_reply_message()
    new_rights = ChatAdminRights(
        add_admins=False, invite_users=True, change_info=True,
        ban_users=True, delete_messages=True, pin_messages=True,
    )
    try:
        await event.client(EditAdminRequest(event.chat_id, reply.sender_id, new_rights, "Admin"))
        await event.edit(f"✅ **تم رفع المستخدوم بنجاح!**")
    except Exception as e: await event.edit("❌ **ليس لدي صلاحيات كافية لرفع مشرف!**")

@hellas.on(events.NewMessage(pattern=r"^\.تنزيل الكل$", outgoing=True))
async def demote(event):
    if not event.is_reply: return await event.edit("❌ **رد على المستخدم لتنزيله!**")
    reply = await event.get_reply_message()
    try:
        await event.client(EditAdminRequest(event.chat_id, reply.sender_id, ChatAdminRights(
            add_admins=None, invite_users=None, change_info=None,
            ban_users=None, delete_messages=None, pin_messages=None,
        ), "Admin"))
        await event.edit(f"✅ **تم تنزيل المستخدم من الإشراف.**")
    except Exception as e: await event.edit(f"❌ **خطأ:** `{str(e)}`")

# --- 3. الحظر والطرد والكتم ---
@hellas.on(events.NewMessage(pattern=r"^\.حظر$", outgoing=True))
async def ban_user(event):
    if not event.is_reply: return await event.edit("❌ **رد على المستخدم لحظره!**")
    reply = await event.get_reply_message()
    try:
        await event.client(EditBannedRequest(event.chat_id, reply.sender_id, BANNED_RIGHTS))
        await event.edit(f"🚫 **تم حظر المستخدم بنجاح.**")
    except Exception as e: await event.edit("❌ **صلاحياتي لا تسمح بالحظر!**")

@hellas.on(events.NewMessage(pattern=r"^\.الغاء حظر$", outgoing=True))
async def unban_user(event):
    if not event.is_reply: return await event.edit("❌ **رد على المستخدم لرفع الحظر!**")
    reply = await event.get_reply_message()
    try:
        await event.client(EditBannedRequest(event.chat_id, reply.sender_id, UNBAN_RIGHTS))
        await event.edit(f"✅ **تم الغاء حظر المستخدم.**")
    except Exception as e: await event.edit(f"❌ **خطأ:** `{str(e)}`")

@hellas.on(events.NewMessage(pattern=r"^\.طرد$", outgoing=True))
async def kick_user(event):
    if not event.is_reply: return await event.edit("❌ **رد على المستخدم لطرده!**")
    reply = await event.get_reply_message()
    try:
        await event.client.kick_participant(event.chat_id, reply.sender_id)
        await event.edit(f"👞 **تم طرد المستخدم بنجاح.**")
    except Exception as e: await event.edit("❌ **لا أملك صلاحية الطرد!**")

@hellas.on(events.NewMessage(pattern=r"^\.كتم$", outgoing=True))
async def mute_user(event):
    if not event.is_reply: return await event.edit("❌ **رد على المستخدم لكتمه!**")
    reply = await event.get_reply_message()
    try:
        await event.client(EditBannedRequest(event.chat_id, reply.sender_id, MUTE_RIGHTS))
        await event.edit(f"🔇 **تم كتم المستخدم في هذه المجموعة.**")
    except Exception as e: await event.edit("❌ **صلاحياتي لا تسمح بالكتم!**")

@hellas.on(events.NewMessage(pattern=r"^\.الغاء كتم$", outgoing=True))
async def unmute_user(event):
    if not event.is_reply: return await event.edit("❌ **رد على المستخدم لرفع الكتم!**")
    reply = await event.get_reply_message()
    try:
        await event.client(EditBannedRequest(event.chat_id, reply.sender_id, UNMUTE_RIGHTS))
        await event.edit(f"🔊 **تم رفع الكتم عن المستخدم.**")
    except Exception as e: await event.edit(f"❌ **خطأ:** `{str(e)}`")

# --- 4. أوامر إضافية (تثبيت وحذف) ---
@hellas.on(events.NewMessage(pattern=r"^\.تثبيت$", outgoing=True))
async def pin_msg(event):
    if not event.is_reply: return await event.edit("❌ **رد على الرسالة لتثبيتها!**")
    reply = await event.get_reply_message()
    try:
        await event.client(UpdatePinnedMessageRequest(event.chat_id, reply.id))
        await event.edit("📌 **تم تثبيت الرسالة بنجاح.**")
    except Exception as e: await event.edit("❌ **فشل التثبيت!**")

@hellas.on(events.NewMessage(pattern=r"^\.حذف$", outgoing=True))
async def delete_msg(event):
    if not event.is_reply: return await event.edit("❌ **رد على الرسالة لحذفها!**")
    reply = await event.get_reply_message()
    try:
        await reply.delete()
        await event.delete()
    except Exception: pass

# --- قائمة أوامر الإدارة ---
@hellas.on(events.NewMessage(pattern=r"^\.اوامر الادارة$", outgoing=True))
async def admin_help(event):
    await event.edit(
        "👮‍♂️ **قائمة أوامر الإدارة - سورس هيلاس:**\n\n"
        "• `.رفع مشرف` | `.تنزيل الكل`\n"
        "• `.حظر` | `.الغاء حظر` | `.طرد`\n"
        "• `.كتم` | `.الغاء كتم`\n"
        "• `.تثبيت` | `.حذف`\n"
        "• `.الصورة -وضع` | `.الصورة -حذف`\n\n"
        "📌 **ملاحظة:** جميع الأوامر تعمل بالرد على الشخص أو الرسالة."
    )
