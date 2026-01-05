import __main__ as main_module
import re
from telethon import events, Button

# ربط المحركات
hellas = main_module.hellas
tg_bot = main_module.tg_bot

# أيقونات احترافية للتصميم
HEADER = "✨ **𝐇𝐄𝐋𝐋𝐀𝐒 𝐂𝐀𝐋𝐂𝐔𝐋𝐀𝐓𝐎𝐑** ✨"
DISPLAY_FORMAT = "```\n[ {} ]\n```"

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^\.حاسبة$"))
async def start_calc(event):
    bot_me = await tg_bot.get_me()
    # استخدام نظام الانلاين كيري لبدء الحاسبة
    results = await hellas.inline_query(bot_me.username, "calc_init")
    await results[0].click(event.chat_id)
    await event.delete()

@tg_bot.on(events.InlineQuery(pattern=r"calc_init"))
async def inline_calc(event):
    builder = event.builder
    # واجهة التشغيل الأولى
    result = builder.article(
        title="شغل الحاسبة الاحترافية",
        text=f"{HEADER}\n\n{DISPLAY_FORMAT.format('0')}",
        buttons=create_pro_buttons("0")
    )
    await event.answer([result])

@tg_bot.on(events.CallbackQuery(data=re.compile(b"cal_btn:(.*)")))
async def handle_calc_press(event):
    action = event.data_match.group(1).decode()
    # جلب النص الحالي من الشاشة بين الأقواس [ ]
    current_display = re.search(r"\[ (.*) \]", event.original_update.msg.message).group(1)

    if action == "AC":
        new_display = "0"
    elif action == "DEL":
        new_display = current_display[:-1] if len(current_display) > 1 else "0"
    elif action == "equal":
        try:
            # معالجة الرموز للغة البايثون
            safe_expr = current_display.replace("×", "*").replace("÷", "/").replace("^", "**").replace("%", "/100")
            new_display = str(eval(safe_expr))
            # تقريب النتائج الطويلة جداً
            if "." in new_display and len(new_display) > 10:
                new_display = str(round(float(new_display), 5))
        except:
            new_display = "Error"
    else:
        if current_display in ["0", "Error"]:
            new_display = action
        else:
            new_display = current_display + action

    # تحديث الواجهة فقط إذا تغير النص لمنع الـ Flood
    if new_display != current_display:
        try:
            await event.edit(
                f"{HEADER}\n\n{DISPLAY_FORMAT.format(new_display)}",
                buttons=create_pro_buttons(new_display)
            )
        except: pass
    
    await event.answer()

def create_pro_buttons(display):
    """توزيع أزرار احترافي وشفاف"""
    return [
        [Button.inline("AC", data="cal_btn:AC"), Button.inline("⌫", data="cal_btn:DEL"), Button.inline("^", data="cal_btn:^"), Button.inline("÷", data="cal_btn:÷")],
        [Button.inline("7", data="cal_btn:7"), Button.inline("8", data="cal_btn:8"), Button.inline("9", data="cal_btn:9"), Button.inline("×", data="cal_btn:×")],
        [Button.inline("4", data="cal_btn:4"), Button.inline("5", data="cal_btn:5"), Button.inline("6", data="cal_btn:6"), Button.inline("-", data="cal_btn:-")],
        [Button.inline("1", data="cal_btn:1"), Button.inline("2", data="cal_btn:2"), Button.inline("3", data="cal_btn:3"), Button.inline("+", data="cal_btn:+")],
        [Button.inline("%", data="cal_btn:%"), Button.inline("0", data="cal_btn:0"), Button.inline(".", data="cal_btn:."), Button.inline("=", data="cal_btn:equal")]
    ]
