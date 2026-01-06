import __main__ as main_module
from telethon import events
import os
import requests
import re

# ربط محرك سورس هيلاس
hellas = main_module.hellas

# ملفات حفظ البيانات
ASIA_FILE = "asia_number.txt"
KASH_FILE = "kash_number.txt"
KOREK_FILE = "korek_number.txt"
TON_FILE = "ton_address.txt"
ETH_FILE = "eth_number.txt"
USDT_FILE = "usdt_number.txt"
MASTER_FILE = "master_number.txt"

# ======== وظائف المساعدة (للتوفير في الكود) ========
async def save_data(event, file_path, data, label):
    with open(file_path, "w") as f:
        f.write(data)
    await event.edit(f"✅ تم حفظ {label}: `{data}`")

async def show_data(event, file_path, label):
    if os.path.exists(file_path):
        with open(file_path, "r") as f:
            data = f.read().strip()
        await event.edit(f"📌 {label} المحفوظ هو: `{data}`")
    else:
        await event.edit(f"❌ لا يوجد {label} محفوظ بعد.")

async def delete_data(event, file_path, label):
    if os.path.exists(file_path):
        os.remove(file_path)
        await event.edit(f"🗑 تم حذف {label} بنجاح.")
    else:
        await event.edit(f"❌ لا يوجد {label} للحذف.")

# ======== أوامر القوائم ========

@hellas.on(events.NewMessage(pattern=r"^\.اوامر الرصيد$", outgoing=True))
async def show_balance_sections(event):
    await event.edit(
        "**📦 أقسام أوامر الرصيد والمحافظ:**\n\n"
        "⥾ `.اوامر الاسيا` | `.اوامر الماستر`\n"
        "⥾ `.اوامر الكاش` | `.اوامر الكورك`\n"
        "⥾ `.اوامر التون` | `.اوامر الاثير`\n"
        "⥾ `.اوامر اليوستد` | `.اوامر تحويل`\n\n"
        "✦ أرسل أي أمر منها لعرض التعليمات."
    )

# ======== أوامر الحفظ (أرقام الهاتف) ========

# اسيا
@hellas.on(events.NewMessage(pattern=r"^\.(رقم|تغ) اسيا (\d+)$", outgoing=True))
async def s_asia(e): await save_data(e, ASIA_FILE, e.pattern_match.group(2), "رقم اسيا")

@hellas.on(events.NewMessage(pattern=r"^\.اسيا$", outgoing=True))
async def g_asia(e): await show_data(e, ASIA_FILE, "رقم اسيا")

# كاش
@hellas.on(events.NewMessage(pattern=r"^\.(رقم|تغ) كاش (\d+)$", outgoing=True))
async def s_kash(e): await save_data(e, KASH_FILE, e.pattern_match.group(2), "رقم الكاش")

@hellas.on(events.NewMessage(pattern=r"^\.كاش$", outgoing=True))
async def g_kash(e): await show_data(e, KASH_FILE, "رقم الكاش")

# كورك
@hellas.on(events.NewMessage(pattern=r"^\.(رقم|تغ) كورك (\d+)$", outgoing=True))
async def s_korek(e): await save_data(e, KOREK_FILE, e.pattern_match.group(2), "رقم كورك")

@hellas.on(events.NewMessage(pattern=r"^\.كورك$", outgoing=True))
async def g_korek(e): await show_data(e, KOREK_FILE, "رقم كورك")

# ماستر
@hellas.on(events.NewMessage(pattern=r"^\.(رقم|تغ) ماستر (\d+)$", outgoing=True))
async def s_master(e): await save_data(e, MASTER_FILE, e.pattern_match.group(2), "رقم الماستر")

@hellas.on(events.NewMessage(pattern=r"^\.ماستر$", outgoing=True))
async def g_master(e): await show_data(e, MASTER_FILE, "رقم الماستر")

# ======== أوامر الحفظ (المحافظ والعناوين) ========

# تون
@hellas.on(events.NewMessage(pattern=r"^\.(ادرس|تغ) تون (.+)$", outgoing=True))
async def s_ton(e): await save_data(e, TON_FILE, e.pattern_match.group(2).strip(), "عنوان التون")

@hellas.on(events.NewMessage(pattern=r"^\.(ادرسي|تون)$", outgoing=True))
async def g_ton(e): await show_data(e, TON_FILE, "عنوان التون")

# اثير
@hellas.on(events.NewMessage(pattern=r"^\.(رقم|تغ) اثير (.+)$", outgoing=True))
async def s_eth(e): await save_data(e, ETH_FILE, e.pattern_match.group(2).strip(), "رقم الاثير")

@hellas.on(events.NewMessage(pattern=r"^\.اثير$", outgoing=True))
async def g_eth(e): await show_data(e, ETH_FILE, "رقم الاثير")

# يوستد
@hellas.on(events.NewMessage(pattern=r"^\.(رقم|تغ) يوستد (.+)$", outgoing=True))
async def s_usdt(e): await save_data(e, USDT_FILE, e.pattern_match.group(2).strip(), "عنوان اليوستد")

@hellas.on(events.NewMessage(pattern=r"^\.يوستد$", outgoing=True))
async def g_usdt(e): await show_data(e, USDT_FILE, "عنوان اليوستد")

# ======== الحذف الموحد ========
@hellas.on(events.NewMessage(pattern=r"^\.حذف (اسيا|كاش|ماستر|كورك|تون|اثير|يوستد)$", outgoing=True))
async def del_any(e):
    cmd = e.pattern_match.group(1)
    f_map = {"اسيا": ASIA_FILE, "كاش": KASH_FILE, "ماستر": MASTER_FILE, "كورك": KOREK_FILE, "تون": TON_FILE, "اثير": ETH_FILE, "يوستد": USDT_FILE}
    await delete_data(e, f_map[cmd], cmd)

# ======== التحويل والأسعار ========
@hellas.on(events.NewMessage(pattern=r'^\.تحويل\s+(\d+)\s+(\d+)$', outgoing=True))
async def convert_handler(e):
    await e.edit(f"```\n*123*{e.pattern_match.group(2)}*{e.pattern_match.group(1)}#\n```")

@hellas.on(events.NewMessage(pattern=r"^\.صرف$", outgoing=True))
async def ton_price(e):
    try:
        p = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=the-open-network&vs_currencies=usd").json()['the-open-network']['usd']
        await e.edit(f"💸 سعر عملة TON حالياً: `{p} $`")
    except: await e.edit("❌ خطأ في جلب السعر.")

# ======== قوائم التعليمات لكل قسم ========
@hellas.on(events.NewMessage(pattern=r"^\.اوامر (الاسيا|الكاش|الكورك|الماستر|التون|الاثير|اليوستد|تحويل)$", outgoing=True))
async def detailed_help(event):
    cmd = event.pattern_match.group(1)
    await event.edit(f"**📱 أوامر إدارة {cmd}:**\n\n• `.رقم {cmd.lower()} <الرقم>`\n• `.تغ {cmd.lower()} <الرقم>`\n• `.{cmd.lower()}` لعرضه\n• `.حذف {cmd.lower()}`")
