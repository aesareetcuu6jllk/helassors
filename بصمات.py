import __main__ as main_module
from telethon import events
import asyncio

# ربط محرك سورس هيلاس
hellas = main_module.hellas


@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.فك عيوني$"))
async def jepmeme(memejep):
  r = await memejep.get_reply_message(); Jep = r.id if r else None
  url = f"https://t.me/NC2CN/10"
  await hellas.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()


@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.امرع$"))
async def jepmeme(memejep):
  r = await memejep.get_reply_message(); Jep = r.id if r else None
  url = f"https://t.me/NC2CN/13"
  await hellas.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()


@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.الجبور$"))
async def jepmeme(memejep):
  r = await memejep.get_reply_message(); Jep = r.id if r else None
  url = f"https://t.me/NC2CN/14"
  await hellas.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.كرنج$"))
async def jepmeme(memejep):
  r = await memejep.get_reply_message(); Jep = r.id if r else None
  url = f"https://t.me/NC2CN/730"
  await hellas.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()


@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.سيلوش$"))
async def jepmeme(memejep):
  r = await memejep.get_reply_message(); Jep = r.id if r else None
  url = f"https://t.me/NC2CN/734"
  await hellas.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.ام لحلقوم$"))
async def jepmeme(memejep):
  r = await memejep.get_reply_message(); Jep = r.id if r else None
  url = f"https://t.me/NC2CN/737"
  await hellas.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.شموتك$"))
async def jepmeme(memejep):
  r = await memejep.get_reply_message(); Jep = r.id if r else None
  url = f"https://t.me/NC2CN/738"
  await hellas.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()


@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.بكيفك$"))
async def jepmeme(memejep):
  r = await memejep.get_reply_message(); Jep = r.id if r else None
  url = f"https://t.me/NC2CN/739"
  await hellas.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()


@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.نصو$"))
async def jepmeme(memejep):
  r = await memejep.get_reply_message(); Jep = r.id if r else None
  url = f"https://t.me/NC2CN/741"
  await hellas.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()


@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.ياهو انت$"))
async def jepmeme(memejep):
  r = await memejep.get_reply_message(); Jep = r.id if r else None
  url = f"https://t.me/NC2CN/745"
  await hellas.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()



@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.اضحكله$"))
async def jepmeme(memejep):
  r = await memejep.get_reply_message(); Jep = r.id if r else None
  url = f"https://t.me/NC2CN/751"
  await hellas.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.هلا$"))
async def jepmeme(memejep):
  r = await memejep.get_reply_message(); Jep = r.id if r else None
  url = f"https://t.me/AJSJ36/1101"
  await hellas.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.شلخبار$"))
async def jepmeme(memejep):
  r = await memejep.get_reply_message(); Jep = r.id if r else None
  url = f"https://t.me/AJSJ36/1103"
  await hellas.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.شلونك$"))
async def jepmeme(memejep):
  r = await memejep.get_reply_message(); Jep = r.id if r else None
  url = f"https://t.me/AJSJ36/1105"
  await hellas.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()


@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.شلونج$"))
async def jepmeme(memejep):
  r = await memejep.get_reply_message(); Jep = r.id if r else None
  url = f"https://t.me/AJSJ36/1107"
  await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
  await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.نتعرف$"))
async def jepmeme(memejep):
  r = await memejep.get_reply_message(); Jep = r.id if r else None
  url = f"https://t.me/AJSJ36/1109"
  await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
  await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.اني معجبه$"))
async def jepmeme(memejep):
  r = await memejep.get_reply_message(); Jep = r.id if r else None
  url = f"https://t.me/AJSJ36/1112"
  await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
  await memejep.delete()

# ... تم تكرار نفس الكود 20 مرة

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.عجبني اراسلك$"))
async def jepmeme(memejep):
  r = await memejep.get_reply_message(); Jep = r.id if r else None
  url = f"https://t.me/AJSJ36/1114"
  await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
  await memejep.delete()



@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.نرتبط$"))
async def jepmeme(memejep):
  r = await memejep.get_reply_message(); Jep = r.id if r else None
  url = f"https://t.me/AJSJ36/1116"
  await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
  await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.نتزوج$"))
async def jepmeme(memejep):
  r = await memejep.get_reply_message(); Jep = r.id if r else None
  url = f"https://t.me/AJSJ36/1118"
  await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
  await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.ترا حبيتك$"))
async def jepmeme(memejep):
  r = await memejep.get_reply_message(); Jep = r.id if r else None
  url = f"https://t.me/AJSJ36/1120"
  await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
  await memejep.delete()

# ... تم تكرار نفس الكود 20 مرة

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.هلكد ثكيل"))
async def jepmeme(memejep):
  r = await memejep.get_reply_message(); Jep = r.id if r else None
  url = f"https://t.me/AJSJ36/1122"
  await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
  await memejep.delete()


@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.دز رصيد$"))
async def jepmeme(memejep):
  r = await memejep.get_reply_message(); Jep = r.id if r else None
  url = f"https://t.me/AJSJ36/1127"
  await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
  await memejep.delete()



@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.غنيله$"))
async def jepmeme(memejep):
  r = await memejep.get_reply_message(); Jep = r.id if r else None
  url = f"https://t.me/AJSJ36/3184"
  await hellas.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.اريد رصيد$"))
async def jepmeme(memejep):
  r = await memejep.get_reply_message(); Jep = r.id if r else None
  url = f"https://t.me/AJSJ36/1129"
  await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
  await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.ارشقلي$"))
async def jepmeme(memejep):
  r = await memejep.get_reply_message(); Jep = r.id if r else None
  url = f"https://t.me/AJSJ36/1131"
  await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
  await memejep.delete()

# ... تم تكرار نفس الكود 20 مرة

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.ارشق قناتي$"))
async def jepmeme(memejep):
  r = await memejep.get_reply_message(); Jep = r.id if r else None
  url = f"fhttps://t.me/AJSJ36/1133"
  await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
  await memejep.delete()


@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.ارشقلي حسابي$"))
async def jepmeme(memejep):
  r = await memejep.get_reply_message(); Jep = r.id if r else None
  url = f"https://t.me/AJSJ36/1135"
  await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
  await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.سويلي تمويل$"))
async def jepmeme(memejep):
  r = await memejep.get_reply_message(); Jep = r.id if r else None
  url = f"https://t.me/AJSJ36/1137"
  await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
  await memejep.delete()




@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.دز صورتك$"))
async def jepmeme(memejep):
  r = await memejep.get_reply_message(); Jep = r.id if r else None
  url = f"https://t.me/AJSJ36/1139"
  await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
  await memejep.delete()

# ... تم تكرار نفس الكود 20 مرة

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.دز ببجي"))
async def jepmeme(memejep):
  r = await memejep.get_reply_message(); Jep = r.id if r else None
  url = f"https://t.me/AJSJ36/1141"
  await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
  await memejep.delete()



@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.دز لودو$"))
async def jepmeme(memejep):
  r = await memejep.get_reply_message(); Jep = r.id if r else None
  url = f"https://t.me/AJSJ36/1143"
  await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
  await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.حساب انستا$"))
async def jepmeme(memejep):
  r = await memejep.get_reply_message(); Jep = r.id if r else None
  url = f"https://t.me/AJSJ36/1145"
  await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
  await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.حساب تيك$"))
async def jepmeme(memejep):
  r = await memejep.get_reply_message(); Jep = r.id if r else None
  url = f"https://t.me/AJSJ36/1147"
  await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
  await memejep.delete()

# ... تم تكرار نفس الكود 20 مرة

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.الو$"))
async def jepmeme(memejep):
  r = await memejep.get_reply_message(); Jep = r.id if r else None
  url = f"https://t.me/AJSJ36/1154"
  await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
  await memejep.delete()
@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.وينك$"))
async def jepmeme(memejep):
  r = await memejep.get_reply_message(); Jep = r.id if r else None
  url = f"https://t.me/AJSJ36/1156"
  await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
  await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.وينج$"))
async def jepmeme(memejep):
  r = await memejep.get_reply_message(); Jep = r.id if r else None
  url = f"https://t.me/AJSJ36/1158"
  await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
  await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.اي$"))
async def jepmeme(memejep):
  r = await memejep.get_reply_message(); Jep = r.id if r else None
  url = f"https://t.me/AJSJ36/1160"
  await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
  await memejep.delete()

# ... تم تكرار نفس الكود 20 مرة

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.لا$"))
async def jepmeme(memejep):
  r = await memejep.get_reply_message(); Jep = r.id if r else None
  url = f"https://t.me/AJSJ36/1162"
  await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
  await memejep.delete()



@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.اكل خره$"))
async def jepmeme(memejep):
  r = await memejep.get_reply_message(); Jep = r.id if r else None
  url = f"https://t.me/AJSJ36/1164"
  await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
  await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.اكلي خره$"))
async def jepmeme(memejep):
  r = await memejep.get_reply_message(); Jep = r.id if r else None
  url = f"https://t.me/AJSJ36/1166"
  await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
  await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.يله$"))
async def jepmeme(memejep):
  r = await memejep.get_reply_message(); Jep = r.id if r else None
  url = f"https://t.me/AJSJ36/1170"
  await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
  await memejep.delete()

# ... تم تكرار نفس الكود 20 مرة

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.شبيك$"))
async def jepmeme(memejep):
  r = await memejep.get_reply_message(); Jep = r.id if r else None
  url = f"https://t.me/AJSJ36/1172"
  await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
  await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.شبيج$"))
async def jepmeme(memejep):
  r = await memejep.get_reply_message(); Jep = r.id if r else None
  url = f"https://t.me/AJSJ36/1174"
  await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
  await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.احبك$"))
async def jepmeme(memejep):
  r = await memejep.get_reply_message(); Jep = r.id if r else None
  url = f"https://t.me/AJSJ36/1176"
  await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
  await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.احبج$"))
async def jepmeme(memejep):
  r = await memejep.get_reply_message(); Jep = r.id if r else None
  url = f"https://t.me/AJSJ36/1178"
  await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
  await memejep.delete()

# ... تم تكرار نفس الكود 20 مرة

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.تحبني$"))
async def jepmeme(memejep):
  r = await memejep.get_reply_message(); Jep = r.id if r else None
  url = f"https://t.me/AJSJ36/1180"
  await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
  await memejep.delete()




@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.انطي بوسه$"))
async def jepmeme(memejep):
  r = await memejep.get_reply_message(); Jep = r.id if r else None
  url = f"https://t.me/AJSJ36/1182"
  await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
  await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.ابوسك$"))
async def jepmeme(memejep):
  r = await memejep.get_reply_message(); Jep = r.id if r else None
  url = f"https://t.me/AJSJ36/1189"
  await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
  await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.احضنك$"))
async def jepmeme(memejep):
  r = await memejep.get_reply_message(); Jep = r.id if r else None
  url = f"https://t.me/AJSJ36/1191"
  await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
  await memejep.delete()

# ... تم تكرار نفس الكود 20 مرة

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.اريدك بس الي$"))
async def jepmeme(memejep):
  r = await memejep.get_reply_message(); Jep = r.id if r else None
  url = f"https://t.me/AJSJ36/1194"
  await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
  await memejep.delete()






@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.ماكدر تصال$"))
async def jepmeme(memejep):
  r = await memejep.get_reply_message(); Jep = r.id if r else None
  url = f"https://t.me/AJSJ36/1196"
  await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
  await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.ماحب لتصال$"))
async def jepmeme(memejep):
  r = await memejep.get_reply_message(); Jep = r.id if r else None
  url = f"https://t.me/AJSJ36/1197"
  await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
  await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.هاي احسن$"))
async def jepmeme(memejep):
  r = await memejep.get_reply_message(); Jep = r.id if r else None
  url = f"https://t.me/AJSJ36/1199"
  await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
  await memejep.delete()

# ... تم تكرار نفس الكود 20 مرة

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.يلا لتلح$"))
async def jepmeme(memejep):
  r = await memejep.get_reply_message(); Jep = r.id if r else None
  url = f"https://t.me/AJSJ36/1203"
  await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
  await memejep.delete()




@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.لا تلحين$"))
async def jepmeme(memejep):
  r = await memejep.get_reply_message(); Jep = r.id if r else None
  url = f"https://t.me/AJSJ36/1205"
  await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
  await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.امداك$"))
async def jepmeme(memejep):
  r = await memejep.get_reply_message(); Jep = r.id if r else None
  url = f"https://t.me/AJSJ36/1207"
  await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
  await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.امداج$"))
async def jepmeme(memejep):
  r = await memejep.get_reply_message(); Jep = r.id if r else None
  url = f"https://t.me/AJSJ36/1209"
  await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
  await memejep.delete()



