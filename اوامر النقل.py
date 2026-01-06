import __main__ as main_module
from telethon import events, errors
from telethon.tl.functions.channels import InviteToChannelRequest, GetFullChannelRequest, GetParticipantsRequest
from telethon.tl.functions.messages import ImportChatInviteRequest
from telethon.tl.types import ChannelParticipantsSearch
import os
import asyncio

# ربط محرك سورس هيلاس
hellas = main_module.hellas

active_task = None
stop_requested = False

# --- وظيفة سحب الأعضاء ---
async def fetch_users(group_link, event):
    global active_task, stop_requested
    users_set = set()
    file_path = f"users_{int(asyncio.get_event_loop().time())}.txt"
    stop_requested = False

    try:
        group = await hellas.get_entity(group_link)
        full_chat = await hellas(GetFullChannelRequest(group))
        total_count = full_chat.full_chat.participants_count

        msg = await event.edit(f"🔄 جاري سحب أعضاء: **{group.title}**\n👥 العدد الكلي: `{total_count}`\n⏳ يرجى الانتظار...")
        
        offset = 0
        limit = 100
        while True:
            if stop_requested: 
                await event.respond("🛑 تم إيقاف السحب بناءً على طلبك.")
                break
                
            participants = await hellas(GetParticipantsRequest(
                channel=group, filter=ChannelParticipantsSearch(''),
                offset=offset, limit=limit, hash=0
            ))
            
            if not participants or not participants.users: break

            with open(file_path, 'a', encoding='utf-8') as f:
                for user in participants.users:
                    if user.username and user.username not in users_set:
                        users_set.add(user.username)
                        f.write(f"{user.username}\n")
            
            offset += len(participants.users)
            await msg.edit(f"🔄 جاري السحب...\n✅ تم سحب: `{len(users_set)}` من `{total_count}`")
            
            if len(participants.users) < limit: break

        await msg.edit(f"✅ اكتملت العملية!\n📦 العدد النهائي المستخرج: `{len(users_set)}`")
        if len(users_set) > 0:
            await hellas.send_file('me', file_path, caption=f"📄 قائمة أعضاء: {group.title}\n✅ العدد: {len(users_set)}")
        
        if os.path.exists(file_path): os.remove(file_path)

    except Exception as e: 
        await event.reply(f"❌ حدث خطأ أثناء السحب: {e}")
    finally: 
        active_task = None
        stop_requested = False

# --- أمر السحب ---
@hellas.on(events.NewMessage(pattern=r'^\.سحب\s+(.+)$', outgoing=True))
async def start_fetch(event):
    global active_task
    if active_task: return await event.edit("⚠️ هناك عملية سحب جارية بالفعل!")
    gp = event.pattern_match.group(1)
    active_task = asyncio.create_task(fetch_users(gp, event))

# --- أمر إيقاف السحب (المعدل) ---
@hellas.on(events.NewMessage(pattern=r'^\.ايقاف السحب$', outgoing=True))
async def stop_fetch(event):
    global stop_requested
    if active_task:
        stop_requested = True
        await event.edit("🛑 **جاري إيقاف عملية السحب وحفظ البيانات...**")
    else:
        await event.edit("⚠️ **لا توجد عملية سحب جارية حالياً.**")

# --- أمر النقل (الإضافة) ---
@hellas.on(events.NewMessage(pattern=r'^\.نقل\s+(.+)$', outgoing=True))
async def add_users_handler(event):
    if not event.is_reply: return await event.edit("❌ رد على ملف اليوزرات أولاً!")
    
    reply_msg = await event.get_reply_message()
    if not reply_msg.document: return await event.edit("❌ الرد يجب أن يكون على ملف نصي!")

    group_link = event.pattern_match.group(1)
    file_path = await reply_msg.download_media()
    msg = await event.edit("⏳ جاري تهيئة عملية النقل...")

    try:
        target = await hellas.get_entity(group_link)
        with open(file_path, 'r') as f: users = f.read().splitlines()
        
        added = 0
        for user in users:
            try:
                await hellas(InviteToChannelRequest(target, [user]))
                added += 1
                await msg.edit(f"📥 جاري النقل إلى: **{target.title}**\n✅ المضافين حالياً: `{added}`")
                await asyncio.sleep(10) # تأخير لتجنب الحظر
            except errors.FloodWaitError as e:
                await event.respond(f"⏳ حظر مؤقت من التليجرام! انتظر `{e.seconds}` ثانية.")
                break
            except errors.UserPrivacyRestrictedError: continue
            except: continue
        
        await msg.edit(f"✅ انتهت عملية النقل.\n➕ إجمالي المضافين: `{added}`")
    except Exception as e: await event.edit(f"❌ خطأ في النقل: {e}")
    finally:
        if os.path.exists(file_path): os.remove(file_path)

# --- قائمة الأوامر ---
@hellas.on(events.NewMessage(pattern=r'^\.اوامر النقل$', outgoing=True))
async def transfer_help(event):
    help_text = (
        "⚙️ **أوامر نقل وسحب الأعضاء - سورس هيلاس:**\n\n"
        "• `.سحب [رابط]`\n"
        "  - لسحب يوزرات أعضاء المجموعة لملف نصي.\n\n"
        "• `.ايقاف السحب`\n"
        "  - لإيقاف عملية السحب الجارية فوراً.\n\n"
        "• `.نقل [رابط]`\n"
        "  - رد على ملف يوزرات لنقلهم إلى المجموعة المطلوبة.\n\n"
        "⚠️ **ملاحظة:** يفضل أن يكون الحساب أدمن في المجموعة التي تنقل إليها."
    )
    await event.edit(help_text)
