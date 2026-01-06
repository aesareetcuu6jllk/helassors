import __main__ as main_module
from datetime import datetime
from math import sqrt
import asyncio
from telethon import events
from telethon.errors import (
    ChannelInvalidError,
    ChannelPrivateError,
    ChannelPublicGroupNaError,
)
from telethon.tl.functions.channels import GetFullChannelRequest, GetParticipantsRequest
from telethon.tl.functions.messages import GetFullChatRequest, GetHistoryRequest
from telethon.tl.types import (
    ChannelParticipantAdmin,
    ChannelParticipantCreator,
    ChannelParticipantsAdmins,
    ChannelParticipantsBots,
    MessageActionChannelMigrateFrom,
)
from telethon.utils import get_input_location

# ربط محرك سورس هيلاس الأساسي
hellas = main_module.hellas

# ========================================================
# 1. أمر عرض المشرفين (مع التاك والدور)
# ========================================================
@hellas.on(events.NewMessage(pattern=r"^\.المشرفين(?: |$)(.*)", outgoing=True))
async def get_admins(event):
    input_str = event.pattern_match.group(1)
    mentions = "**᯽︙ مشرفين هذه المجموعة ✪**:\n"
    
    if input_str:
        try:
            chat = await event.client.get_entity(input_str)
            mentions = f"**⌔︙مشرفين الدردشة : {chat.title}**\n"
        except Exception as e:
            return await event.edit(f"❌ **الخطأ:** `{str(e)}`")
    else:
        chat = await event.get_chat()
        if not event.is_group:
            return await event.edit("**❌ هذا الأمر يعمل في المجموعات فقط!**")

    msg = await event.edit("⏳ **جاري جلب قائمة المشرفين...**")
    try:
        async for x in event.client.iter_participants(chat, filter=ChannelParticipantsAdmins):
            if not x.deleted:
                role = "المالك 👑" if isinstance(x.participant, ChannelParticipantCreator) else "مشرف 👮"
                mentions += f"\n- [{x.first_name}](tg://user?id={x.id}) | `{x.id}`\n  **الدور:** {role}\n"
            else:
                mentions += f"\n- `حساب محذوف` | `{x.id}`\n"
        await msg.edit(mentions)
    except Exception as e:
        await msg.edit(f"❌ **حدث خطأ:** `{str(e)}`")

# ========================================================
# 2. أمر عرض البوتات الموجودة بالمجموعة
# ========================================================
@hellas.on(events.NewMessage(pattern=r"^\.البوتات(?: |$)(.*)", outgoing=True))
async def get_bots(event):
    input_str = event.pattern_match.group(1)
    mentions = "**᯽︙ البوتات في هذه المجموعة 🝰**:\n"
    
    if input_str:
        try:
            chat = await event.client.get_entity(input_str)
        except Exception as e:
            return await event.edit(f"❌ **الخطأ:** `{str(e)}`")
    else:
        chat = await event.get_chat()

    msg = await event.edit("⏳ **جاري البحث عن البوتات...**")
    try:
        async for x in event.client.iter_participants(chat, filter=ChannelParticipantsBots):
            mentions += f"\n- [{x.first_name}](tg://user?id={x.id}) | `{x.id}`"
        await msg.edit(mentions)
    except Exception as e:
        await msg.edit(f"❌ **حدث خطأ:** `{str(e)}`")

# ========================================================
# 3. أمر عرض الأعضاء (مع جرد سريع)
# ========================================================
@hellas.on(events.NewMessage(pattern=r"^\.الاعضاء(?: |$)(.*)", outgoing=True))
async def get_users(event):
    input_str = event.pattern_match.group(1)
    if input_str:
        try:
            chat = await event.client.get_entity(input_str)
        except Exception as e:
            return await event.edit(f"❌ **الخطأ:** `{str(e)}`")
    else:
        if not event.is_group:
            return await event.edit("**❌ هذا ليس كروب!**")
        chat = await event.get_chat()

    msg = await event.edit("**🔄 جاري جلب قائمة الأعضاء (أول 100)...**")
    mentions = f"**👥 أعضاء مجموعة: {chat.title}**\n"
    
    try:
        count = 0
        async for user in event.client.iter_participants(chat):
            if count >= 100: # لمنع الحظر والتعليق
                mentions += "\n\n⚠️ **ملاحظة:** تم عرض أول 100 عضو فقط."
                break
            if user.deleted:
                mentions += f"\n- `حساب محذوف` | `{user.id}`"
            else:
                mentions += f"\n- [{user.first_name}](tg://user?id={user.id}) | `{user.id}`"
            count += 1
        await msg.edit(mentions)
    except Exception as e:
        await msg.edit(f"❌ **خطأ:** `{str(e)}`")

# ========================================================
# 4. أمر معلومات المجموعة الشامل
# ========================================================
@hellas.on(events.NewMessage(pattern=r"^\.معلومات(?: |$)(.*)", outgoing=True))
async def info(event):
    input_chat = event.pattern_match.group(1) or event.chat_id
    msg = await event.edit("⏳ **جاري تحليل معلومات الدردشة...**")
    
    try:
        # جلب البيانات الكاملة من التلغرام
        full_chat = await event.client(GetFullChannelRequest(input_chat))
        chat_obj = await event.client.get_entity(input_chat)
        
        caption = f"<b>📊 معلومات المجموعة / القناة:</b>\n\n"
        caption += f"• <b>الاسم:</b> {chat_obj.title}\n"
        caption += f"• <b>الآيدي:</b> <code>{chat_obj.id}</code>\n"
        caption += f"• <b>التاريخ:</b> <code>{chat_obj.date.strftime('%Y-%m-%d')}</code>\n"
        caption += f"• <b>الأعضاء:</b> <code>{full_chat.full_chat.participants_count}</code>\n"
        caption += f"• <b>المشرفين:</b> <code>{full_chat.full_chat.admins_count or '0'}</code>\n"
        caption += f"• <b>المحظورين:</b> <code>{full_chat.full_chat.kicked_count or '0'}</code>\n"
        
        if chat_obj.username:
            caption += f"• <b>اليوزر:</b> @{chat_obj.username}\n"
        else:
            caption += f"• <b>النوع:</b> دردشة خاصة 🔒\n"
            
        if full_chat.full_chat.about:
            caption += f"\n📝 <b>الوصف:</b>\n<code>{full_chat.full_chat.about}</code>"

        await msg.edit(caption, parse_mode="html")
    except Exception as e:
        await msg.edit(f"❌ **فشل جلب المعلومات:** `{str(e)}`")
