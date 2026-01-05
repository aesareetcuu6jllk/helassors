import __main__ as main_module
import re
from telethon import events, Button

# ربط المحركات
hellas = main_module.hellas
tg_bot = main_module.tg_bot

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^\.حاسبة$"))
async def start_calc(event):
    bot_me = await tg_bot.get_me()
    results = await hellas.inline_query(bot_me.username, "calc_init")
    await results[0].click(event.chat_id)
    await event.delete()

@tg_bot.on(events.InlineQuery(pattern=r"calc_init"))
async def inline_calc(event):
    builder = event.builder
    # الشاشة تبدأ برقم 0 صافي
    result = builder.article(
        title="الآلة الحاسبة",
        text="0",
        buttons=create_pro_buttons("0")
    )
    await event.answer([result], cache_time=0)

@tg_bot.on(events.CallbackQuery(data=re.compile(b"cal_btn:(.*)")))
async def handle_calc_press(event):
    action = event.data_match.group(1).decode()
    
    # جلب النص الحالي "كما هو" بدون أي تشفير برمي
    current_display = event.original_update.msg.message.strip()

    if action == "AC":
        new_display = "0"
    elif action == "DEL":
        if "=" in current_display or current_display == "Error":
            new_display = "0"
        else:
            new_display = current_display[:-1] if len(current_display) > 1 else "0"
    elif action == "equal":
        if "=" in current_display or current_display == "Error" or current_display == "0":
            return await event.answer("أدخل أرقاماً أولاً", alert=False)
        try:
            expr = current_display.replace("×", "*").replace("÷", "/").replace("^", "**")
            res = eval(expr)
            new_display = f"{current_display}={res:g}"
        except:
            new_display = "Error"
    else:
        # إضافة الأرقام والعمليات
        if "=" in current_display or current_display == "Error":
            if action in "+-×÷^%":
                new_display = current_display.split("=")[-1] + action
            else:
                new_display = action
        else:
            if current_display == "0":
                if action in "+-×÷^%": return await event.answer()
                new_display = action
            else:
                new_display = current_display + action

    # التعديل اللحظي (بدون شروط تعجيزية)
    try:
        await event.edit(
            new_display,
            buttons=create_pro_buttons(new_display)
        )
    except Exception as e:
        print(f"Update Error: {e}")
    
    await event.answer() # ينهي حالة التحميل على الزر

def create_pro_buttons(display):
    return [
        [Button.inline("AC", data="cal_btn:AC"), Button.inline("⌫", data="cal_btn:DEL"), Button.inline("^", data="cal_btn:^"), Button.inline("÷", data="cal_btn:÷")],
        [Button.inline("7", data="cal_btn:7"), Button.inline("8", data="cal_btn:8"), Button.inline("9", data="cal_btn:9"), Button.inline("×", data="cal_btn:×")],
        [Button.inline("4", data="cal_btn:4"), Button.inline("5", data="cal_btn:5"), Button.inline("6", data="cal_btn:6"), Button.inline("-", data="cal_btn:-")],
        [Button.inline("1", data="cal_btn:1"), Button.inline("2", data="cal_btn:2"), Button.inline("3", data="cal_btn:3"), Button.inline("+", data="cal_btn:+")],
        [Button.inline("%", data="cal_btn:%"), Button.inline("0", data="cal_btn:0"), Button.inline(".", data="cal_btn:."), Button.inline("=", data="cal_btn:equal")]
    ]
