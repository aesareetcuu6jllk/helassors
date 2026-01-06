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

# وظائف الحفظ والعرض والحذف
async def save_data(event, file_path, data, label):
    with open(file_path, "w") as f:
        f.write(data)
    await event.edit(f"✅ تم حفظ {label}: `{data}`")

async def show_data(event, file_path, label):
    if os.path.exists(file_path):
        with open(file_path, "r") as f:
            data = f.read().strip()
        await event.edit(f"📌 {label}: `{data}`")
    else:
        await event.edit(f"❌ لا يوجد {label} محفوظ.")

async def delete_data(event, file_path, label):
    if os.path.exists(file_path):
        os.remove(file_path)
        await event.edit(f"🗑 تم حذف {label} بنجاح.")
    else:
        await event.edit(f"❌ لا يوجد {label} للحذف.")

# ======== أوامر المساعدة لكل قسم (بنفس الشكل المطلوب) ========

@hellas.on(events.NewMessage(pattern=r"^\.اوامر الماستر$", outgoing=True))
async def help_master(e):
    await e.edit("📱 **أوامر إدارة الماستر:**\n\n• `.رقم الماستر <الرقم>`\n• `.تغ الماستر <الرقم>`\n• `.الماستر` لعرضه\n• `.حذف الماستر`")

@hellas.on(events.NewMessage(pattern=r"^\.اوامر الاسيا$", outgoing=True))
async def help_asia(e):
    await e.edit("📱 **أوامر إدارة الاسيا:**\n\n• `.رقم الاسيا <الرقم>`\n• `.تغ الاسيا <الرقم>`\n• `.الاسيا` لعرضه\n• `.حذف الاسيا`")

@hellas.on(events.NewMessage(pattern=r"^\.اوامر الكاش$", outgoing=True))
async def help_kash(e):
    await e.edit("📱 **أوامر إدارة الكاش:**\n\n• `.رقم الكاش <الرقم>`\n• `.تغ الكاش <الرقم>`\n• `.الكاش` لعرضه\n• `.حذف الكاش`")

@hellas.on(events.NewMessage(pattern=r"^\.اوامر الكورك$", outgoing=True))
async def help_korek(e):
    await e.edit("📱 **أوامر إدارة الكورك:**\n\n• `.رقم الكورك <الرقم>`\n• `.تغ الكورك <الرقم>`\n• `.الكورك` لعرضه\n• `.حذف الكورك`")

@hellas.on(events.NewMessage(pattern=r"^\.اوامر التون$", outgoing=True))
async def help_ton(e):
    await e.edit("📱 **أوامر إدارة التون:**\n\n• `.رقم التون <العنوان>`\n• `.تغ التون <العنوان>`\n• `.التون` لعرضه\n• `.حذف التون`")

@hellas.on(events.NewMessage(pattern=r"^\.اوامر اليوستد$", outgoing=True))
async def help_usdt(e):
    await e.edit("📱 **أوامر إدارة اليوستد:**\n\n• `.رقم اليوستد <العنوان>`\n• `.تغ اليوستد <العنوان>`\n• `.اليوستد` لعرضه\n• `.حذف اليوستد`")

# ======== تنفيذ العمليات (حفظ، عرض، حذف) ========

# --- الماستر ---
@hellas.on(events.NewMessage(pattern=r"^\.(رقم|تغ) الماستر\s+(.+)$", outgoing=True))
async def s_master(e): await save_data(e, MASTER_FILE, e.pattern_match.group(2).strip(), "رقم الماستر")
@hellas.on(events.NewMessage(pattern=r"^\.الماستر$", outgoing=True))
async def g_master(e): await show_data(e, MASTER_FILE, "الماستر")
@hellas.on(events.NewMessage(pattern=r"^\.حذف الماستر$", outgoing=True))
async def d_master(e): await delete_data(e, MASTER_FILE, "الماستر")

# --- الاسيا ---
@hellas.on(events.NewMessage(pattern=r"^\.(رقم|تغ) الاسيا\s+(.+)$", outgoing=True))
async def s_asia(e): await save_data(e, ASIA_FILE, e.pattern_match.group(2).strip(), "رقم الاسيا")
@hellas.on(events.NewMessage(pattern=r"^\.الاسيا$", outgoing=True))
async def g_asia(e): await show_data(e, ASIA_FILE, "الاسيا")
@hellas.on(events.NewMessage(pattern=r"^\.حذف الاسيا$", outgoing=True))
async def d_asia(e): await delete_data(e, ASIA_FILE, "الاسيا")

# --- الكاش ---
@hellas.on(events.NewMessage(pattern=r"^\.(رقم|تغ) الكاش\s+(.+)$", outgoing=True))
async def s_kash(e): await save_data(e, KASH_FILE, e.pattern_match.group(2).strip(), "رقم الكاش")
@hellas.on(events.NewMessage(pattern=r"^\.الكاش$", outgoing=True))
async def g_kash(e): await show_data(e, KASH_FILE, "الكاش")
@hellas.on(events.NewMessage(pattern=r"^\.حذف الكاش$", outgoing=True))
async def d_kash(e): await delete_data(e, KASH_FILE, "الكاش")

# --- التون ---
@hellas.on(events.NewMessage(pattern=r"^\.(رقم|تغ) التون\s+(.+)$", outgoing=True))
async def s_ton(e): await save_data(e, TON_FILE, e.pattern_match.group(2).strip(), "عنوان التون")
@hellas.on(events.NewMessage(pattern=r"^\.التون$", outgoing=True))
async def g_ton(e): await show_data(e, TON_FILE, "التون")
@hellas.on(events.NewMessage(pattern=r"^\.حذف التون$", outgoing=True))
async def d_ton(e): await delete_data(e, TON_FILE, "التون")

# --- اليوستد ---
@hellas.on(events.NewMessage(pattern=r"^\.(رقم|تغ) اليوستد\s+(.+)$", outgoing=True))
async def s_usdt(e): await save_data(e, USDT_FILE, e.pattern_match.group(2).strip(), "عنوان اليوستد")
@hellas.on(events.NewMessage(pattern=r"^\.اليوستد$", outgoing=True))
async def g_usdt(e): await show_data(e, USDT_FILE, "اليوستد")
@hellas.on(events.NewMessage(pattern=r"^\.حذف اليوستد$", outgoing=True))
async def d_usdt(e): await delete_data(e, USDT_FILE, "اليوستد")

# --- تحويل الرصيد المباشر ---
@hellas.on(events.NewMessage(pattern=r"^\.تحويل\s+(\d+)\s+(\d+)$", outgoing=True))
async def convert_handler(e):
    await e.edit(f"```\n*123*{e.pattern_match.group(2)}*{e.pattern_match.group(1)}#\n```")

# قائمة الأوامر العامة
@hellas.on(events.NewMessage(pattern=r"^\.اوامر الرصيد$", outgoing=True))
async def show_all(e):
    await e.edit("**📦 أقسام أوامر الرصيد والمحافظ:**\n\n⥾ `.اوامر الاسيا`\n⥾ `.اوامر الماستر`\n⥾ `.اوامر الكاش`\n⥾ `.اوامر التون`\n⥾ `.اوامر اليوستد`\n⥾ `.تحويل` رقم مبلغ")