@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.تمام$"))
async def jepmeme(memejep):
  r = await memejep.get_reply_message(); Jep = r.id if r else None
  url = f"https://t.me/AJSJ36/1212"
  await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
  await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.هلو محمد$"))
async def jepmeme(memejep):
  r = await memejep.get_reply_message(); Jep = r.id if r else None
  url = f"https://t.me/AJSJ36/3145"
  await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
  await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.باي$"))
async def jepmeme(memejep):
  r = await memejep.get_reply_message(); Jep = r.id if r else None
  url = f"https://t.me/AJSJ36/1213"
  await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
  await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.مابيه شي$"))
async def jepmeme(memejep):
  r = await memejep.get_reply_message(); Jep = r.id if r else None
  url = f"https://t.me/AJSJ36/1217"
  await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
  await memejep.delete()

# ... تم تكرار نفس الكود 20 مرة

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.منو$"))
async def jepmeme(memejep):
  r = await memejep.get_reply_message(); Jep = r.id if r else None
  url = f"https://t.me/AJSJ36/1219"
  await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
  await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.كول$"))
async def jepmeme(memejep):
  r = await memejep.get_reply_message(); Jep = r.id if r else None
  url = f"https://t.me/AJSJ36/1237"
  await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
  await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.اكلج$"))
async def jepmeme(memejep):
  r = await memejep.get_reply_message(); Jep = r.id if r else None
  url = f"https://t.me/AJSJ36/1239"
  await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
  await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.كولي$"))
async def jepmeme(memejep):
  r = await memejep.get_reply_message(); Jep = r.id if r else None
  url = f"https://t.me/AJSJ36/1242"
  await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
  await memejep.delete()

# ... تم تكرار نفس الكود 20 مرة

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.مبي شحن$"))
async def jepmeme(memejep):
  r = await memejep.get_reply_message(); Jep = r.id if r else None
  url = f"https://t.me/AJSJ36/1243"
  await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
  await memejep.delete()




@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.من بغداد$"))
async def jepmeme(memejep):
  r = await memejep.get_reply_message(); Jep = r.id if r else None
  url = f"https://t.me/AJSJ36/1245"
  await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
  await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.من الكوت$"))
async def jepmeme(memejep):
  r = await memejep.get_reply_message(); Jep = r.id if r else None
  url = f"https://t.me/AJSJ36/1247"
  await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
  await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.من لعماره$"))
async def jepmeme(memejep):
  r = await memejep.get_reply_message(); Jep = r.id if r else None
  url = f"https://t.me/AJSJ36/1249"
  await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
  await memejep.delete()

# ... تم تكرار نفس الكود 20 مرة

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.من الناصريه$"))
async def jepmeme(memejep):
  r = await memejep.get_reply_message(); Jep = r.id if r else None
  url = f"https://t.me/AJSJ36/1251"
  await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
  await memejep.delete()





@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.من البصره$"))
async def jepmeme(memejep):
  r = await memejep.get_reply_message(); Jep = r.id if r else None
  url = f"https://t.me/AJSJ36/1253"
  await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
  await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.من الديوانيه$"))
async def jepmeme(memejep):
  r = await memejep.get_reply_message(); Jep = r.id if r else None
  url = f"https://t.me/AJSJ36/1255"
  await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
  await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.من الحله$"))
async def jepmeme(memejep):
  r = await memejep.get_reply_message(); Jep = r.id if r else None
  url = f"https://t.me/AJSJ36/1257"
  await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
  await memejep.delete()

# ... تم تكرار نفس الكود 20 مرة

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.من السماوه$"))
async def jepmeme(memejep):
  r = await memejep.get_reply_message(); Jep = r.id if r else None
  url = f"https://t.me/AJSJ36/1259"
  await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
  await memejep.delete()





@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.من كربلاء$"))
async def jepmeme(memejep):
  r = await memejep.get_reply_message(); Jep = r.id if r else None
  url = f"https://t.me/AJSJ36/1261"
  await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
  await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.من النجف$"))
async def jepmeme(memejep):
  r = await memejep.get_reply_message(); Jep = r.id if r else None
  url = f"https://t.me/AJSJ36/1263"
  await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
  await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.من دبالى$"))
async def jepmeme(memejep):
  r = await memejep.get_reply_message(); Jep = r.id if r else None
  url = f"https://t.me/AJSJ36/1265"
  await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
  await memejep.delete()

# ... تم تكرار نفس الكود 20 مرة

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.من صلاح الدين$"))
async def jepmeme(memejep):
  r = await memejep.get_reply_message(); Jep = r.id if r else None
  url = f"https://t.me/AJSJ36/1267"
  await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
  await memejep.delete()




@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.من كركوك$"))
async def jepmeme(memejep):
  r = await memejep.get_reply_message(); Jep = r.id if r else None
  url = f"https://t.me/AJSJ36/1269"
  await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
  await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.من الموصل$"))
async def jepmeme(memejep):
  r = await memejep.get_reply_message(); Jep = r.id if r else None
  url = f"https://t.me/AJSJ36/1271"
  await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
  await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.من سليمانيه$"))
async def jepmeme(memejep):
  r = await memejep.get_reply_message(); Jep = r.id if r else None
  url = f"https://t.me/AJSJ36/1273"
  await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
  await memejep.delete()

# ... تم تكرار نفس الكود 20 مرة

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.من اربيل$"))
async def jepmeme(memejep):
  r = await memejep.get_reply_message(); Jep = r.id if r else None
  url = f"https://t.me/AJSJ36/1275"
  await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
  await memejep.delete()


@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.من دهوك$"))
async def jepmeme(memejep):
  r = await memejep.get_reply_message(); Jep = r.id if r else None
  url = f"https://t.me/AJSJ36/1277"
  await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
  await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.فعلي مميز$"))
async def jepmeme(memejep):
  r = await memejep.get_reply_message(); Jep = r.id if r else None
  url = f"https://t.me/AJSJ36/1281"
  await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
  await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.بوسهه$"))
async def jepmeme(memejep):
  r = await memejep.get_reply_message(); Jep = r.id if r else None
  url = f"https://t.me/AJSJ36/1283"
  await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
  await memejep.delete()

# ... تم تكرار نفس الكود 20 مرة

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.افتح كام$"))
async def jepmeme(memejep):
  r = await memejep.get_reply_message(); Jep = r.id if r else None
  url = f"https://t.me/AJSJ36/1285"
  await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
  await memejep.delete()



@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.دز شدات$"))
async def jepmeme(memejep):
  r = await memejep.get_reply_message(); Jep = r.id if r else None
  url = f"https://t.me/AJSJ36/1288"
  await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
  await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.شنو$"))
async def jepmeme(memejep):
  r = await memejep.get_reply_message(); Jep = r.id if r else None
  url = f"https://t.me/AJSJ36/1289"
  await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
  await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.عرفني عليك$"))
async def jepmeme(memejep):
  r = await memejep.get_reply_message(); Jep = r.id if r else None
  url = f"https://t.me/AJSJ36/1291"
  await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
  await memejep.delete()

# ... تم تكرار نفس الكود 20 مرة

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.وانته$"))
async def jepmeme(memejep):
  r = await memejep.get_reply_message(); Jep = r.id if r else None
  url = f"https://t.me/AJSJ36/1293"
  await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
  await memejep.delete()



@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.ها$"))
async def jepmeme(memejep):
  r = await memejep.get_reply_message(); Jep = r.id if r else None
  url = f"https://t.me/AJSJ36/1295"
  await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
  await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.شتريد$"))
async def jepmeme(memejep):
  r = await memejep.get_reply_message(); Jep = r.id if r else None
  url = f"https://t.me/AJSJ36/1297"
  await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
  await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.اني بنيه$"))
async def jepmeme(memejep):
  r = await memejep.get_reply_message(); Jep = r.id if r else None
  url = f"https://t.me/AJSJ36/1306"
  await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
  await memejep.delete()

# ... تم تكرار نفس الكود 20 مرة

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.اني بنيه لج$"))
async def jepmeme(memejep):
  r = await memejep.get_reply_message(); Jep = r.id if r else None
  url = f"https://t.me/AJSJ36/1308"
  await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
  await memejep.delete()



@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.17$"))
async def jepmeme(memejep):
  r = await memejep.get_reply_message(); Jep = r.id if r else None
  url = f"https://t.me/AJSJ36/1310"
  await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
  await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.18$"))
async def jepmeme(memejep):
  r = await memejep.get_reply_message(); Jep = r.id if r else None
  url = f"https://t.me/AJSJ36/1315"
  await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
  await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.19$"))
async def jepmeme(memejep):
  r = await memejep.get_reply_message(); Jep = r.id if r else None
  url = f"https://t.me/AJSJ36/1316"
  await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
  await memejep.delete()

# ... تم تكرار نفس الكود 20 مرة

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.20$"))
async def jepmeme(memejep):
  r = await memejep.get_reply_message(); Jep = r.id if r else None
  url = f"https://t.me/AJSJ36/1318"
  await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
  await memejep.delete()


@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.21$"))
async def jepmeme(memejep):
  r = await memejep.get_reply_message(); Jep = r.id if r else None
  url = f"https://t.me/AJSJ36/1320"
  await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
  await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.22$"))
async def jepmeme(memejep):
  r = await memejep.get_reply_message(); Jep = r.id if r else None
  url = f"https://t.me/AJSJ36/1322"
  await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
  await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.ها كبينه$"))
async def jepmeme(memejep):
  r = await memejep.get_reply_message(); Jep = r.id if r else None
  url = f"https://t.me/AJSJ36/1324"
  await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
  await memejep.delete()

# ... تم تكرار نفس الكود 20 مرة

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.وين مختفي$"))
async def jepmeme(memejep):
  r = await memejep.get_reply_message(); Jep = r.id if r else None
  url = f"https://t.me/AJSJ36/1328"
  await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
  await memejep.delete()



@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.ثقفو$"))
async def jepmeme(memejep):
  r = await memejep.get_reply_message(); Jep = r.id if r else None
  url = f"https://t.me/AJSJ36/1330"
  await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
  await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.جبتك لحاله$"))
async def jepmeme(memejep):
  r = await memejep.get_reply_message(); Jep = r.id if r else None
  url = f"https://t.me/AJSJ36/1332"
  await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
  await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.ارجع للمطبخ$"))
async def jepmeme(memejep):
  r = await memejep.get_reply_message(); Jep = r.id if r else None
  url = f"https://t.me/AJSJ36/1334"
  await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
  await memejep.delete()

# ... تم تكرار نفس الكود 20 مرة

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.شلونكم$"))
async def jepmeme(memejep):
  r = await memejep.get_reply_message(); Jep = r.id if r else None
  url = f"https://t.me/AJSJ36/1338"
  await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
  await memejep.delete()




@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.ليش$"))
async def jepmeme(memejep):
  r = await memejep.get_reply_message(); Jep = r.id if r else None
  url = f"https://t.me/AJSJ36/1221"
  await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
  await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.تعذرني$"))
async def jepmeme(memejep):
  r = await memejep.get_reply_message(); Jep = r.id if r else None
  url = f"https://t.me/AJSJ36/1223"
  await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
  await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.لا شكرا$"))
async def jepmeme(memejep):
  r = await memejep.get_reply_message(); Jep = r.id if r else None
  url = f"https://t.me/AJSJ36/1225"
  await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
  await memejep.delete()

# ... تم تكرار نفس الكود 20 مرة


@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.باي حبيبي$"))
async def jepmeme(memejep):
  r = await memejep.get_reply_message(); Jep = r.id if r else None
  url = f"https://t.me/AJSJ36/1227"
  await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
  await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.غير مره$"))
async def jepmeme(memejep):
  r = await memejep.get_reply_message(); Jep = r.id if r else None
  url = f"https://t.me/AJSJ36/1229"
  await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
  await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.اكره ليرد متاخر$"))
async def jepmeme(memejep):
  r = await memejep.get_reply_message(); Jep = r.id if r else None
  url = f"https://t.me/AJSJ36/1231"
  await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
  await memejep.delete()

# ... تم تكرار نفس الكود 20 مرة

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.اكلك$"))
async def jepmeme(memejep):
  r = await memejep.get_reply_message(); Jep = r.id if r else None
  url = f"https://t.me/AJSJ36/1235"
  await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
  await memejep.delete()




@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.عزه العزاك$"))
async def jepmeme(memejep):
    r = await memejep.get_reply_message(); Jep = r.id if r else None
    url = "https://t.me/AJSJ36/1431"
    await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.جنك ماعاجبك$"))
async def jepmeme(memejep):
    r = await memejep.get_reply_message(); Jep = r.id if r else None
    url = "https://t.me/AJSJ36/1433"
    await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.شكد سخيف$"))
async def jepmeme(memejep):
    r = await memejep.get_reply_message(); Jep = r.id if r else None
    url = "https://t.me/AJSJ36/1436"
    await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.انت مطي$"))
