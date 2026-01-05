import __main__ as main_module
import re
from telethon import events, Button

# ربط المحركات من الملف الرئيسي
hellas = main_module.hellas
tg_bot = main_module.tg_bot

# تصميم الواجهة
HEADER = "✨ **𝐇𝐄𝐋𝐋𝐀𝐒 𝐏𝐑𝐎 𝐂𝐀𝐋𝐂** ✨"
# استخدام النمط البرمجي لجعل الشاشة شفافة واحترافية
DISPLAY_FORMAT = "```\n┌──────────────────┐\n  {} \n└──────────────────┘\n```"

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^\.حاسبة$"))
async def start_calc(event):
    bot_me = await tg_bot.get_me()
    # تشغيل نظام الإنلاين لبدء الجلسة
    results = await hellas.inline_query(bot_me.username, "calc_init")
    await results[0].click(event.chat_id)
    await event.delete()

@tg_bot.on(events.InlineQuery(pattern=r"calc_init"))
async def inline_calc(event):
    builder = event.builder
    result = builder.article(
        title="الآلة الحاسبة الاحترافية",
        text=f"{HEADER}\n{DISPLAY_FORMAT.format('0')}",
        buttons=create_pro_buttons("0")
    )
    await event.answer([result])

@tg_bot.on(events.CallbackQuery(data=re.compile(b"cal_btn:(.*)")))
async def handle_calc_press(event):
    action = event.data_match.group(1).decode()
    
    # استخراج النص الحالي من الشاشة (بين الخطوط)
    # نستخدم regex للبحث عن المحتوى داخل صندوق العرض
    try:
        current_display = re.search(r"  (.*) \n", event.original_update.msg.message).group(1).strip()
    except:
        current_display = "0"

    if action == "AC":
        new_display = "0"
    elif action == "DEL":
        # مسح آخر رمز
        new_display = current_display[:-1] if len(current_display) > 1 else "0"
    elif action == "equal":
        try:
            # تحويل الرموز لعمليات رياضية يفهمها البايثون
            expression = current_display.replace("×", "*").replace("÷", "/").replace("^", "**")
            # حساب النتيجة
            res = eval(expression)
            # تنسيق النتيجة (تقريب إذا كانت فواصل طويلة)
            new_display = str(round(res, 5)) if isinstance(res, float) else str(res)
        except:
            new_display = "Error"
    else:
        # إذا كانت الشاشة صفر أو خطأ، نبدأ بكتابة الرقم الجديد
        if current_display in ["0", "Error"]:
            # منع تكرار العمليات في البداية
            if action in ["+", "×", "÷", "^", "%"]:
                new_display = "0"
            else:
                new_display = action
        else:
            # إضافة الرقم أو العملية بجانب النص الحالي فوراً
            new_display = current_display + action

    # التحديث اللحظي: نعدل الرسالة فقط إذا تغير المحتوى
    if new_display != current_display:
        await event.edit(
            f"{HEADER}\n{DISPLAY_FORMAT.format(new_display)}",
            buttons=create_pro_buttons(new_display)
        )
    
    # إخبار التليجرام أن الكولباك تم بنجاح لمنع ظهور علامة التحميل على الزر
    await event.answer()

def create_pro_buttons(display):
    """توزيع الأزرار بشكل شفاف ومنظم"""
    return [
        [Button.inline("AC", data="cal_btn:AC"), Button.inline("⌫", data="cal_btn:DEL"), Button.inline("^", data="cal_btn:^"), Button.inline("÷", data="cal_btn:÷")],
        [Button.inline("7", data="cal_btn:7"), Button.inline("8", data="cal_btn:8"), Button.inline("9", data="cal_btn:9"), Button.inline("×", data="cal_btn:×")],
        [Button.inline("4", data="cal_btn:4"), Button.inline("5", data="cal_btn:5"), Button.inline("6", data="cal_btn:6"), Button.inline("-", data="cal_btn:-")],
        [Button.inline("1", data="cal_btn:1"), Button.inline("2", data="cal_btn:2"), Button.inline("3", data="cal_btn:3"), Button.inline("+", data="cal_btn:+")],
        [Button.inline("%", data="cal_btn:%"), Button.inline("0", data="cal_btn:0"), Button.inline(".", data="cal_btn:."), Button.inline("=", data="cal_btn:equal")]
    ]
