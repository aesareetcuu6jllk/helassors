import __main__ as main_module
import re
from telethon import events, Button

# ربط المحركات
hellas = main_module.hellas
tg_bot = main_module.tg_bot

# شاشة نظيفة جداً
DISPLAY_FORMAT = "```\n {} \n```"

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
        title="الآلة الحاسبة السريعة",
        text=DISPLAY_FORMAT.format('0'),
        buttons=create_pro_buttons("0")
    )
    await event.answer([result], cache_time=0)

@tg_bot.on(events.CallbackQuery(data=re.compile(b"cal_btn:(.*)")))
async def handle_calc_press(event):
    action = event.data_match.group(1).decode()
    
    # الطريقة الأضمن لجلب النص الحالي بدون أخطاء regex
    raw_text = event.original_update.msg.message
    current_display = raw_text.strip().replace('```', '').strip()

    if action == "AC":
        new_display = "0"
    elif action == "DEL":
        if "=" in current_display: # إذا كانت نتيجة، المسح يصفر الشاشة
            new_display = "0"
        else:
            new_display = current_display[:-1] if len(current_display) > 1 else "0"
    elif action == "equal":
        if "=" in current_display or current_display == "Error":
            new_display = current_display
        else:
            try:
                # استبدال الرموز ليفهمها المحرك الرياضي
                expr = current_display.replace("×", "*").replace("÷", "/").replace("^", "**")
                res = eval(expr)
                # تنسيق النتيجة بشكل جميل (بدون أصفار زائدة)
                formatted_res = f"{res:g}"
                new_display = f"{current_display}={formatted_res}"
            except:
                new_display = "Error"
    else:
        # إذا كنت كاتب عملية وانتهت بالنتيجة (مثل 5+5=10) وضغطت رقم جديد، يبدأ سطر جديد
        if "=" in current_display or current_display == "Error":
            if action in "+-×÷^%": # يكمل على النتيجة السابقة
                new_display = current_display.split("=")[-1] + action
            else: # يبدأ عملية جديدة تماماً
                new_display = action
        else:
            if current_display == "0":
                if action in "+-×÷^%": 
                    new_display = "0" # لا يبدأ بعملية حسابية
                else:
                    new_display = action
            else:
                new_display = current_display + action

    # التعديل اللحظي (السرعة القصوى)
    if new_display != current_display:
        await event.edit(
            DISPLAY_FORMAT.format(new_display),
            buttons=create_pro_buttons(new_display)
        )
    
    await event.answer()

def create_pro_buttons(display):
    return [
        [Button.inline("AC", data="cal_btn:AC"), Button.inline("⌫", data="cal_btn:DEL"), Button.inline("^", data="cal_btn:^"), Button.inline("÷", data="cal_btn:÷")],
        [Button.inline("7", data="cal_btn:7"), Button.inline("8", data="cal_btn:8"), Button.inline("9", data="cal_btn:9"), Button.inline("×", data="cal_btn:×")],
        [Button.inline("4", data="cal_btn:4"), Button.inline("5", data="cal_btn:5"), Button.inline("6", data="cal_btn:6"), Button.inline("-", data="cal_btn:-")],
        [Button.inline("1", data="cal_btn:1"), Button.inline("2", data="cal_btn:2"), Button.inline("3", data="cal_btn:3"), Button.inline("+", data="cal_btn:+")],
        [Button.inline("%", data="cal_btn:%"), Button.inline("0", data="cal_btn:0"), Button.inline(".", data="cal_btn:."), Button.inline("=", data="cal_btn:equal")]
    ]
