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

# ======== أوامر القوائم المساعدة ========

@hellas.on(events.NewMessage(pattern=r"^\.اوامر الرصيد$", outgoing=True))
async def show_balance_sections(event):
    await event.edit(
        "**📦 أقسام أوامر الرصيد والمحافظ:**\n\n"
        "⥾ `.اوامر الاسيا`\n"
        "⥾ `.اوامر الماستر`\n"
        "⥾ `.اوامر الكاش`\n"
        "⥾ `.اوامر الكورك`\n"
        "⥾ `.اوامر التون`\n"
        "⥾ `.اوامر الاثير`\n"
        "⥾ `.اوامر اليوستد`\n"
        "⥾ `.اوامر تحويل`\n\n"
        "✦ أرسل أي أمر منها لعرض التعليمات الخاصة به."
    )

@hellas.on(events.NewMessage(pattern=r"^\.اوامر تحويل$", outgoing=True))
async def show_convert_instructions(event):
    await event.edit(
        "**📥 أوامر تحويل الرصيد 📥**\n\n"
        "⦾ `.تحويل` + رقم الهاتف + المبلغ\n"
        "مثال:\n"
        "`.تحويل 0777 10000`\n\n"
        "سيرد البوت بهذا النص القابل للنسخ:\n"
        "```\n*123*10000*077#\n```"
    )

# ======== وظائف الحفظ العامة ========
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

# ======== تنفيذ الأوامر (اسيا، كاش، كورك، ماستر، الخ) ========

# --- ماستر ---
@hellas.on(events.NewMessage(pattern=r"^\.رقم ماستر (\d+)$", outgoing=True))
async def s_master(e): await save_data(e, MASTER_FILE, e.pattern_match.group(1), "رقم الماستر")

@hellas.on(events.NewMessage(pattern=r"^\.ماستر$", outgoing=True))
async def g_master(e): await show_data(e, MASTER_FILE, "رقم الماستر")

# --- اسيا ---
@hellas.on(events.NewMessage(pattern=r"^\.رقم اسيا (\d+)$", outgoing=True))
async def s_asia(e): await save_data(e, ASIA_FILE, e.pattern_match.group(1), "رقم اسيا")

@hellas.on(events.NewMessage(pattern=r"^\.اسيا$", outgoing=True))
async def g_asia(e): await show_data(e, ASIA_FILE, "رقم اسيا")

# --- كاش ---
@hellas.on(events.NewMessage(pattern=r"^\.رقم كاش (\d+)$", outgoing=True))
async def s_kash(e): await save_data(e, KASH_FILE, e.pattern_match.group(1), "رقم الكاش")

@hellas.on(events.NewMessage(pattern=r"^\.كاش$", outgoing=True))
async def g_kash(e): await show_data(e, KASH_FILE, "رقم الكاش")

# --- تحويل الرصيد المباشر ---
@hellas.on(events.NewMessage(pattern=r'^\.تحويل\s+(\d+)\s+(\d+)$', outgoing=True))
async def convert_handler(event):
    num, amount = event.pattern_match.group(1), event.pattern_match.group(2)
    await event.edit(f"```\n*123*{amount}*{num}#\n```")

# --- سعر التون ---
@hellas.on(events.NewMessage(pattern=r"^\.صرف$", outgoing=True))
async def ton_price(event):
    try:
        r = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=the-open-network&vs_currencies=usd").json()
        p = r['the-open-network']['usd']
        await event.edit(f"💸 سعر عملة TON حالياً:\n`{p} $`")
    except:
        await event.edit("❌ تعذر جلب السعر.")

# --- حذف البيانات (أمثلة) ---
@hellas.on(events.NewMessage(pattern=r"^\.حذف (اسيا|كاش|ماستر|كورك)$", outgoing=True))
async def del_any(e):
    cmd = e.pattern_match.group(1)
    files = {"اسيا": ASIA_FILE, "كاش": KASH_FILE, "ماستر": MASTER_FILE, "كورك": KOREK_FILE}
    await delete_data(e, files[cmd], cmd)

# ======== أوامر المساعدة التفصيلية ========
@hellas.on(events.NewMessage(pattern=r"^\.اوامر (الاسيا|الكاش|الكورك|الماستر)$", outgoing=True))
async def detailed_help(event):
    cmd = event.pattern_match.group(1)
    await event.edit(f"**📱 أوامر إدارة {cmd}:**\n\n"
                     f"• `.رقم {cmd.lower()} <الرقم>` — لحفظ الرقم\n"
                     f"• `.تغ {cmd.lower()} <الرقم>` — لتغييره\n"
                     f"• `.{cmd.lower()}` — عرض الرقم المحفوظ\n"
                     f"• `.حذف {cmd.lower()}` — حذف الرقم")
