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
MASTER_FILE = "master_number.txt"
TON_FILE = "ton_address.txt"
USDT_FILE = "usdt_address.txt"

# وظيفة الحفظ السريعة
async def save_data(event, file_path, data, label):
    with open(file_path, "w") as f:
        f.write(data)
    await event.edit(f"✅ تم حفظ {label}: `{data}`")

# وظيفة العرض السريعة
async def show_data(event, file_path, label):
    if os.path.exists(file_path):
        with open(file_path, "r") as f:
            data = f.read().strip()
        await event.edit(f"📌 {label}: `{data}`")
    else:
        await event.edit(f"❌ لا يوجد {label} محفوظ.")

# --- أوامر الرصيد والمحافظ ---

# آسيا
@hellas.on(events.NewMessage(pattern=r"^\.رقم(ال)?اسيا\s+(.+)$", outgoing=True))
async def s_asia(e): await save_data(e, ASIA_FILE, e.pattern_match.group(2).strip(), "رقم اسيا")

@hellas.on(events.NewMessage(pattern=r"^\.(ال)?اسيا$", outgoing=True))
async def g_asia(e): await show_data(e, ASIA_FILE, "رقم اسيا")

# كاش
@hellas.on(events.NewMessage(pattern=r"^\.رقم(ال)?كاش\s+(.+)$", outgoing=True))
async def s_kash(e): await save_data(e, KASH_FILE, e.pattern_match.group(2).strip(), "رقم الكاش")

@hellas.on(events.NewMessage(pattern=r"^\.(ال)?كاش$", outgoing=True))
async def g_kash(e): await show_data(e, KASH_FILE, "رقم الكاش")

# ماستر
@hellas.on(events.NewMessage(pattern=r"^\.رقم(ال)?ماستر\s+(.+)$", outgoing=True))
async def s_master(e): await save_data(e, MASTER_FILE, e.pattern_match.group(2).strip(), "رقم الماستر")

@hellas.on(events.NewMessage(pattern=r"^\.(ال)?ماستر$", outgoing=True))
async def g_master(e): await show_data(e, MASTER_FILE, "رقم الماستر")

# تون (TON)
@hellas.on(events.NewMessage(pattern=r"^\.رقم(ال)?تون\s+(.+)$", outgoing=True))
async def s_ton(e): await save_data(e, TON_FILE, e.pattern_match.group(2).strip(), "عنوان التون")

@hellas.on(events.NewMessage(pattern=r"^\.(ال)?تون$", outgoing=True))
async def g_ton(e): await show_data(e, TON_FILE, "عنوان التون")

# يوستد (USDT)
@hellas.on(events.NewMessage(pattern=r"^\.رقم(ال)?يوستد\s+(.+)$", outgoing=True))
async def s_usdt(e): await save_data(e, USDT_FILE, e.pattern_match.group(2).strip(), "عنوان اليوستد")

@hellas.on(events.NewMessage(pattern=r"^\.(ال)?يوستد$", outgoing=True))
async def g_usdt(e): await show_data(e, USDT_FILE, "عنوان اليوستد")

# تحويل الرصيد
@hellas.on(events.NewMessage(pattern=r"^\.تحويل\s+(\d+)\s+(\d+)$", outgoing=True))
async def convert_handler(e):
    await e.edit(f"```\n*123*{e.pattern_match.group(2)}*{e.pattern_match.group(1)}#\n```")

# أوامر الرصيد والمحافظ (القائمة)
@hellas.on(events.NewMessage(pattern=r"^\.اوامر الرصيد$", outgoing=True))
async def show_balance_sections(event):
    await event.edit(
        "**📦 قائمة المحافظ والرصيد:**\n"
        "• `.الاسيا` | `.الماستر` | `.الكاش`\n"
        "• `.التون` | `.اليوستد` | `.التحويل`\n\n"
        "📌 للحفظ: `.رقم تون ادرس_المحفظة`"
    )
