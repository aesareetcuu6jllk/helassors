import __main__ as main_module
import re
from telethon import events, Button

# ربط المحركات
hellas = main_module.hellas
tg_bot = main_module.tg_bot

# واجهة نظيفة (بدون تعقيدات برمجية تبطئ التحديث)
def format_screen(text):
    return f"```\n{text}\n```"

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^\.حاسبة$"))
async def start_calc(event):
    bot_me = await tg_bot.get_me()
    results = await hellas.inline_query(bot_me.username, "calc_init")
    await results[0].click(event.chat_id)
    await event.delete()

@tg_bot.on(events.InlineQuery(pattern=r"calc_init"))
async def inline_calc(event):
    builder = event.builder
    result = builder.article(
        title="الآلة الحاسبة الاحترافية",
        text=format_screen("0"),
        buttons=create_pro_buttons("0")
    )
    await event.answer([result], cache_time=0)

@tg_bot.on(events.CallbackQuery(data=re.compile(b"cal_btn:(.*)")))
async def handle_calc_press(event):
    action = event.data_match.group(1).decode()
    
    # جلب النص الحالي وتنظيفه من كل رموز التليجرام الزائدة
    raw_text = event.original_update.msg.message
    current_display = raw_text.replace('`', '').strip()

    if action == "AC":
        new_display = "0"
    elif action == "DEL":
        if "=" in current_display or current_display == "Error":
            new_display = "0"
        else:
            new_display = current_display[:-1] if len(current_display) > 1 else "0"
    elif action == "equal":
        if "=" in current_display or current_display == "Error" or current_display == "0":
            new_display = current_display
        else:
            try:
                # استبدال الرموز للحساب
                expr = current_display.replace("×", "*").replace("÷", "/").replace("^", "**")
                res = eval(expr)
                # تنسيق النتيجة
                formatted_res = f"{res:g}"
                new_display = f"{current_display}={formatted_res}"
            except Exception:
                new_display = "Error"
    else:
        # معالجة إضافة الأرقام والعمليات
        if "=" in current_display or current_display == "Error":
            if action in "+-×÷^%":
                new_display = current_display.split("=")[-1] + action
            else:
                new_display = action
        else:
            if current_display == "0":
                if action in "+-×÷^%":
                    new_display = "0"
                else:
                    new_display = action
            else:
                new_display = current_display + action

    # التحديث (تم إزالة شرط المطابقة لضمان الإرسال في حال وجود رموز مخفية)
    try:
        await event.edit(
            format_screen(new_display),
            buttons=create_pro_buttons(new_display)
        )
    except Exception:
        # في حال كان التليجرام يرفض التعديل لنفس النص
        pass
    
    # إنهاء تأثير التحميل على الزر فوراً
    await event.answer()

def create_pro_buttons(display):
    # استخدام أزرار شفافة ومنظمة
    return [
        [Button.inline("AC", data="cal_btn:AC"), Button.inline("⌫", data="cal_btn:DEL"), Button.inline("^", data="cal_btn:^"), Button.inline("÷", data="cal_btn:÷")],
        [Button.inline("7", data="cal_btn:7"), Button.inline("8", data="cal_btn:8"), Button.inline("9", data="cal_btn:9"), Button.inline("×", data="cal_btn:×")],
        [Button.inline("4", data="cal_btn:4"), Button.inline("5", data="cal_btn:5"), Button.inline("6", data="cal_btn:6"), Button.inline("-", data="cal_btn:-")],
        [Button.inline("1", data="cal_btn:1"), Button.inline("2", data="cal_btn:2"), Button.inline("3", data="cal_btn:3"), Button.inline("+", data="cal_btn:+")],
        [Button.inline("%", data="cal_btn:%"), Button.inline("0", data="cal_btn:0"), Button.inline(".", data="cal_btn:."), Button.inline("=", data="cal_btn:equal")]
    ]
