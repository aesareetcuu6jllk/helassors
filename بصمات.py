import __main__ as main_module
from telethon import events

# ربط محرك السورس
hellas = main_module.hellas

# دالة مساعدة لجلب أيدي الرد
async def get_reply_id(event):
    reply = await event.get_reply_message()
    if reply:
        return reply.id
    return None

# --- الأوامر ---

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^\.احبك مصطفى$"))
async def meme_1(event):
    reply_to = await get_reply_id(event)
    url = "https://t.me/yyegksgfdg/12"
    await event.client.send_file(event.chat_id, url, reply_to=reply_to)
    await event.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^\.بلتفك$"))
async def meme_2(event):
    reply_to = await get_reply_id(event)
    url = "https://t.me/NC2CN/7"
    await event.client.send_file(event.chat_id, url, reply_to=reply_to)
    await event.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^\.ش1$"))
async def meme_3(event):
    reply_to = await get_reply_id(event)
    url = "https://t.me/i8RTl/4344"
    await event.client.send_file(event.chat_id, url, reply_to=reply_to)
    await event.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^\.ها يوسف$"))
async def meme_4(event):
    reply_to = await get_reply_id(event)
    url = "https://t.me/AJSJ36/2430"
    await event.client.send_file(event.chat_id, url, reply_to=reply_to)
    await event.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^\.انا ماشي$"))
async def meme_5(event):
    reply_to = await get_reply_id(event)
    url = "https://t.me/iirrrq/15"
    await event.client.send_file(event.chat_id, url, reply_to=reply_to)
    await event.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^\.اني شكو$"))
async def meme_6(event):
    reply_to = await get_reply_id(event)
    url = "https://t.me/my_7_8/4"
    await event.client.send_file(event.chat_id, url, reply_to=reply_to)
    await event.delete()
