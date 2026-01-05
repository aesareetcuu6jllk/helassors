import __main__ as main_module
import re
import asyncio
from telethon import events, Button

# ربط المحركات
hellas = main_module.hellas
tg_bot = main_module.tg_bot

# واجهة فخمة وشفافة
HEADER = "⚡ **𝐇𝐄𝐋𝐋𝐀𝐒 𝐒𝐔𝐏𝐄𝐑 𝐂𝐀𝐋𝐂** ⚡"
# تصميم الشاشة ليكون أخف وأسرع في المعالجة
DISPLAY_FORMAT = "```\n❱ {} \n```"

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
        title="الآلة الحاسبة الخارقة",
        text=f"{HEADER}\n{DISPLAY_FORMAT.format('0')}",
        buttons=create_pro_buttons("0")
    )
    # إرسال الرد بدون كاش لتسريع الاستجابة
    await event.answer([result], cache_time=0)

@tg_bot.on(events.CallbackQuery(data=re.compile(b"cal_btn:(.*)")))
async def handle_calc_press(event):
    action = event.data_match.group(1).decode()
    
    # استخراج سريع للنص الحالي
    try:
        # البحث عن النص بعد علامة ❱ مباشرة
        current_display = re.search(r"❱ (.*) \n", event.original_update.msg.message).group(1).strip()
    except:
        current_display = "0"

    # منطق المعالجة السريع
    if action == "AC":
        new_display = "0"
    elif action == "DEL":
        new_display = current_display[:-1] if len(current_display) > 1 else "0"
    elif action == "equal":
        try:
            expr = current_display.replace("×", "*").replace("÷", "/").replace("^", "**")
            res = eval(expr)
            new_display = f"{res:g}" # تنسيق ذكي للأرقام يزيل الأصفار الزائدة
        except:
            new_display = "Error"
    else:
        if current_display in ["0", "Error"]:
            new_display = action if action not in "+×÷^%" else "0"
        else:
            new_display = current_display + action

    # التحديث اللحظي "الطلقة"
    if new_display != current_display:
        # استخدام التعديل المباشر بدون انتظار طويل
        await event.edit(
            f"{HEADER}\n{DISPLAY_FORMAT.format(new_display)}",
            buttons=create_pro_buttons(new_display)
        )
    
    # أهم سطر للسرعة: إغلاق حالة التحميل فوراً
    await event.answer()

def create_pro_buttons(display):
    """توزيع أزرار انسيابي وسريع"""
    return [
        [Button.inline("AC", data="cal_btn:AC"), Button.inline("⌫", data="cal_btn:DEL"), Button.inline("^", data="cal_btn:^"), Button.inline("÷", data="cal_btn:÷")],
        [Button.inline("7", data="cal_btn:7"), Button.inline("8", data="cal_btn:8"), Button.inline("9", data="cal_btn:9"), Button.inline("×", data="cal_btn:×")],
        [Button.inline("4", data="cal_btn:4"), Button.inline("5", data="cal_btn:5"), Button.inline("6", data="cal_btn:6"), Button.inline("-", data="cal_btn:-")],
        [Button.inline("1", data="cal_btn:1"), Button.inline("2", data="cal_btn:2"), Button.inline("3", data="cal_btn:3"), Button.inline("+", data="cal_btn:+")],
        [Button.inline("%", data="cal_btn:%"), Button.inline("0", data="cal_btn:0"), Button.inline(".", data="cal_btn:."), Button.inline("=", data="cal_btn:equal")]
    ]