async def jepmeme(memejep):
    r = await memejep.get_reply_message(); Jep = r.id if r else None
    url = "https://t.me/AJSJ36/1438"
    await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.شكد تحمه$"))
async def jepmeme(memejep):
    r = await memejep.get_reply_message(); Jep = r.id if r else None
    url = "https://t.me/AJSJ36/1440"
    await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.شكد فكر$"))
async def jepmeme(memejep):
    r = await memejep.get_reply_message(); Jep = r.id if r else None
    url = "https://t.me/AJSJ36/1443"
    await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.شكد فطير$"))
async def jepmeme(memejep):
    r = await memejep.get_reply_message(); Jep = r.id if r else None
    url = "https://t.me/AJSJ36/1445"
    await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.شكد فاهي$"))
async def jepmeme(memejep):
    r = await memejep.get_reply_message(); Jep = r.id if r else None
    url = "https://t.me/AJSJ36/1447"
    await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.شكد غبي$"))
async def jepmeme(memejep):
    r = await memejep.get_reply_message(); Jep = r.id if r else None
    url = "https://t.me/AJSJ36/1449"
    await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.شنو اسمج$"))
async def jepmeme(memejep):
    r = await memejep.get_reply_message(); Jep = r.id if r else None
    url = "https://t.me/AJSJ36/1451"
    await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.شكرا$"))
async def jepmeme(memejep):
    r = await memejep.get_reply_message(); Jep = r.id if r else None
    url = "https://t.me/AJSJ36/1453"
    await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.هلو كرار$"))
async def jepmeme(memejep):
    r = await memejep.get_reply_message(); Jep = r.id if r else None
    url = "https://t.me/AJSJ36/1457"
    await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.امحح$"))
async def jepmeme(memejep):
    r = await memejep.get_reply_message(); Jep = r.id if r else None
    url = "https://t.me/AJSJ36/1459"
    await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.كافي$"))
async def jepmeme(memejep):
    r = await memejep.get_reply_message(); Jep = r.id if r else None
    url = "https://t.me/AJSJ36/1461"
    await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.ماتاكل خره$"))
async def jepmeme(memejep):
    r = await memejep.get_reply_message(); Jep = r.id if r else None
    url = "https://t.me/AJSJ36/1463"
    await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.ايع$"))
async def jepmeme(memejep):
    r = await memejep.get_reply_message(); Jep = r.id if r else None
    url = "https://t.me/AJSJ36/1465"
    await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.انجب$"))
async def jepmeme(memejep):
    r = await memejep.get_reply_message(); Jep = r.id if r else None
    url = "https://t.me/AJSJ36/1467"
    await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.وي$"))
async def jepmeme(memejep):
    r = await memejep.get_reply_message(); Jep = r.id if r else None
    url = "https://t.me/AJSJ36/1469"
    await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.فهمت لو لا$"))
async def jepmeme(memejep):
    r = await memejep.get_reply_message(); Jep = r.id if r else None
    url = "https://t.me/AJSJ36/1471"
    await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.عادي$"))
async def jepmeme(memejep):
    r = await memejep.get_reply_message(); Jep = r.id if r else None
    url = "https://t.me/AJSJ36/1473"
    await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.امحححح$"))
async def jepmeme(memejep):
    r = await memejep.get_reply_message(); Jep = r.id if r else None
    url = "https://t.me/AJSJ36/1475"
    await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.هلو ابراهيم$"))
async def jepmeme(memejep):
    r = await memejep.get_reply_message(); Jep = r.id if r else None
    url = "https://t.me/AJSJ36/1477"
    await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.هلو حيدر$"))
async def jepmeme(memejep):
    r = await memejep.get_reply_message(); Jep = r.id if r else None
    url = "https://t.me/AJSJ36/1479"
    await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.هلو رضا$"))
async def jepmeme(memejep):
    r = await memejep.get_reply_message(); Jep = r.id if r else None
    url = "https://t.me/AJSJ36/1481"
    await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.هلو مرتضى$"))
async def jepmeme(memejep):
    r = await memejep.get_reply_message(); Jep = r.id if r else None
    url = "https://t.me/AJSJ36/1483"
    await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.هلو عمر$"))
async def jepmeme(memejep):
    r = await memejep.get_reply_message(); Jep = r.id if r else None
    url = "https://t.me/AJSJ36/1485"
    await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.اخوي جفت$"))
async def jepmeme(memejep):
    r = await memejep.get_reply_message(); Jep = r.id if r else None
    url = "https://t.me/AJSJ36/1490"
    await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.والله تمام$"))
async def jepmeme(memejep):
    r = await memejep.get_reply_message(); Jep = r.id if r else None
    url = "https://t.me/AJSJ36/1492"
    await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.اني بخير$"))
async def jepmeme(memejep):
    r = await memejep.get_reply_message(); Jep = r.id if r else None
    url = "https://t.me/AJSJ36/1496"
    await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.الو السلام$"))
async def jepmeme(memejep):
    r = await memejep.get_reply_message(); Jep = r.id if r else None
    url = "https://t.me/AJSJ36/1498"
    await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.انته طيري$"))
async def jepmeme(memejep):
    r = await memejep.get_reply_message(); Jep = r.id if r else None
    url = "https://t.me/AJSJ36/1500"
    await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.وسام احبك$"))
async def jepmeme(memejep):
    r = await memejep.get_reply_message(); Jep = r.id if r else None
    url = "https://t.me/AJSJ36/1530"
    await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()


@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.هلو سجاد$"))
async def jepmeme(memejep):
    r = await memejep.get_reply_message(); Jep = r.id if r else None
    url = "https://t.me/AJSJ36/1408"
    await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.هلو باقر$"))
async def jepmeme(memejep):
    r = await memejep.get_reply_message(); Jep = r.id if r else None
    url = "https://t.me/AJSJ36/1410"
    await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.هلو زيد$"))
async def jepmeme(memejep):
    r = await memejep.get_reply_message(); Jep = r.id if r else None
    url = "https://t.me/AJSJ36/1412"
    await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.شدتسوي$"))
async def jepmeme(memejep):
    r = await memejep.get_reply_message(); Jep = r.id if r else None
    url = "https://t.me/AJSJ36/1419"
    await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.ليش زعلت$"))
async def jepmeme(memejep):
    r = await memejep.get_reply_message(); Jep = r.id if r else None
    url = "https://t.me/AJSJ36/1421"
    await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.شكد عمرك$"))
async def jepmeme(memejep):
    r = await memejep.get_reply_message(); Jep = r.id if r else None
    url = "https://t.me/AJSJ36/1423"
    await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.شكد تحبني$"))
async def jepmeme(memejep):
    r = await memejep.get_reply_message(); Jep = r.id if r else None
    url = "https://t.me/AJSJ36/1425"
    await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.ضفي النيه$"))
async def jepmeme(memejep):
    r = await memejep.get_reply_message(); Jep = r.id if r else None
    url = "https://t.me/AJSJ36/1427"
    await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.ضحكه$"))
async def jepmeme(memejep):
    r = await memejep.get_reply_message(); Jep = r.id if r else None
    url = "https://t.me/AJSJ36/1429"
    await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()


@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.شتريد يسولفون$"))
async def jepmeme(memejep):
    r = await memejep.get_reply_message(); Jep = r.id if r else None
    url = "https://t.me/AJSJ36/1385"
    await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.بنيه تره$"))
async def jepmeme(memejep):
    r = await memejep.get_reply_message(); Jep = r.id if r else None
    url = "https://t.me/AJSJ36/1388"
    await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.لتصير تافه$"))
async def jepmeme(memejep):
    r = await memejep.get_reply_message(); Jep = r.id if r else None
    url = "https://t.me/AJSJ36/1390"
    await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.هلو عبد$"))
async def jepmeme(memejep):
    r = await memejep.get_reply_message(); Jep = r.id if r else None
    url = "https://t.me/AJSJ36/1392"
    await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.هلو علي$"))
async def jepmeme(memejep):
    r = await memejep.get_reply_message(); Jep = r.id if r else None
    url = "https://t.me/AJSJ36/1396"
    await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.هلو حسون$"))
async def jepmeme(memejep):
    r = await memejep.get_reply_message(); Jep = r.id if r else None
    url = "https://t.me/AJSJ36/1398"
    await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.هلو حسين$"))
async def jepmeme(memejep):
    r = await memejep.get_reply_message(); Jep = r.id if r else None
    url = "https://t.me/AJSJ36/1400"
    await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.هلو مصطفى$"))
async def jepmeme(memejep):
    r = await memejep.get_reply_message(); Jep = r.id if r else None
    url = "https://t.me/AJSJ36/1404"
    await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.هلو احمد$"))
async def jepmeme(memejep):
    r = await memejep.get_reply_message(); Jep = r.id if r else None
    url = "https://t.me/AJSJ36/1406"
    await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()


@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.شوف اغار$"))
async def jepmeme(memejep):
    r = await memejep.get_reply_message(); Jep = r.id if r else None
    url = "https://t.me/AJSJ36/1363"
    await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.اغار عليك$"))
async def jepmeme(memejep):
    r = await memejep.get_reply_message(); Jep = r.id if r else None
    url = "https://t.me/AJSJ36/1364"
    await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.غزل$"))
async def jepmeme(memejep):
    r = await memejep.get_reply_message(); Jep = r.id if r else None
    url = "https://t.me/AJSJ36/1366"
    await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()


@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.وصخ$"))
async def jepmeme(memejep):
    r = await memejep.get_reply_message(); Jep = r.id if r else None
    url = "https://t.me/AJSJ36/1350"
    await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.دي$"))
async def jepmeme(memejep):
    r = await memejep.get_reply_message(); Jep = r.id if r else None
    url = "https://t.me/AJSJ36/1352"
    await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.اتسرسح$"))
async def jepmeme(memejep):
    r = await memejep.get_reply_message(); Jep = r.id if r else None
    url = "https://t.me/AJSJ36/1354"
    await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.تحبيني$"))
async def jepmeme(memejep):
    r = await memejep.get_reply_message(); Jep = r.id if r else None
    url = "https://t.me/AJSJ36/1359"
    await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.اموت عليك$"))
async def jepmeme(memejep):
    r = await memejep.get_reply_message(); Jep = r.id if r else None
    url = "https://t.me/AJSJ36/1361"
    await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.ماريد اغلط$"))
async def jepmeme(memejep):
    r = await memejep.get_reply_message(); Jep = r.id if r else None
    url = "https://t.me/AJSJ36/1340"
    await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.ماريد اهينك$"))
async def jepmeme(memejep):
    r = await memejep.get_reply_message(); Jep = r.id if r else None
    url = "https://t.me/AJSJ36/1342"
    await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.ماريد اهينج$"))
async def jepmeme(memejep):
    r = await memejep.get_reply_message(); Jep = r.id if r else None
    url = "https://t.me/AJSJ36/1344"
    await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.انجب$"))
async def jepmeme(memejep):
    r = await memejep.get_reply_message(); Jep = r.id if r else None
    url = "https://t.me/AJSJ36/1346"
    await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.انجبي$"))
async def jepmeme(memejep):
    r = await memejep.get_reply_message(); Jep = r.id if r else None
    url = "https://t.me/AJSJ36/1348"
    await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()


@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.انت لمالك$"))
async def jepmeme(memejep):
    r = await memejep.get_reply_message(); Jep = r.id if r else None
    url = "https://t.me/AJSJ36/1542"
    await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.ارفعني$"))
async def jepmeme(memejep):
    r = await memejep.get_reply_message(); Jep = r.id if r else None
    url = "https://t.me/AJSJ36/1544"
    await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.تصبحون على خير$"))
async def jepmeme(memejep):
    r = await memejep.get_reply_message(); Jep = r.id if r else None
    url = f"https://t.me/AJSJ36/1546"
    await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.اجت فكره$"))
async def jepmeme(memejep):
    r = await memejep.get_reply_message(); Jep = r.id if r else None
    url = f"https://t.me/AJSJ36/1558"
    await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.تموت عل بنات$"))
async def jepmeme(memejep):
    r = await memejep.get_reply_message(); Jep = r.id if r else None
    url = f"https://t.me/AJSJ36/1560"
    await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.هلو مسلم$"))
async def jepmeme(memejep):
    r = await memejep.get_reply_message(); Jep = r.id if r else None
    url = f"https://t.me/AJSJ36/1572"
    await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.السلام$"))
async def jepmeme(memejep):
    r = await memejep.get_reply_message(); Jep = r.id if r else None
    url = f"https://t.me/AJSJ36/1650"
    await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.ممكن نتعرف$"))
async def jepmeme(memejep):
    r = await memejep.get_reply_message(); Jep = r.id if r else None
    url = f"https://t.me/AJSJ36/1652"
    await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.اني زينه$"))
