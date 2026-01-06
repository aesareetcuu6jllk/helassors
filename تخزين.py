import asyncio
import __main__ as main_module
from telethon import events, functions, types
from datetime import datetime
import os

# ربط المحرك
hellas = main_module.hellas

# نظام حفظ الحالة في قاعدة البيانات لضمان الاستمرارية بعد التحديث
try:
    from JoKeRUB.sql_helper.globals import addgvar, delgvar, gvarstatus
except:
    # حل بديل في حال عدم وجود قاعدة بيانات
    def addgvar(k, v): globals()[k] = v
    def delgvar(k): globals().pop(k, None)
    def gvarstatus(k): return globals().get(k)

# --- دالة جلب أو إنشاء مجموعة التخزين ---
async def get_or_create_log_group():
    group_id = gvarstatus("HELLAS_LOG_ID")
    if group_id:
        try:
            return int(group_id)
        except:
            pass
    
    try:
        result = await hellas(functions.channels.CreateChannelRequest(
            title="تخزين هيلاس - أرشيف الرسائل",
            about="هذه المجموعة لتخزين رسائل الخاص والكروبات تلقائياً",
            megagroup=True
        ))
        new_id = result.chats[0].id
        full_id = int(f"-100{new_id}")
        addgvar("HELLAS_LOG_ID", str(full_id))
        return full_id
    except:
        return "me"

# --- أوامر التفعيل (تشغيل وحفظ الحالة) ---

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^\.تفعيل التخزين$"))
async def enable_all(event):
    addgvar("log_private", "on")
    addgvar("log_groups", "on")
    log_id = await get_or_create_log_group()
    await event.edit(f"**᯽︙ تم تفعيل التخزين الشامل وحفظ الحالة ✅**\n**⌔∮ الوجهة:** `{log_id}`")

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^\.تفعيل التخزين خاص$"))
async def enable_pv(event):
    addgvar("log_private", "on")
    await event.edit("**᯽︙ تم تفعيل تخزين الخاص وحفظ الحالة ✅**")

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^\.تفعيل التخزين كروبات$"))
async def enable_gp(event):
    addgvar("log_groups", "on")
    await event.edit("**᯽︙ تم تفعيل تخزين الكروبات وحفظ الحالة ✅**")

# --- أوامر التعطيل (إيقاف وحذف الحالة) ---

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^\.تعطيل التخزين$"))
async def disable_all(event):
    delgvar("log_private")
    delgvar("log_groups")
    await event.edit("**᯽︙ تم تعطيل التخزين الشامل وإيقاف الحفظ ❌**")

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^\.تعطيل التخزين خاص$"))
async def disable_pv(event):
    delgvar("log_private")
    await event.edit("**᯽︙ تم تعطيل تخزين الخاص ❌**")

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^\.تعطيل التخزين كروبات$"))
async def disable_gp(event):
    delgvar("log_groups")
    await event.edit("**᯽︙ تم تعطيل تخزين الكروبات ❌**")

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^\.تعديل التخزين$"))
async def change_log(event):
    addgvar("HELLAS_LOG_ID", str(event.chat_id))
    await event.edit(f"**᯽︙ تم تحديث وجهة التخزين إلى هذه المجموعة ✅**")

# --- محرك الأرشفة التلقائي ---

@hellas.on(events.NewMessage(incoming=True))
async def auto_logger(event):
    # التحقق من الحالة المحفوظة في القاعدة
    can_log_pv = event.is_private and gvarstatus("log_private") == "on"
    can_log_gp = event.is_group and gvarstatus("log_groups") == "on"
    
    if can_log_pv or can_log_gp:
        log_chat = await get_or_create_log_group()
        sender = await event.get_sender()
        name = sender.first_name if sender else "مستخدم"
        time_now = datetime.now().strftime("%Y-%m-%d | %I:%M:%S %p")
        
        # رابط الرسالة
        chat_link = f"https://t.me/c/{str(event.chat_id)[4:]}/{event.id}" if event.is_group else "محادثة خاصة"
        
        header = "📂 **أرشيف الكروبات**" if event.is_group else "👤 **أرشيف الخاص**"
        caption = (
            f"{header}\n"
            f"**•───── HELLAS ─────•**\n"
            f"**👤 من:** [{name}](tg://user?id={event.sender_id})\n"
            f"**⏰ الوقت:** `{time_now}`\n"
            f"**🔗 الرابط:** [اضغط هنا]({chat_link})\n"
            f"**•───── HELLAS ─────•**"
        )

        try:
            if event.message.text and not event.media:
                await hellas.send_message(log_chat, f"{caption}\n\n**📝 النص:**\n{event.message.text}", link_preview=False)
            elif event.media:
                await hellas.send_file(log_chat, event.message, caption=caption)
        except:
            pass
