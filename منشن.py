import asyncio
import __main__ as main_module
from telethon import events

# ربط محرك السورس
hellas = main_module.hellas

# قائمة لتتبع عمليات المنشن في كل دردشة بشكل منفصل
mention_chats = {}

# --- أمر المنشن (واحد واحد) ---
@hellas.on(events.NewMessage(outgoing=True, pattern=r"^\.منشن ?(.*)"))
async def mention_all(event):
    chat_id = event.chat_id
    if event.is_private:
        return await event.edit("**᯽︙ هذا الأمر للمجموعات فقط!**")
    
    msg = event.pattern_match.group(1) or "هلو"
    
    if chat_id in mention_chats:
        return await event.edit("**᯽︙ هناك عملية منشن جارية بالفعل!**")
    
    await event.delete()
    mention_chats[chat_id] = True
    
    async for user in hellas.iter_participants(chat_id):
        if chat_id not in mention_chats:
            break
        if user.bot: continue # تخطي البوتات
        
        tag = f"[{user.first_name}](tg://user?id={user.id})"
        try:
            await hellas.send_message(chat_id, f"{msg}\n\n{tag}")
            await asyncio.sleep(2.5) # تأخير آمن لتجنب الحظر
        except:
            break
            
    mention_chats.pop(chat_id, None)

# --- أمر التاك (كل 5 سوا - أسرع) ---
@hellas.on(events.NewMessage(outgoing=True, pattern=r"^\.تاك ?(.*)"))
async def tag_all(event):
    chat_id = event.chat_id
    if event.is_private:
        return await event.edit("**᯽︙ هذا الأمر للمجموعات فقط!**")
    
    msg = event.pattern_match.group(1) or "تنبيه للجميع 📢"
    
    if chat_id in mention_chats:
        return await event.edit("**᯽︙ هناك عملية منشن/تاك جارية بالفعل!**")
    
    await event.edit("**᯽︙ جاري بدء عملية التاك الجماعي...**")
    mention_chats[chat_id] = True
    
    participants = []
    async for user in hellas.iter_participants(chat_id):
        if not user.bot:
            participants.append(user)
    
    await event.delete()
    
    # تقسيم الأعضاء لمجموعات (كل رسالة فيها 5 أعضاء)
    for i in range(0, len(participants), 5):
        if chat_id not in mention_chats:
            break
            
        chunk = participants[i:i+5]
        tags = " ".join([f"[{u.first_name}](tg://user?id={u.id})" for u in chunk])
        
        try:
            await hellas.send_message(chat_id, f"{msg}\n\n{tags}")
            await asyncio.sleep(3)
        except:
            break
            
    mention_chats.pop(chat_id, None)

# --- أمر الإلغاء ---
@hellas.on(events.NewMessage(outgoing=True, pattern=r"^\.الغاء (تاك|منشن)$"))
async def stop_tag(event):
    chat_id = event.chat_id
    if chat_id in mention_chats:
        mention_chats.pop(chat_id)
        await event.edit("**᯽︙ تم إلغاء العملية بنجاح ✓**")
    else:
        await event.edit("**᯽︙ لا توجد عملية جارية لإلغائها!**")
