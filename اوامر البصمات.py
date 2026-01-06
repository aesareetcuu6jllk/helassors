import __main__ as main_module
from telethon import events

# ربط محرك سورس هيلاس
hellas = main_module.hellas

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^\.اوامر البصمات$"))
async def _(event):
    # إرسال قائمة الأوامر كـ رد على رسالتك قبل حذفها أو كرسالة جديدة
    await event.edit(
        "⦑ قائمة أوامر البصمات 🎧 ⦒\n"
        "★•────────────•★\n"
        "`.بصمات1`\n"
        "`.بصمات2`\n"
        "`.بصمات3`\n"
        "`.بصمات4`\n"
        "`.بصمات5`\n"
        "`.بصمات6`\n"
        "`.بصمات7`\n"
        "`.بصمات8`\n"
        "`.بصمات9`\n"
        "`.بصمات10`\n"
        "`.بصمات11`\n"
        "`.بصمات12`\n"
        "★•────────────•★\n"
        "CH : @HELLASUserBot"
    )
