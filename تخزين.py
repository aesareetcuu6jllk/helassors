import asyncio
import __main__ as main_module
from telethon import events, functions, types
from datetime import datetime
import os

# ربط المحرك
hellas = main_module.hellas

# مسارات التخزين بالقاعدة (لضمان الاستمرارية)
try:
    from JoKeRUB.sql_helper.globals import addgvar, delgvar, gvarstatus
except:
    def addgvar(k, v): globals()[k] = v
    def delgvar(k): globals().pop(k, None)
    def gvarstatus(k): return globals().get(k)

# --- دالة إنشاء مجموعة التخزين تلقائياً ---
async def get_or_create_log_group():
    group_id = gvarstatus("HELLAS_LOG_ID")
    if group_id:
        return int(group_id)
    
    # إذا لم توجد مجموعة، نقوم بإنشائها
    try:
        result = await hellas(functions.channels.CreateChannelRequest(
            title="تخزين هيلاس - أرشيف الرسائل",
            about="هذه المجموعة لتخزين رسائل الخاص والكروبات تلقائياً",
            megagroup=True
        ))
        new_id = result.chats[0].id
        # تحويل الأيدي لصيغة كاملة
        full_id = int(f"-100{new_id}")
        addgvar("HELLAS_LOG_ID", str(full_id))
        return full_id
    except:
        return "me" # إذا فشل الإنشاء يحفظ بالرسائل المحفوظة

# --- الأوامر ---

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^\.تفعيل التخزين$"))
async def enable_all(event):
    addgvar("log_private", "on")
    addgvar("log_groups", "on")
    log_id = await get_or_create_log_group()
    await event.edit(f"**᯽︙ تم تفعيل التخزين الشامل بنجاح ✅**\n**⌔∮ يتم التخزين الآن في الأيدي:** `{log_id}`")

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^\.تفعيل التخزين خاص$"))
async def enable_pv(event):
    addgvar("log_private", "on")
    await event.edit("**᯽︙ تم تفعيل تخزين رسائل الخاص فقط ✅**")

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^\.تفعيل التخزين كروبات$"))
async def enable_gp(event):
    addgvar("log_groups", "on")
    await event.edit("**᯽︙ تم تفعيل تخزين الكروبات فقط ✅**")

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^\.تعديل التخزين$"))
async def change_log(event):
    # يسمح لك بتغيير مجموعة التخزين يدوياً بالرد على مجموعة أخرى
    addgvar("HELLAS_LOG_ID", str(event.chat_id))
    await event.edit(f"**᯽︙ تم تعديل وجهة التخزين إلى هذه المجموعة بنجاح ✅**")

# --- محرك الحفظ التلقائي ---

@hellas.on(events.NewMessage(incoming=True))
async def auto_logger(event):
    # فحص الإعدادات
    is_pv = event.is_private and gvarstatus("log_private")
    is_gp = event.is_group and gvarstatus("log_groups")
    
    if is_pv or is_gp:
        log_chat = await get_or_create_log_group()
        sender = await event.get_sender()
        name = sender.first_name if sender else "مستخدم غير معروف"
        time_now = datetime.now().strftime("%Y-%m-%d | %I:%M:%S %p")
        
        # تجهيز رابط الرسالة
        chat_link = f"https://t.me/c/{str(event.chat_id)[4:]}/{event.id}" if event.is_group else "محادثة خاصة"
        
        header = "📂 **تخزين جديد (مجموعة)**" if event.is_group else "👤 **تخزين جديد (خاص)**"
        caption = (
            f"{header}\n"
            f"**•───── هيلاس ─────•**\n"
            f"**👤 المرسل:** [{name}](tg://user?id={event.sender_id})\n"
            f"**⏰ الوقت:** `{time_now}`\n"
            f"**🔗 رابط الرسالة:** [اضغط هنا]({chat_link})\n"
            f"**•───── هيلاس ─────•**"
        )

        try:
            # إذا كانت الرسالة نصية فقط
            if event.message.text and not event.media:
                full_text = f"{caption}\n\n**📝 الرسالة:**\n{event.message.text}"
                await hellas.send_message(log_chat, full_text, link_preview=False)
            
            # إذا كانت الرسالة ميديا (صورة، فيديو، بصمة...)
            elif event.media:
                await hellas.send_file(log_chat, event.message, caption=caption)
        except:
            pass
