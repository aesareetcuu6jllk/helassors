import __main__ as main_module
import re
from telethon import events, Button

# ربط المحركات
hellas = main_module.hellas
tg_bot = main_module.tg_bot

# مخزن للعمليات الحسابية (عشان ما نعتمد على قراءة الشاشة)
calc_storage = {}

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^\.حاسبة$"))
async def start_calc(event):
    bot_me = await tg_bot.get_me()
    results = await hellas.inline_query(bot_me.username, "calc_init")
    await results[0].click(event.chat_id)
    await event.delete()

@tg_bot.on(events.InlineQuery(pattern=r"calc_init"))
async def inline_calc(event):
    builder = event.builder
    # تصفير المخزن لهذا المستخدم
    calc_storage[event.sender_id] = "0"
    result = builder.article(
        title="الآلة الحاسبة الاحترافية",
        text="```\n 0 \n```",
        buttons=create_pro_buttons()
    )
    await event.answer([result], cache_time=0)

@tg_bot.on(events.CallbackQuery(data=re.compile(b"cal_btn:(.*)")))
async def handle_calc_press(event):
    action = event.data_match.group(1).decode()
    user_id = event.sender_id
    
    # جلب القيمة من المخزن، إذا مو موجودة نعتبرها 0
    current_val = str(calc_storage.get(user_id, "0"))

    if action == "AC":
        new_val = "0"
    elif action == "DEL":
        if "=" in current_val or current_val == "Error":
            new_val = "0"
        else:
            new_val = current_val[:-1] if len(current_val) > 1 else "0"
    elif action == "equal":
        if "=" in current_val or current_val == "Error" or current_display == "0":
            return await event.answer("أدخل عملية أولاً")
        try:
            # تحويل الرموز والحساب
            expr = current_val.replace("×", "*").replace("÷", "/").replace("^", "**")
            res = eval(expr)
            new_val = f"{current_val}={res:g}"
        except:
            new_val = "Error"
    else:
        # إضافة الأرقام والعمليات
        if "=" in current_val or current_val == "Error":
            if action in "+-×÷^%":
                new_val = current_val.split("=")[-1] + action
            else:
                new_val = action
        else:
            if current_val == "0":
                if action in "+-×÷^%": return await event.answer()
                new_val = action
            else:
                new_val = current_val + action

    # حفظ القيمة الجديدة في المخزن
    calc_storage[user_id] = new_val

    # تحديث الرسالة (هنا راح يشتغل غصب عن التليجرام لأننا نبعث نص جديد تماماً)
    await event.edit(
        f"```\n {new_val} \n```",
        buttons=create_pro_buttons()
    )
    await event.answer()

def create_pro_buttons():
    return [
        [Button.inline("AC", data="cal_btn:AC"), Button.inline("⌫", data="cal_btn:DEL"), Button.inline("^", data="cal_btn:^"), Button.inline("÷", data="cal_btn:÷")],
        [Button.inline("7", data="cal_btn:7"), Button.inline("8", data="cal_btn:8"), Button.inline("9", data="cal_btn:9"), Button.inline("×", data="cal_btn:×")],
        [Button.inline("4", data="cal_btn:4"), Button.inline("5", data="cal_btn:5"), Button.inline("6", data="cal_btn:6"), Button.inline("-", data="cal_btn:-")],
        [Button.inline("1", data="cal_btn:1"), Button.inline("2", data="cal_btn:2"), Button.inline("3", data="cal_btn:3"), Button.inline("+", data="cal_btn:+")],
        [Button.inline("%", data="cal_btn:%"), Button.inline("0", data="cal_btn:0"), Button.inline(".", data="cal_btn:."), Button.inline("=", data="cal_btn:equal")]
    ]