async def jepmeme(memejep):
    r = await memejep.get_reply_message(); Jep = r.id if r else None
    url = f"https://t.me/AJSJ36/1656"
    await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.دز صورتك$"))
async def jepmeme(memejep):
    r = await memejep.get_reply_message(); Jep = r.id if r else None
    url = f"https://t.me/AJSJ36/1658"
    await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.هاي انته$"))
async def jepmeme(memejep):
    r = await memejep.get_reply_message(); Jep = r.id if r else None
    url = f"https://t.me/AJSJ36/1660"
    await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.من وين$"))
async def jepmeme(memejep):
    r = await memejep.get_reply_message(); Jep = r.id if r else None
    url = f"https://t.me/AJSJ36/1662"
    await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()





@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.اشكد عمرك$"))
async def jepmeme(memejep):
    r = await memejep.get_reply_message(); Jep = r.id if r else None
    url = f"https://t.me/AJSJ36/1664"
    await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.انت مرتبط$"))
async def jepmeme(memejep):
    r = await memejep.get_reply_message(); Jep = r.id if r else None
    url = f"https://t.me/AJSJ36/1666"
    await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.من امت مرتبط$"))
async def jepmeme(memejep):
    r = await memejep.get_reply_message(); Jep = r.id if r else None
    url = f"https://t.me/AJSJ36/1668"
    await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.ليش مامرتبط$"))
async def jepmeme(memejep):
    r = await memejep.get_reply_message(); Jep = r.id if r else None
    url = f"https://t.me/AJSJ36/1670"
    await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.نصير اصدقاء$"))
async def jepmeme(memejep):
    r = await memejep.get_reply_message(); Jep = r.id if r else None
    url = f"https://t.me/AJSJ36/1672"
    await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.تشرفت$"))
async def jepmeme(memejep):
    r = await memejep.get_reply_message(); Jep = r.id if r else None
    url = f"https://t.me/AJSJ36/1674"
    await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.لحضه$"))
async def jepmeme(memejep):
    r = await memejep.get_reply_message(); Jep = r.id if r else None
    url = f"https://t.me/AJSJ36/1686"
    await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.مشغول$"))
async def jepmeme(memejep):
    r = await memejep.get_reply_message(); Jep = r.id if r else None
    url = f"https://t.me/AJSJ36/1688"
    await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.مترد بسرعه$"))
async def jepmeme(memejep):
    r = await memejep.get_reply_message(); Jep = r.id if r else None
    url = f"https://t.me/AJSJ36/1690"
    await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.الجو حار$"))
async def jepmeme(memejep):
    r = await memejep.get_reply_message(); Jep = r.id if r else None
    url = f"https://t.me/AJSJ36/1692"
    await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()







@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.شخبارك$"))
async def jepmeme(memejep):
    r = await memejep.get_reply_message(); Jep = r.id if r else None
    url = f"https://t.me/AJSJ36/1695"
    await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.تابع مردوده$"))
async def jepmeme(memejep):
    r = await memejep.get_reply_message(); Jep = r.id if r else None
    url = f"https://t.me/AJSJ36/1701"
    await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.اسمي ايه$"))
async def jepmeme(memejep):
    r = await memejep.get_reply_message(); Jep = r.id if r else None
    url = f"https://t.me/AJSJ36/1706"
    await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.ضحكتني$"))
async def jepmeme(memejep):
    r = await memejep.get_reply_message(); Jep = r.id if r else None
    url = f"https://t.me/AJSJ36/1708"
    await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.جوعانه$"))
async def jepmeme(memejep):
    r = await memejep.get_reply_message(); Jep = r.id if r else None
    url = f"https://t.me/AJSJ36/1710"
    await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.امي صاحتني$"))
async def jepmeme(memejep):
    r = await memejep.get_reply_message(); Jep = r.id if r else None
    url = f"https://t.me/AJSJ36/1712"
    await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.بابا صاحني$"))
async def jepmeme(memejep):
    r = await memejep.get_reply_message(); Jep = r.id if r else None
    url = f"https://t.me/AJSJ36/1714"
    await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.اريد اتغده$"))
async def jepmeme(memejep):
    r = await memejep.get_reply_message(); Jep = r.id if r else None
    url = f"https://t.me/AJSJ36/1716"
    await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.هسه كعدو اهلي$"))
async def jepmeme(memejep):
    r = await memejep.get_reply_message(); Jep = r.id if r else None
    url = f"https://t.me/AJSJ36/1718"
    await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.صباحو$"))
async def jepmeme(memejep):
    r = await memejep.get_reply_message(); Jep = r.id if r else None
    url = f"https://t.me/AJSJ36/1729"
    await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()









@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.سلام عليكم$"))
async def jepmeme(memejep):
    r = await memejep.get_reply_message(); Jep = r.id if r else None
    url = f"https://t.me/AJSJ36/1731"
    await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.عليكم السلام$"))
async def jepmeme(memejep):
    r = await memejep.get_reply_message(); Jep = r.id if r else None
    url = f"https://t.me/AJSJ36/1733"
    await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.عليكم السلام تفضلي$"))
async def jepmeme(memejep):
    r = await memejep.get_reply_message(); Jep = r.id if r else None
    url = f"https://t.me/AJSJ36/1735"
    await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.احبك علي$"))
async def jepmeme(memejep):
    r = await memejep.get_reply_message(); Jep = r.id if r else None
    url = f"https://t.me/AJSJ36/1739"
    await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.احبك حسين$"))
async def jepmeme(memejep):
    r = await memejep.get_reply_message(); Jep = r.id if r else None
    url = f"https://t.me/AJSJ36/1741"
    await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.احبك عباس$"))
async def jepmeme(memejep):
    r = await memejep.get_reply_message(); Jep = r.id if r else None
    url = f"https://t.me/AJSJ36/1743"
    await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.مشتاقتلك$"))
async def jepmeme(memejep):
    r = await memejep.get_reply_message(); Jep = r.id if r else None
    url = f"https://t.me/AJSJ36/1745"
    await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.نسيتني$"))
async def jepmeme(memejep):
    r = await memejep.get_reply_message(); Jep = r.id if r else None
    url = f"https://t.me/AJSJ36/1747"
    await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.ليش تحظر$"))
async def jepmeme(memejep):
    r = await memejep.get_reply_message(); Jep = r.id if r else None
    url = f"https://t.me/AJSJ36/1749"
    await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.احبك اورهان$"))
async def jepmeme(memejep):
    r = await memejep.get_reply_message(); Jep = r.id if r else None
    url = f""
    await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()








@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.احبك2$"))
async def jepmeme(memejep):
    r = await memejep.get_reply_message(); Jep = r.id if r else None
    url = f"https://t.me/AJSJ36/1774"
    await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.عبودي$"))
async def jepmeme(memejep):
    r = await memejep.get_reply_message(); Jep = r.id if r else None
    url = f"https://t.me/AJSJ36/1776"
    await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.ابعت هديه$"))
async def jepmeme(memejep):
    r = await memejep.get_reply_message(); Jep = r.id if r else None
    url = f"https://t.me/AJSJ36/1778"
    await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.بهاء احبك$"))
async def jepmeme(memejep):
    r = await memejep.get_reply_message(); Jep = r.id if r else None
    url = f"https://t.me/AJSJ36/1782"
    await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.دز رصيد اونسك$"))
async def jepmeme(memejep):
    r = await memejep.get_reply_message(); Jep = r.id if r else None
    url = f"https://t.me/AJSJ36/1785"
    await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.فوك ما تعبانه$"))
async def jepmeme(memejep):
    r = await memejep.get_reply_message(); Jep = r.id if r else None
    url = f"https://t.me/AJSJ36/1789"
    await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.ثقه$"))
async def jepmeme(memejep):
    r = await memejep.get_reply_message(); Jep = r.id if r else None
    url = f"https://t.me/AJSJ36/1790"
    await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.باي تعبت ممستفاده$"))
async def jepmeme(memejep):
    r = await memejep.get_reply_message(); Jep = r.id if r else None
    url = f"https://t.me/AJSJ36/1792"
    await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.احبك احمد$"))
async def jepmeme(memejep):
    r = await memejep.get_reply_message(); Jep = r.id if r else None
    url = f"https://t.me/AJSJ36/1794"
    await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.مشايف حلوين$"))
async def jepmeme(memejep):
    r = await memejep.get_reply_message(); Jep = r.id if r else None
    url = f"https://t.me/AJSJ36/1833"
    await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()








@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.طفي الكامره$"))
async def jepmeme(memejep):
    r = await memejep.get_reply_message(); Jep = r.id if r else None
    url = f"https://t.me/AJSJ36/1834"
    await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.زلمه جيس$"))
async def jepmeme(memejep):
    r = await memejep.get_reply_message(); Jep = r.id if r else None
    url = f"https://t.me/AJSJ36/1835"
    await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.انجب لدوخني$"))
async def jepmeme(memejep):
    r = await memejep.get_reply_message(); Jep = r.id if r else None
    url = f"https://t.me/AJSJ36/1836"
    await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.اخجل اني$"))
async def jepmeme(memejep):
    r = await memejep.get_reply_message(); Jep = r.id if r else None
    url = f"https://t.me/AJSJ36/1837"
    await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.شنو هذه$"))
async def jepmeme(memejep):
    r = await memejep.get_reply_message(); Jep = r.id if r else None
    url = f"https://t.me/AJSJ36/1838"
    await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.اتصنع$"))
async def jepmeme(memejep):
    r = await memejep.get_reply_message(); Jep = r.id if r else None
    url = f"https://t.me/AJSJ36/1839"
    await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.ماعرف شحجي$"))
async def jepmeme(memejep):
    r = await memejep.get_reply_message(); Jep = r.id if r else None
    url = f"https://t.me/AJSJ36/1840"
    await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.حشوره$"))
async def jepmeme(memejep):
    r = await memejep.get_reply_message(); Jep = r.id if r else None
    url = f"https://t.me/AJSJ36/1841"
    await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.تحب الاندومي$"))
async def jepmeme(memejep):
    r = await memejep.get_reply_message(); Jep = r.id if r else None
    url = f"https://t.me/AJSJ36/1842"
    await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.اكوله احبك يكلي شلابسه$"))
async def jepmeme(memejep):
    r = await memejep.get_reply_message(); Jep = r.id if r else None
    url = f"https://t.me/AJSJ36/1843"
    await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()







@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.اوي دروحي$"))
async def jepmeme(memejep):
    r = await memejep.get_reply_message(); Jep = r.id if r else None
    url = f"https://t.me/AJSJ36/1844"
    await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.كتمتك$"))
async def jepmeme(memejep):
    r = await memejep.get_reply_message(); Jep = r.id if r else None
    url = f"https://t.me/AJSJ36/1845"
    await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.هاي شبيك$"))
async def jepmeme(memejep):
    r = await memejep.get_reply_message(); Jep = r.id if r else None
    url = f"https://t.me/AJSJ36/1846"
    await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.لكلاوات$"))
async def jepmeme(memejep):
    r = await memejep.get_reply_message(); Jep = r.id if r else None
    url = f"https://t.me/AJSJ36/1847"
    await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.هاي ليش$"))
async def jepmeme(memejep):
    r = await memejep.get_reply_message(); Jep = r.id if r else None
    url = f"https://t.me/AJSJ36/1848"
    await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.هلو شلونك$"))
async def jepmeme(memejep):
    r = await memejep.get_reply_message(); Jep = r.id if r else None
    url = f"https://t.me/AJSJ36/1873"
    await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.عادي نتعرف$"))
async def jepmeme(memejep):
    r = await memejep.get_reply_message(); Jep = r.id if r else None
    url = f"https://t.me/AJSJ36/1875"
    await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.ااسلام عليكم$"))
async def jepmeme(memejep):
    r = await memejep.get_reply_message(); Jep = r.id if r else None
    url = f"https://t.me/AJSJ36/1877"
    await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.شلونك2$"))
async def jepmeme(memejep):
    r = await memejep.get_reply_message(); Jep = r.id if r else None
    url = f"https://t.me/AJSJ36/1879"
    await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.اني سينكل$"))
async def jepmeme(memejep):
    r = await memejep.get_reply_message(); Jep = r.id if r else None
    url = f"https://t.me/AJSJ36/1881"
    await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()







@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.اني حلوه$"))
async def jepmeme(memejep):
    r = await memejep.get_reply_message(); Jep = r.id if r else None
    url = f"https://t.me/AJSJ36/1883"
    await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.اهلي يمي$"))
async def jepmeme(memejep):
    r = await memejep.get_reply_message(); Jep = r.id if r else None
    url = f"https://t.me/AJSJ36/1887"
    await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.مكدر$"))
