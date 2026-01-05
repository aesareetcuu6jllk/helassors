import asyncio
import __main__ as main_module
from telethon import events
from telethon.tl.functions.channels import LeaveChannelRequest

# ربط محرك السورس
hellas = main_module.hellas

# متغير تتبع الإيقاف
stop_leaving = False

@hellas.on(events.NewMessage(outgoing=True, pattern=r'^\.مغادرة$'))
async def leave_all_channels(event):
    global stop_leaving
    stop_leaving = False
    
    await event.edit("**᯽︙ جاري جرد القنوات والمجموعات والمغادرة...**")
    
    count = 0
    try:
        async for dialog in hellas.iter_dialogs():
            if stop_leaving:
                break
            
            # مغادرة القنوات والمجموعات (باستثناء المحادثات الخاصة والبوتات)
            if dialog.is_channel or dialog.is_group:
                try:
                    await hellas(LeaveChannelRequest(dialog.entity))
                    count += 1
                    # تأخير بسيط جداً لتجنب الحظر
                    await asyncio.sleep(0.5) 
                except:
                    continue
        
        status = "✅ تم المغادرة من جميع القنوات." if not stop_leaving else "⏹ تم إيقاف العملية."
        await hellas.send_message("me", f"**᯽︙ تقرير المغادرة:**\n\n{status}\n**⌔∮ عدد المغادرات:** `{count}`")
        await event.delete()
        
    except Exception as e:
        await event.edit(f"**❌ حدث خطأ:** `{str(e)}`")

@hellas.on(events.NewMessage(outgoing=True, pattern=r'^\.إيقاف المغادرة$'))
async def stop_leaving_cmd(event):
    global stop_leaving
    stop_leaving = True
    await event.edit("**᯽︙ تم إرسال أمر إيقاف المغادرة بنجاح ✓**")