async def jepmeme(memejep):
    r = await memejep.get_reply_message(); Jep = r.id if r else None
    url = f"https://t.me/AJSJ36/1889"
    await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.اهلي ميعرفون$"))
async def jepmeme(memejep):
    r = await memejep.get_reply_message(); Jep = r.id if r else None
    url = f"https://t.me/AJSJ36/1891"
    await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.يله تنام$"))
async def jepmeme(memejep):
    r = await memejep.get_reply_message(); Jep = r.id if r else None
    url = f"https://t.me/AJSJ36/1917"
    await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.من وين$"))
async def jepmeme(memejep):
    r = await memejep.get_reply_message(); Jep = r.id if r else None
    url = f"https://t.me/AJSJ36/1929"
    await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.شسمك$"))
async def jepmeme(memejep):
    r = await memejep.get_reply_message(); Jep = r.id if r else None
    url = f"https://t.me/AJSJ36/1931"
    await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.تشرفت2$"))
async def jepmeme(memejep):
    r = await memejep.get_reply_message(); Jep = r.id if r else None
    url = f"https://t.me/AJSJ36/1935"
    await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.ببا منطقه$"))
async def jepmeme(memejep):
    r = await memejep.get_reply_message(); Jep = r.id if r else None
    url = f"https://t.me/AJSJ36/1937"
    await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.مرتبط$"))
async def jepmeme(memejep):
    r = await memejep.get_reply_message(); Jep = r.id if r else None
    url = f"https://t.me/AJSJ36/1939"
    await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()







@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.ما مرتبطه$"))
async def jepmeme(memejep):
    r = await memejep.get_reply_message(); Jep = r.id if r else None
    url = f"https://t.me/AJSJ36/1941"
    await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.ولا مره$"))
async def jepmeme(memejep):
    r = await memejep.get_reply_message(); Jep = r.id if r else None
    url = f"https://t.me/AJSJ36/1943"
    await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.كم مره حبيت$"))
async def jepmeme(memejep):
    r = await memejep.get_reply_message(); Jep = r.id if r else None
    url = f"https://t.me/AJSJ36/1945"
    await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.نت ماعندي$"))
async def jepmeme(memejep):
    r = await memejep.get_reply_message(); Jep = r.id if r else None
    url = f"https://t.me/AJSJ36/1947"
    await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.طلب$"))
async def jepmeme(memejep):
    r = await memejep.get_reply_message(); Jep = r.id if r else None
    url = f"https://t.me/AJSJ36/1951"
    await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.رشق انستا$"))
async def jepmeme(memejep):
    r = await memejep.get_reply_message(); Jep = r.id if r else None
    url = f"https://t.me/AJSJ36/1956"
    await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.انت تحبني$"))
async def jepmeme(memejep):
    r = await memejep.get_reply_message(); Jep = r.id if r else None
    url = f"https://t.me/AJSJ36/1959"
    await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.اني احبك$"))
async def jepmeme(memejep):
    r = await memejep.get_reply_message(); Jep = r.id if r else None
    url = f"https://t.me/AJSJ36/1961"
    await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.كم اخ عندك$"))
async def jepmeme(memejep):
    r = await memejep.get_reply_message(); Jep = r.id if r else None
    url = f"https://t.me/AJSJ36/1963"
    await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.وحيده لهلي$"))
async def jepmeme(memejep):
    r = await memejep.get_reply_message(); Jep = r.id if r else None
    url = f"https://t.me/AJSJ36/1967"
    await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()






@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.مخنوكه$"))
async def jepmeme(memejep):
    r = await memejep.get_reply_message(); Jep = r.id if r else None
    url = f"https://t.me/AJSJ36/1969"
    await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.بيت عمي$"))
async def jepmeme(memejep):
    r = await memejep.get_reply_message(); Jep = r.id if r else None
    url = f"https://t.me/AJSJ36/1971"
    await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.بيت خالتي$"))
async def jepmeme(memejep):
    r = await memejep.get_reply_message(); Jep = r.id if r else None
    url = f"https://t.me/AJSJ36/1973"
    await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.بيت عمتي$"))
async def jepmeme(memejep):
    r = await memejep.get_reply_message(); Jep = r.id if r else None
    url = f"https://t.me/AJSJ36/1975"
    await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.رايحه للطبيب$"))
async def jepmeme(memejep):
    r = await memejep.get_reply_message(); Jep = r.id if r else None
    url = f"https://t.me/AJSJ36/1977"
    await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.عادي نرتبط$"))
async def jepmeme(memejep):
    r = await memejep.get_reply_message(); Jep = r.id if r else None
    url = f"https://t.me/AJSJ36/1979"
    await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.شوي وجي$"))
async def jepmeme(memejep):
    r = await memejep.get_reply_message(); Jep = r.id if r else None
    url = f"https://t.me/AJSJ36/1981"
    await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.يلا اجيت$"))
async def jepmeme(memejep):
    r = await memejep.get_reply_message(); Jep = r.id if r else None
    url = f"https://t.me/AJSJ36/1983"
    await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.اخمطج$"))
async def jepmeme(memejep):
    r = await memejep.get_reply_message(); Jep = r.id if r else None
    url = f"https://t.me/AJSJ36/2049"
    await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.اني حساسه$"))
async def jepmeme(memejep):
    r = await memejep.get_reply_message(); Jep = r.id if r else None
    url = f"https://t.me/AJSJ36/2053"
    await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()






@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.متغيير عليه$"))
async def jepmeme(memejep):
    r = await memejep.get_reply_message(); Jep = r.id if r else None
    url = f"https://t.me/AJSJ36/2055"
    await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.كيفك حبيبي$"))
async def jepmeme(memejep):
    r = await memejep.get_reply_message(); Jep = r.id if r else None
    url = f"https://t.me/AJSJ36/2057"
    await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.هلا بروحي$"))
async def jepmeme(memejep):
    r = await memejep.get_reply_message(); Jep = r.id if r else None
    url = f"https://t.me/AJSJ36/2059"
    await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.هلو شلونك$"))
async def jepmeme(memejep):
    r = await memejep.get_reply_message(); Jep = r.id if r else None
    url = f"https://t.me/AJSJ36/2061"
    await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.صور خاصك$"))
async def jepmeme(memejep):
    r = await memejep.get_reply_message(); Jep = r.id if r else None
    url = f"https://t.me/AJSJ36/2064"
    await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.سلم على امك$"))
async def jepmeme(memejep):
    r = await memejep.get_reply_message(); Jep = r.id if r else None
    url = f"https://t.me/AJSJ36/2066"
    await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.شنو مصدك$"))
async def jepmeme(memejep):
    r = await memejep.get_reply_message(); Jep = r.id if r else None
    url = f"https://t.me/AJSJ36/2193"
    await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.رفعني$"))
async def jepmeme(memejep):
    r = await memejep.get_reply_message(); Jep = r.id if r else None
    url = f"https://t.me/AJSJ36/2195"
    await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.مالك5$"))
async def jepmeme(memejep):
    r = await memejep.get_reply_message(); Jep = r.id if r else None
    url = f"https://t.me/AJSJ36/2197"
    await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.وكت ليعجبني ادز$"))
async def jepmeme(memejep):
    r = await memejep.get_reply_message(); Jep = r.id if r else None
    url = f"https://t.me/AJSJ36/2199"
    await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()





@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.اني اتصل$"))
async def jepmeme(memejep):
    r = await memejep.get_reply_message(); Jep = r.id if r else None
    url = f"https://t.me/AJSJ36/2203"
    await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.رتبه$"))
async def jepmeme(memejep):
    r = await memejep.get_reply_message(); Jep = r.id if r else None
    url = f"https://t.me/AJSJ36/2205"
    await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.غزل7$"))
async def jepmeme(memejep):
    r = await memejep.get_reply_message(); Jep = r.id if r else None
    url = f"https://t.me/AJSJ36/2240"
    await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.ها دوده$"))
async def jepmeme(memejep):
    r = await memejep.get_reply_message(); Jep = r.id if r else None
    url = f"https://t.me/AJSJ36/2258"
    await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.كس امك$"))
async def jepmeme(memejep):
    r = await memejep.get_reply_message(); Jep = r.id if r else None
    url = f"https://t.me/AJSJ36/2260"
    await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.تنيجين$"))
async def jepmeme(memejep):
    r = await memejep.get_reply_message(); Jep = r.id if r else None
    url = f"https://t.me/AJSJ36/2262"
    await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.تنيج$"))
async def jepmeme(memejep):
    r = await memejep.get_reply_message(); Jep = r.id if r else None
    url = f"https://t.me/AJSJ36/2264"
    await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.كس امج$"))
async def jepmeme(memejep):
    r = await memejep.get_reply_message(); Jep = r.id if r else None
    url = f"https://t.me/AJSJ36/2266"
    await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.دي فرخ$"))
async def jepmeme(memejep):
    r = await memejep.get_reply_message(); Jep = r.id if r else None
    url = f"https://t.me/AJSJ36/2268"
    await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.كحبه$"))
async def jepmeme(memejep):
    r = await memejep.get_reply_message(); Jep = r.id if r else None
    url = f"https://t.me/AJSJ36/2270"
    await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()







@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.ابلع بلوك$"))
async def jepmeme(memejep):
    r = await memejep.get_reply_message(); Jep = r.id if r else None
    url = f"https://t.me/AJSJ36/2281"
    await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.انت الحب$"))
async def jepmeme(memejep):
    r = await memejep.get_reply_message(); Jep = r.id if r else None
    url = f"https://t.me/AJSJ36/2283"
    await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.انت الاول$"))
async def jepmeme(memejep):
    r = await memejep.get_reply_message(); Jep = r.id if r else None
    url = f"https://t.me/AJSJ36/2285"
    await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.وين وصلت$"))
async def jepmeme(memejep):
    r = await memejep.get_reply_message(); Jep = r.id if r else None
    url = f"https://t.me/AJSJ36/2301"
    await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.ابد لتحاول$"))
async def jepmeme(memejep):
    r = await memejep.get_reply_message(); Jep = r.id if r else None
    url = f"https://t.me/AJSJ36/2313"
    await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.انت تدبرها$"))
async def jepmeme(memejep):
    r = await memejep.get_reply_message(); Jep = r.id if r else None
    url = f"https://t.me/AJSJ36/2319"
    await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.انت قافل$"))
async def jepmeme(memejep):
    r = await memejep.get_reply_message(); Jep = r.id if r else None
    url = f"https://t.me/AJSJ36/2323"
    await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.اعشقك$"))
async def jepmeme(memejep):
    r = await memejep.get_reply_message(); Jep = r.id if r else None
    url = f"https://t.me/AJSJ36/2327"
    await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.اسفا$"))
async def jepmeme(memejep):
    r = await memejep.get_reply_message(); Jep = r.id if r else None
    url = f"https://t.me/AJSJ36/2329"
    await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.اريد اشوفك$"))
async def jepmeme(memejep):
    r = await memejep.get_reply_message(); Jep = r.id if r else None
    url = f"https://t.me/AJSJ36/2331"
    await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()








@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.ليش مصدك$"))
async def jepmeme(memejep):
    r = await memejep.get_reply_message(); Jep = r.id if r else None
    url = f"https://t.me/AJSJ36/2426"
    await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.غنيلي$"))
async def jepmeme(memejep):
    r = await memejep.get_reply_message(); Jep = r.id if r else None
    url = f"https://t.me/AJSJ36/2426"
    await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.كوه دزيت$"))
async def jepmeme(memejep):
    r = await memejep.get_reply_message(); Jep = r.id if r else None
    url = f"https://t.me/AJSJ36/2426"
    await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.حروح اسبح$"))
async def jepmeme(memejep):
    r = await memejep.get_reply_message(); Jep = r.id if r else None
    url = f"https://t.me/AJSJ36/2486"
    await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.اشكرك$"))
async def jepmeme(memejep):
    r = await memejep.get_reply_message(); Jep = r.id if r else None
    url = f"https://t.me/AJSJ36/2513"
    await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.نورت$"))
async def jepmeme(memejep):
    r = await memejep.get_reply_message(); Jep = r.id if r else None
    url = f"https://t.me/AJSJ36/2515"
    await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.مافهم عليج$"))
async def jepmeme(memejep):
    r = await memejep.get_reply_message(); Jep = r.id if r else None
    url = f"https://t.me/AJSJ36/2519"
    await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.جهز رصيدك$"))
async def jepmeme(memejep):
    r = await memejep.get_reply_message(); Jep = r.id if r else None
    url = f"https://t.me/AJSJ36/2521"
    await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.جيب رصيد$"))
async def jepmeme(memejep):
    r = await memejep.get_reply_message(); Jep = r.id if r else None
    url = f"https://t.me/AJSJ36/2523"
    await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.العفو كلبي$"))
async def jepmeme(memejep):
    r = await memejep.get_reply_message(); Jep = r.id if r else None
    url = f"https://t.me/AJSJ36/2527"
    await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()
###دجله
@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.اريد اروح$"))
async def jepmeme(memejep):
    r = await memejep.get_reply_message(); Jep = r.id if r else None
    url = f"https://t.me/yyegksgfdg/1113"
    await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.انجب2$"))
async def jepmeme(memejep):
    r = await memejep.get_reply_message(); Jep = r.id if r else None
    url = f"https://t.me/yyegksgfdg/1114"
    await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()
@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.انجبي2$"))
async def jepmeme(memejep):
    r = await memejep.get_reply_message(); Jep = r.id if r else None
    url = f"https://t.me/yyegksgfdg/1115"
    await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()
@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.شسمك2$"))
async def jepmeme(memejep):
    r = await memejep.get_reply_message(); Jep = r.id if r else None
    url = f"https://t.me/yyegksgfdg/1116"
    await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()




###
@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.من تحول$"))
async def jepmeme(memejep):
    r = await memejep.get_reply_message(); Jep = r.id if r else None
    url = f"https://t.me/bxhbvtujxsrfx/4"
    await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()
@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.على شنو$"))
async def jepmeme(memejep):
    r = await memejep.get_reply_message(); Jep = r.id if r else None
    url = f"https://t.me/bxhbvtujxsrfx/6"
    await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.هلا تفضل$"))
async def jepmeme(memejep):
    r = await memejep.get_reply_message(); Jep = r.id if r else None
    url = f"https://t.me/bxhbvtujxsrfx/8"
    await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()
@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.هلا شلونك$"))
async def jepmeme(memejep):
    r = await memejep.get_reply_message(); Jep = r.id if r else None
    url = f"https://t.me/bxhbvtujxsrfx/10"
    await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()
@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.تمام الحمدلله$"))
async def jepmeme(memejep):
    r = await memejep.get_reply_message(); Jep = r.id if r else None
    url = f"https://t.me/bxhbvtujxsrfx/13"
    await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()
@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.واني شعليه$"))
async def jepmeme(memejep):
    r = await memejep.get_reply_message(); Jep = r.id if r else None
    url = f"https://t.me/bxhbvtujxsrfx/19"
    await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()
@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.حول وريحك$"))
async def jepmeme(memejep):
    r = await memejep.get_reply_message(); Jep = r.id if r else None
    url = f"https://t.me/bxhbvtujxsrfx/15"
    await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()
@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.مواصفات$"))
async def jepmeme(memejep):
    r = await memejep.get_reply_message(); Jep = r.id if r else None
    url = f"https://t.me/bxhbvtujxsrfx/15"
    await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()
@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.تمامم$"))
async def jepmeme(memejep):
    r = await memejep.get_reply_message(); Jep = r.id if r else None
    url = f"https://t.me/bxhbvtujxsrfx/20"
    await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()
@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.وين مكانك$"))
async def jepmeme(memejep):
    r = await memejep.get_reply_message(); Jep = r.id if r else None
    url = f"https://t.me/bxhbvtujxsrfx/22"
    await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()
@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.عمولتي10$"))
async def jepmeme(memejep):
    r = await memejep.get_reply_message(); Jep = r.id if r else None
    url = f"https://t.me/bxhbvtujxsrfx/24"
    await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()
@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.اه مشتهيه$"))
async def jepmeme(memejep):
    r = await memejep.get_reply_message(); Jep = r.id if r else None
    url = f"https://t.me/bxhbvtujxsrfx/26"
    await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()
@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.ماعندك ثقه$"))
async def jepmeme(memejep):
    r = await memejep.get_reply_message(); Jep = r.id if r else None
    url = f"https://t.me/bxhbvtujxsrfx/28"
    await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.مو بكيفك$"))
async def jepmeme(memejep):
    r = await memejep.get_reply_message(); Jep = r.id if r else None
    url = f"https://t.me/bxhbvtujxsrfx/31"
    await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()
@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.جاد لو لا$"))
async def jepmeme(memejep):
    r = await memejep.get_reply_message(); Jep = r.id if r else None
    url = f"https://t.me/bxhbvtujxsrfx/32"
    await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()
@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.للثقه$"))
async def jepmeme(memejep):
    r = await memejep.get_reply_message(); Jep = r.id if r else None
    url = f"https://t.me/bxhbvtujxsrfx/36"
    await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()
@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.لاحضرك$"))
async def jepmeme(memejep):
    r = await memejep.get_reply_message(); Jep = r.id if r else None
    url = f"https://t.me/bxhbvtujxsrfx/38"
    await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()
@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.مالتي وردي$"))
async def jepmeme(memejep):
    r = await memejep.get_reply_message(); Jep = r.id if r else None
    url = f"https://t.me/bxhbvtujxsrfx/41"
    await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()
@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.اخابر وجي$"))
async def jepmeme(memejep):
    r = await memejep.get_reply_message(); Jep = r.id if r else None
    url = f"https://t.me/bxhbvtujxsrfx/43"
    await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()
@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.كل لمحافضات$"))
async def jepmeme(memejep):
    r = await memejep.get_reply_message(); Jep = r.id if r else None
    url = f"https://t.me/bxhbvtujxsrfx/44"
    await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()
@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.اني بنت$"))
async def jepmeme(memejep):
    r = await memejep.get_reply_message(); Jep = r.id if r else None
    url = f"https://t.me/bxhbvtujxsrfx/46"
    await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()
@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.تبياته لو ساعات$"))
async def jepmeme(memejep):
    r = await memejep.get_reply_message(); Jep = r.id if r else None
    url = f"https://t.me/bxhbvtujxsrfx/50"
    await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()
@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.كام10 صوت5$"))
async def jepmeme(memejep):
    r = await memejep.get_reply_message(); Jep = r.id if r else None
    url = f"https://t.me/bxhbvtujxsrfx/52"
    await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()
@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.سعر تبياته$"))
async def jepmeme(memejep):
    r = await memejep.get_reply_message(); Jep = r.id if r else None
    url = f"https://t.me/bxhbvtujxsrfx/61"
    await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()
@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.سعر ساعه$"))
async def jepmeme(memejep):
    r = await memejep.get_reply_message(); Jep = r.id if r else None
    url = f"https://t.me/bxhbvtujxsrfx/64"
    await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()
@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.مكان$"))
async def jepmeme(memejep):
    r = await memejep.get_reply_message(); Jep = r.id if r else None
    url = f"https://t.me/bxhbvtujxsrfx/67"
    await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()
@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.اعمار$"))
async def jepmeme(memejep):
    r = await memejep.get_reply_message(); Jep = r.id if r else None
    url = f"https://t.me/bxhbvtujxsrfx/70"
    await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.خره2$"))
async def jepmeme(memejep):
    r = await memejep.get_reply_message(); Jep = r.id if r else None
    url = f"https://t.me/yyegksgfdg/1391"
    await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
    await memejep.delete()


@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.مرتبط2$"))
async def jepmeme(memejep):
  r = await memejep.get_reply_message(); Jep = r.id if r else None
  url = f"https://t.me/yyegksgfdg/1118"
  await hellas.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()



@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.لويش مامرتبط$"))
async def jepmeme(memejep):
  r = await memejep.get_reply_message(); Jep = r.id if r else None
  url = f"https://t.me/yyegksgfdg/1119"
  await hellas.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.لحضه2$"))
async def jepmeme(memejep):
  r = await memejep.get_reply_message(); Jep = r.id if r else None
  url = f"https://t.me/yyegksgfdg/1120"
  await hellas.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()



@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.عومري$"))
async def jepmeme(memejep):
  r = await memejep.get_reply_message(); Jep = r.id if r else None
  url = f"https://t.me/yyegksgfdg/1146"
  await hellas.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()


@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.احبك2$"))
async def jepmeme(memejep):
  r = await memejep.get_reply_message(); Jep = r.id if r else None
  url = f"https://t.me/yyegksgfdg/1166"
  await hellas.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()





@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.تفاعل قليل$"))
async def jepmeme(memejep):
  r = await memejep.get_reply_message(); Jep = r.id if r else None
  url = f"https://t.me/yyegksgfdg/1172"
  await hellas.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()



@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.احبج2$"))
async def jepmeme(memejep):
  r = await memejep.get_reply_message(); Jep = r.id if r else None
  url = f"https://t.me/yyegksgfdg/1266"
  await hellas.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()



@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.اموت بيك$"))
async def jepmeme(memejep):
  r = await memejep.get_reply_message(); Jep = r.id if r else None
  url = f"https://t.me/yyegksgfdg/1268"
  await hellas.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()



@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.اموت بيج$"))
async def jepmeme(memejep):
  r = await memejep.get_reply_message(); Jep = r.id if r else None
  url = f"https://t.me/yyegksgfdg/1269"
  await hellas.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()




@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.حياتي2$"))
async def jepmeme(memejep):
  r = await memejep.get_reply_message(); Jep = r.id if r else None
  url = f"https://t.me/yyegksgfdg/1270"
  await hellas.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()



@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.رويحتي$"))
async def jepmeme(memejep):
  r = await memejep.get_reply_message(); Jep = r.id if r else None
  url = f"https://t.me/yyegksgfdg/1271"
  await hellas.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()


@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.شلونك2$"))
async def jepmeme(memejep):
  r = await memejep.get_reply_message(); Jep = r.id if r else None
  url = f"https://t.me/yyegksgfdg/1272"
  await hellas.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()



@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.شلونج2$"))
async def jepmeme(memejep):
  r = await memejep.get_reply_message(); Jep = r.id if r else None
  url = f"https://t.me/yyegksgfdg/1273"
  await hellas.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()



@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.شخباركم2$"))
async def jepmeme(memejep):
  r = await memejep.get_reply_message(); Jep = r.id if r else None
  url = f"https://t.me/yyegksgfdg/1274"
  await hellas.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()


@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.بخير اذا انت$"))
async def jepmeme(memejep):
  r = await memejep.get_reply_message(); Jep = r.id if r else None
  url = f"https://t.me/yyegksgfdg/1275"
  await hellas.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()


@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.شكو ماكو$"))
async def jepmeme(memejep):
  r = await memejep.get_reply_message(); Jep = r.id if r else None
  url = f"https://t.me/yyegksgfdg/1276"
  await hellas.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()


@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.بيش$"))
async def jepmeme(memejep):
  r = await memejep.get_reply_message(); Jep = r.id if r else None
  url = f"https://t.me/yyegksgfdg/1277"
  await hellas.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.بيش$"))
async def jepmeme(memejep):
  r = await memejep.get_reply_message(); Jep = r.id if r else None
  url = f"https://t.me/yyegksgfdg/1278"
  await hellas.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.بصره$"))
async def jepmeme(memejep):
  r = await memejep.get_reply_message(); Jep = r.id if r else None
  url = f"https://t.me/yyegksgfdg/1279"
  await hellas.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.بغداد$"))
async def jepmeme(memejep):
  r = await memejep.get_reply_message(); Jep = r.id if r else None
  url = f"https://t.me/yyegksgfdg/1280"
  await hellas.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.ديالى$"))
async def jepmeme(memejep):
  r = await memejep.get_reply_message(); Jep = r.id if r else None
  url = f"https://t.me/yyegksgfdg/1281"
  await hellas.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.لحله$"))
async def jepmeme(memejep):
  r = await memejep.get_reply_message(); Jep = r.id if r else None
  url = f"https://t.me/yyegksgfdg/1282"
  await hellas.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.اربيل$"))
async def jepmeme(memejep):
  r = await memejep.get_reply_message(); Jep = r.id if r else None
  url = f"https://t.me/yyegksgfdg/1283"
  await hellas.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.كوت$"))
async def jepmeme(memejep):
  r = await memejep.get_reply_message(); Jep = r.id if r else None
  url = f"https://t.me/yyegksgfdg/1284"
  await hellas.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.سامراء$"))
async def jepmeme(memejep):
  r = await memejep.get_reply_message(); Jep = r.id if r else None
  url = f"https://t.me/yyegksgfdg/1285"
  await hellas.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.كوت2$"))
async def jepmeme(memejep):
  r = await memejep.get_reply_message(); Jep = r.id if r else None
  url = f"https://t.me/yyegksgfdg/1286"
  await hellas.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.نورت2$"))
async def jepmeme(memejep):
  r = await memejep.get_reply_message(); Jep = r.id if r else None
  url = f"https://t.me/yyegksgfdg/1287"
  await hellas.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.نورتي2$"))
async def jepmeme(memejep):
  r = await memejep.get_reply_message(); Jep = r.id if r else None
  url = f"https://t.me/yyegksgfdg/1288"
  await hellas.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.حياك$"))
async def jepmeme(memejep):
  r = await memejep.get_reply_message(); Jep = r.id if r else None
  url = f"https://t.me/yyegksgfdg/1289"
  await hellas.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.حياج$"))
async def jepmeme(memejep):
  r = await memejep.get_reply_message(); Jep = r.id if r else None
  url = f"https://t.me/yyegksgfdg/1290"
  await hellas.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.مقدمه$"))
async def jepmeme(memejep):
  r = await memejep.get_reply_message(); Jep = r.id if r else None
  url = f"https://t.me/yyegksgfdg/1291"
  await hellas.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.نهايه$"))
async def jepmeme(memejep):
  r = await memejep.get_reply_message(); Jep = r.id if r else None
  url = f"https://t.me/yyegksgfdg/1294"
  await hellas.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.صباحو2$"))
async def jepmeme(memejep):
  r = await memejep.get_reply_message(); Jep = r.id if r else None
  url = f"https://t.me/yyegksgfdg/1295"
  await hellas.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.مساء الورد$"))
async def jepmeme(memejep):
  r = await memejep.get_reply_message(); Jep = r.id if r else None
  url = f"https://t.me/yyegksgfdg/1296"
  await hellas.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.هلاةيروحي2$"))
async def jepmeme(memejep):
  r = await memejep.get_reply_message(); Jep = r.id if r else None
  url = f"https://t.me/yyegksgfdg/1297"
  await hellas.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.هلا قلبي2$"))
async def jepmeme(memejep):
  r = await memejep.get_reply_message(); Jep = r.id if r else None
  url = f"https://t.me/yyegksgfdg/1298"
  await hellas.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.بربوك$"))
async def jepmeme(memejep):
  r = await memejep.get_reply_message(); Jep = r.id if r else None
  url = f"https://t.me/yyegksgfdg/1299"
  await hellas.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.ابلع بلوك2$"))
async def jepmeme(memejep):
  r = await memejep.get_reply_message(); Jep = r.id if r else None
  url = f"https://t.me/yyegksgfdg/1301"
  await hellas.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.شعر1$"))
async def jepmeme(memejep):
  r = await memejep.get_reply_message(); Jep = r.id if r else None
  url = f"https://t.me/yyegksgfdg/1302"
  await hellas.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.شعر2$"))
async def jepmeme(memejep):
  r = await memejep.get_reply_message(); Jep = r.id if r else None
  url = f"https://t.me/yyegksgfdg/1303"
  await hellas.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.امشي لك$"))
async def jepmeme(memejep):
  r = await memejep.get_reply_message(); Jep = r.id if r else None
  url = f"https://t.me/yyegksgfdg/1305"
  await hellas.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.ابو لبنات$"))
async def jepmeme(memejep):
  r = await memejep.get_reply_message(); Jep = r.id if r else None
  url = f"https://t.me/yyegksgfdg/1306"
  await hellas.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete() 
@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.ايع2$"))
async def jepmeme(memejep):
  r = await memejep.get_reply_message(); Jep = r.id if r else None
  url = f"https://t.me/yyegksgfdg/1308"
  await hellas.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.مشاعرك عضروطيه$"))
async def jepmeme(memejep):
  r = await memejep.get_reply_message(); Jep = r.id if r else None
  url = f"https://t.me/yyegksgfdg/1309"
  await hellas.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.س ميوزك$"))
async def jepmeme(memejep):
  r = await memejep.get_reply_message(); Jep = r.id if r else None
  url = f"https://t.me/yyegksgfdg/1341"
  await hellas.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.س نشر$"))
async def jepmeme(memejep):
  r = await memejep.get_reply_message(); Jep = r.id if r else None
  url = f"https://t.me/yyegksgfdg/1342"
  await hellas.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.س حمايه$"))
async def jepmeme(memejep):
  r = await memejep.get_reply_message(); Jep = r.id if r else None
  url = f"https://t.me/yyegksgfdg/1343"
  await hellas.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.اريد هديه$"))
async def jepmeme(memejep):
  r = await memejep.get_reply_message(); Jep = r.id if r else None
  url = f"https://t.me/yyegksgfdg/1345"
  await hellas.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.اريد نجوم$"))
async def jepmeme(memejep):
  r = await memejep.get_reply_message(); Jep = r.id if r else None
  url = f"https://t.me/yyegksgfdg/1346"
  await hellas.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.50 نجمه$"))
async def jepmeme(memejep):
  r = await memejep.get_reply_message(); Jep = r.id if r else None
  url = f"https://t.me/yyegksgfdg/1347"
  await hellas.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.100 نجمه$"))
async def jepmeme(memejep):
  r = await memejep.get_reply_message(); Jep = r.id if r else None
  url = f"https://t.me/yyegksgfdg/1348"
  await hellas.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.ماعندي نجوم$"))
async def jepmeme(memejep):
  r = await memejep.get_reply_message(); Jep = r.id if r else None
  url = f"https://t.me/yyegksgfdg/1349"
  await hellas.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.25 نجمه$"))
async def jepmeme(memejep):
  r = await memejep.get_reply_message(); Jep = r.id if r else None
  url = f"https://t.me/yyegksgfdg/1350"
  await hellas.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.شلخبار2$"))
async def jepmeme(memejep):
  r = await memejep.get_reply_message(); Jep = r.id if r else None
  url = f"https://t.me/yyegksgfdg/1352"
  await hellas.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.شلونك3$"))
async def jepmeme(memejep):
  r = await memejep.get_reply_message(); Jep = r.id if r else None
  url = f"https://t.me/yyegksgfdg/1353"
  await hellas.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.شلونج3$"))
async def jepmeme(memejep):
  r = await memejep.get_reply_message(); Jep = r.id if r else None
  url = f"https://t.me/yyegksgfdg/1354"
  await hellas.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.نتعرف2$"))
async def jepmeme(memejep):
  r = await memejep.get_reply_message(); Jep = r.id if r else None
  url = f"https://t.me/yyegksgfdg/1355"
  await hellas.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.معجبه$"))
async def jepmeme(memejep):
  r = await memejep.get_reply_message(); Jep = r.id if r else None
  url = f"https://t.me/yyegksgfdg/1356"
  await hellas.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.عجبني اراسلك$"))
async def jepmeme(memejep):
  r = await memejep.get_reply_message(); Jep = r.id if r else None
  url = f"https://t.me/yyegksgfdg/1357"
  await hellas.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.نرتبط2$"))
async def jepmeme(memejep):
  r = await memejep.get_reply_message(); Jep = r.id if r else None
  url = f"https://t.me/yyegksgfdg/1358"
  await hellas.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.نزوج2$"))
async def jepmeme(memejep):
  r = await memejep.get_reply_message(); Jep = r.id if r else None
  url = f"https://t.me/yyegksgfdg/1359"
  await hellas.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.ترا حبيتك$"))
async def jepmeme(memejep):
  r = await memejep.get_reply_message(); Jep = r.id if r else None
  url = f"https://t.me/yyegksgfdg/1360"
  await hellas.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.دز صورتك$"))
async def jepmeme(memejep):
  r = await memejep.get_reply_message(); Jep = r.id if r else None
  url = f"https://t.me/yyegksgfdg/1364"
  await hellas.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.سويلي تمويل$"))
async def jepmeme(memejep):
  r = await memejep.get_reply_message(); Jep = r.id if r else None
  url = f"https://t.me/yyegksgfdg/1365"
  await hellas.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.ارشق قناتي$"))
async def jepmeme(memejep):
  r = await memejep.get_reply_message(); Jep = r.id if r else None
  url = f"https://t.me/yyegksgfdg/1366"
  await hellas.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.ارشقلي$"))
async def jepmeme(memejep):
  r = await memejep.get_reply_message(); Jep = r.id if r else None
  url = f"https://t.me/yyegksgfdg/1367"
  await hellas.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.2غنيلي$"))
async def jepmeme(memejep):
  r = await memejep.get_reply_message(); Jep = r.id if r else None
  url = f"https://t.me/yyegksgfdg/1368"
  await hellas.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.غنيلك$"))
async def jepmeme(memejep):
  r = await memejep.get_reply_message(); Jep = r.id if r else None
  url = f"https://t.me/yyegksgfdg/1369"
  await hellas.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.ارشق حسابي$"))
async def jepmeme(memejep):
  r = await memejep.get_reply_message(); Jep = r.id if r else None
  url = f"https://t.me/yyegksgfdg/1370"
  await hellas.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.دز رصيد2$"))
async def jepmeme(memejep):
  r = await memejep.get_reply_message(); Jep = r.id if r else None
  url = f"https://t.me/yyegksgfdg/1375"
  await hellas.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.شبيك لك$"))
async def jepmeme(memejep):
  r = await memejep.get_reply_message(); Jep = r.id if r else None
  url = f"https://t.me/yyegksgfdg/1392"
  await hellas.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.ماكدر تصال2$"))
async def jepmeme(memejep):
  r = await memejep.get_reply_message(); Jep = r.id if r else None
  url = f"https://t.me/yyegksgfdg/1393"
  await hellas.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.ماحب لتصال2$"))
async def jepmeme(memejep):
  r = await memejep.get_reply_message(); Jep = r.id if r else None
  url = f"https://t.me/yyegksgfdg/1394"
  await hellas.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.ابوسك2$"))
async def jepmeme(memejep):
  r = await memejep.get_reply_message(); Jep = r.id if r else None
  url = f"https://t.me/yyegksgfdg/1395"
  await hellas.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.وينك2$"))
async def jepmeme(memejep):
  r = await memejep.get_reply_message(); Jep = r.id if r else None
  url = f"https://t.me/yyegksgfdg/1399"
  await hellas.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.الو2$"))
async def jepmeme(memejep):
  r = await memejep.get_reply_message(); Jep = r.id if r else None
  url = f"https://t.me/yyegksgfdg/1400"
  await hellas.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.اني بنيه لك$"))
async def jepmeme(memejep):
  r = await memejep.get_reply_message(); Jep = r.id if r else None
  url = f"https://t.me/yyegksgfdg/1403"
  await hellas.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.اني بنيه لج$"))
async def jepmeme(memejep):
  r = await memejep.get_reply_message(); Jep = r.id if r else None
  url = f"https://t.me/yyegksgfdg/1404"
  await hellas.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.مبي شحن2$"))
async def jepmeme(memejep):
  r = await memejep.get_reply_message(); Jep = r.id if r else None
  url = f"https://t.me/yyegksgfdg/1406"
  await hellas.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.يلا لتلح2$"))
async def jepmeme(memejep):
  r = await memejep.get_reply_message(); Jep = r.id if r else None
  url = f"https://t.me/yyegksgfdg/1407"
  await hellas.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.يلا لتلحين2$"))
async def jepmeme(memejep):
  r = await memejep.get_reply_message(); Jep = r.id if r else None
  url = f"https://t.me/yyegksgfdg/1409"
  await hellas.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.مادري2$"))
async def jepmeme(memejep):
  r = await memejep.get_reply_message(); Jep = r.id if r else None
  url = f"https://t.me/yyegksgfdg/1410"
  await hellas.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.فعلي مميز2$"))
async def jepmeme(memejep):
  r = await memejep.get_reply_message(); Jep = r.id if r else None
  url = f"https://t.me/yyegksgfdg/1413"
  await hellas.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.همداك$"))
async def jepmeme(memejep):
  r = await memejep.get_reply_message(); Jep = r.id if r else None
  url = f"https://t.me/yyegksgfdg/1415"
  await hellas.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.شدلي منصه2$"))
async def jepmeme(memejep):
  r = await memejep.get_reply_message(); Jep = r.id if r else None
  url = f"https://t.me/yyegksgfdg/1420"
  await hellas.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.بيش هاذ$"))
async def jepmeme(memejep):
  r = await memejep.get_reply_message(); Jep = r.id if r else None
  url = f"https://t.me/yyegksgfdg/1422"
  await hellas.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.قفل$"))
async def jepmeme(memejep):
  r = await memejep.get_reply_message(); Jep = r.id if r else None
  url = f"https://t.me/yyegksgfdg/1425"
  await hellas.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.متتوفر$"))
async def jepmeme(memejep):
  r = await memejep.get_reply_message(); Jep = r.id if r else None
  url = f"https://t.me/yyegksgfdg/1428"
  await hellas.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.الو السلام2$"))
async def jepmeme(memejep):
  r = await memejep.get_reply_message(); Jep = r.id if r else None
  url = f"https://t.me/yyegksgfdg/1432"
  await hellas.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.شكد فاهي2$"))
async def jepmeme(memejep):
  r = await memejep.get_reply_message(); Jep = r.id if r else None
  url = f"https://t.me/yyegksgfdg/1433"
  await hellas.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.شدسوي2$"))
async def jepmeme(memejep):
  r = await memejep.get_reply_message(); Jep = r.id if r else None
  url = f"https://t.me/yyegksgfdg/1438"
  await hellas.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.انت فاهي$"))
async def jepmeme(memejep):
  r = await memejep.get_reply_message(); Jep = r.id if r else None
  url = f"https://t.me/yyegksgfdg/1439"
  await hellas.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.هاي انته2$"))
async def jepmeme(memejep):
  r = await memejep.get_reply_message(); Jep = r.id if r else None
  url = f"https://t.me/yyegksgfdg/1444"
  await hellas.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.شتريد2$"))
async def jepmeme(memejep):
  r = await memejep.get_reply_message(); Jep = r.id if r else None
  url = f"https://t.me/yyegksgfdg/1445"
  await hellas.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.اني حلوه2$"))
async def jepmeme(memejep):
  r = await memejep.get_reply_message(); Jep = r.id if r else None
  url = f"https://t.me/yyegksgfdg/1446"
  await hellas.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.ارفعني2$"))
async def jepmeme(memejep):
  r = await memejep.get_reply_message(); Jep = r.id if r else None
  url = f"https://t.me/yyegksgfdg/1452"
  await hellas.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.ليش2$"))
async def jepmeme(memejep):
  r = await memejep.get_reply_message(); Jep = r.id if r else None
  url = f"https://t.me/yyegksgfdg/1453"
  await hellas.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.تعذرني$"))
async def jepmeme(memejep):
  r = await memejep.get_reply_message(); Jep = r.id if r else None
  url = f"https://t.me/yyegksgfdg/1454"
  await hellas.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.لا شكرا2$"))
async def jepmeme(memejep):
  r = await memejep.get_reply_message(); Jep = r.id if r else None
  url = f"https://t.me/yyegksgfdg/1455"
  await hellas.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.ثقفو2$"))
async def jepmeme(memejep):
  r = await memejep.get_reply_message(); Jep = r.id if r else None
  url = f"https://t.me/yyegksgfdg/1456"
  await hellas.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.عزه لعزاك$"))
async def jepmeme(memejep):
  r = await memejep.get_reply_message(); Jep = r.id if r else None
  url = f"https://t.me/yyegksgfdg/1459"
  await hellas.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.شكد سخيف2$"))
async def jepmeme(memejep):
  r = await memejep.get_reply_message(); Jep = r.id if r else None
  url = f"https://t.me/yyegksgfdg/1466"
  await hellas.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.لبش تغييرت$"))
async def jepmeme(memejep):
  r = await memejep.get_reply_message(); Jep = r.id if r else None
  url = f"https://t.me/yyegksgfdg/1473"
  await hellas.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.جنك ماعاجبك2$"))
async def jepmeme(memejep):
  r = await memejep.get_reply_message(); Jep = r.id if r else None
  url = f"https://t.me/yyegksgfdg/1474"
  await hellas.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.اكل خره2$"))
async def jepmeme(memejep):
  r = await memejep.get_reply_message(); Jep = r.id if r else None
  url = f"https://t.me/yyegksgfdg/1476"
  await hellas.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.اخوي اجهه$"))
async def jepmeme(memejep):
  r = await memejep.get_reply_message(); Jep = r.id if r else None
  url = f"https://t.me/yyegksgfdg/1477"
  await hellas.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.هلو كرار2$"))
async def jepmeme(memejep):
  r = await memejep.get_reply_message(); Jep = r.id if r else None
  url = f"https://t.me/yyegksgfdg/1478"
  await hellas.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.هلو محمد2$"))
async def jepmeme(memejep):
  r = await memejep.get_reply_message(); Jep = r.id if r else None
  url = f"https://t.me/yyegksgfdg/1479"
  await hellas.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.هلو علي2$"))
async def jepmeme(memejep):
  r = await memejep.get_reply_message(); Jep = r.id if r else None
  url = f"https://t.me/yyegksgfdg/1480"
  await hellas.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.هلو داده$"))
async def jepmeme(memejep):
  r = await memejep.get_reply_message(); Jep = r.id if r else None
  url = f"https://t.me/yyegksgfdg/1481"
  await hellas.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.عيوني الك$"))
async def jepmeme(memejep):
  r = await memejep.get_reply_message(); Jep = r.id if r else None
  url = f"https://t.me/yyegksgfdg/1486"
  await hellas.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.شكد عمرك2$"))
async def jepmeme(memejep):
  r = await memejep.get_reply_message(); Jep = r.id if r else None
  url = f"https://t.me/yyegksgfdg/1487"
  await hellas.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.من شوكت مرتبط$"))
async def jepmeme(memejep):
  r = await memejep.get_reply_message(); Jep = r.id if r else None
  url = f"https://t.me/yyegksgfdg/1488"
  await hellas.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.راح احذفك$"))
async def jepmeme(memejep):
  r = await memejep.get_reply_message(); Jep = r.id if r else None
  url = f"https://t.me/yyegksgfdg/1489"
  await hellas.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.رد خاص$"))
async def jepmeme(memejep):
  r = await memejep.get_reply_message(); Jep = r.id if r else None
  url = f"https://t.me/yyegksgfdg/1490"
  await hellas.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.كلشي من وراك$"))
async def jepmeme(memejep):
  r = await memejep.get_reply_message(); Jep = r.id if r else None
  url = f"https://t.me/yyegksgfdg/1491"
  await hellas.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.لاشوف غيري$"))
async def jepmeme(memejep):
  r = await memejep.get_reply_message(); Jep = r.id if r else None
  url = f"https://t.me/yyegksgfdg/1492"
  await hellas.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.هواي تعبت$"))
async def jepmeme(memejep):
  r = await memejep.get_reply_message(); Jep = r.id if r else None
  url = f"https://t.me/yyegksgfdg/1493"
  await hellas.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.ليش زعلت$"))
async def jepmeme(memejep):
  r = await memejep.get_reply_message(); Jep = r.id if r else None
  url = f"https://t.me/yyegksgfdg/1494"
  await hellas.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.هلو حسون2$"))
async def jepmeme(memejep):
  r = await memejep.get_reply_message(); Jep = r.id if r else None
  url = f"https://t.me/yyegksgfdg/1495"
  await hellas.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.هلو عبودي2$"))
async def jepmeme(memejep):
  r = await memejep.get_reply_message(); Jep = r.id if r else None
  url = f"https://t.me/yyegksgfdg/1496"
  await hellas.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.هلو مصطفى2$"))
async def jepmeme(memejep):
  r = await memejep.get_reply_message(); Jep = r.id if r else None
  url = f""
  await hellas.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()
@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.وصخ2$"))
async def jepmeme(memejep):
  r = await memejep.get_reply_message(); Jep = r.id if r else None
  url = f"https://t.me/yyegksgfdg/1498"
  await hellas.send_file(memejep.chat_id,url,caption="",parse_mode="html",reply_to=Jep)
  await memejep.delete()

###ميمز

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.هاروني$"))
async def jepmeme(memejep):
  r = await memejep.get_reply_message(); Jep = r.id if r else None
  url = f"https://t.me/kkmgee/97"
  await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
  await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.همبركر$"))
async def jepmeme(memejep):
  r = await memejep.get_reply_message(); Jep = r.id if r else None
  url = f"https://t.me/kkmgee/98"
  await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
  await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.لا شماته$"))
async def jepmeme(memejep):
  r = await memejep.get_reply_message(); Jep = r.id if r else None
  url = f"https://t.me/kkmgee/4"
  await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
  await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.تفضل$"))
async def jepmeme(memejep):
  r = await memejep.get_reply_message(); Jep = r.id if r else None
  url = f"https://t.me/kkmgee/5"
  await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
  await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.اشكرج طبعا$"))
async def jepmeme(memejep):
  r = await memejep.get_reply_message(); Jep = r.id if r else None
  url = f"https://t.me/kkmgee/7"
  await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
  await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.ماردنا الطلايب$"))
async def jepmeme(memejep):
  r = await memejep.get_reply_message(); Jep = r.id if r else None
  url = f"https://t.me/kkmgee/8"
  await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
  await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.موال سلام$"))
async def jepmeme(memejep):
  r = await memejep.get_reply_message(); Jep = r.id if r else None
  url = f"https://t.me/kkmgee/9"
  await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
  await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.اف مبروك$"))
async def jepmeme(memejep):
  r = await memejep.get_reply_message(); Jep = r.id if r else None
  url = f"https://t.me/kkmgee/10"
  await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
  await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.الاكننا الافضل$"))
async def jepmeme(memejep):
  r = await memejep.get_reply_message(); Jep = r.id if r else None
  url = f"https://t.me/kkmgee/11"
  await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
  await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.اطلع بره$"))
async def jepmeme(memejep):
  r = await memejep.get_reply_message(); Jep = r.id if r else None
  url = f"https://t.me/kkmgee/12"
  await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
  await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.بليز ترامب$"))
async def jepmeme(memejep):
  r = await memejep.get_reply_message(); Jep = r.id if r else None
  url = f"https://t.me/kkmgee/13"
  await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
  await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.واجب$"))
async def jepmeme(memejep):
  r = await memejep.get_reply_message(); Jep = r.id if r else None
  url = f"https://t.me/kkmgee/14"
  await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
  await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.حيدر كيمز$"))
async def jepmeme(memejep):
  r = await memejep.get_reply_message(); Jep = r.id if r else None
  url = f"https://t.me/kkmgee/15"
  await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
  await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.شماته$"))
async def jepmeme(memejep):
  r = await memejep.get_reply_message(); Jep = r.id if r else None
  url = f"https://t.me/kkmgee/19"
  await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
  await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.يلا دي$"))
async def jepmeme(memejep):
  r = await memejep.get_reply_message(); Jep = r.id if r else None
  url = f"https://t.me/kkmgee/21"
  await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
  await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.وين كلاوات$"))
async def jepmeme(memejep):
  r = await memejep.get_reply_message(); Jep = r.id if r else None
  url = f"https://t.me/kkmgee/23"
  await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
  await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.لكيتني$"))
async def jepmeme(memejep):
  r = await memejep.get_reply_message(); Jep = r.id if r else None
  url = f"https://t.me/kkmgee/24"
  await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
  await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.يعني يعني$"))
async def jepmeme(memejep):
  r = await memejep.get_reply_message(); Jep = r.id if r else None
  url = f"https://t.me/kkmgee/25"
  await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
  await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.يبو فاضل$"))
async def jepmeme(memejep):
  r = await memejep.get_reply_message(); Jep = r.id if r else None
  url = f"https://t.me/kkmgee/26"
  await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
  await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.جلاب$"))
async def jepmeme(memejep):
  r = await memejep.get_reply_message(); Jep = r.id if r else None
  url = f"https://t.me/kkmgee/27"
  await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
  await memejep.delete()

# 10 أخرى أيضاً بنفس الشكل:

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.حسناء$"))
async def jepmeme(memejep):
  r = await memejep.get_reply_message(); Jep = r.id if r else None
  url = f"https://t.me/kkmgee/28"
  await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
  await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.انت اسكت$"))
async def jepmeme(memejep):
  r = await memejep.get_reply_message(); Jep = r.id if r else None
  url = f"https://t.me/kkmgee/29"
  await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
  await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.اسكت ياخي$"))
async def jepmeme(memejep):
  r = await memejep.get_reply_message(); Jep = r.id if r else None
  url = f"https://t.me/kkmgee/30"
  await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
  await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.ارسلني حمزه$"))
async def jepmeme(memejep):
  r = await memejep.get_reply_message(); Jep = r.id if r else None
  url = f"https://t.me/kkmgee/32"
  await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
  await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.عفطه$"))
async def jepmeme(memejep):
  r = await memejep.get_reply_message(); Jep = r.id if r else None
  url = f"https://t.me/kkmgee/36"
  await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
  await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.حيل ضايج$"))
async def jepmeme(memejep):
  r = await memejep.get_reply_message(); Jep = r.id if r else None
  url = f"https://t.me/kkmgee/41"
  await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
  await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.شجاي تلغي$"))
async def jepmeme(memejep):
  r = await memejep.get_reply_message(); Jep = r.id if r else None
  url = f"https://t.me/kkmgee/47"
  await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
  await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.كافي جلبت$"))
async def jepmeme(memejep):
  r = await memejep.get_reply_message(); Jep = r.id if r else None
  url = f"https://t.me/kkmgee/48"
  await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
  await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.هاي شبيك$"))
async def jepmeme(memejep):
  r = await memejep.get_reply_message(); Jep = r.id if r else None
  url = f"https://t.me/kkmgee/50"
  await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
  await memejep.delete()

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^.انا اسفف$"))
async def jepmeme(memejep):
  r = await memejep.get_reply_message(); Jep = r.id if r else None
  url = f"https://t.me/kkmgee/53"
  await hellas.send_file(memejep.chat_id, url, caption="", parse_mode="html", reply_to=Jep)
  await memejep.delete()
