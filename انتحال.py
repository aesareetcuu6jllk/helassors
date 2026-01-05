import os
import html
import asyncio
import __main__ as main_module
from telethon import functions, types, events
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.functions.channels import GetFullChannelRequest
from telethon.errors import ChatAdminRequiredError, FloodWaitError

# ربط المحرك من الملف الرئيسي
hellas = main_module.hellas

# دالة مساعدة للحذف أو التعديل (بديلة لـ edit_delete)
async def hel_edit(event, text, time=10):
    await event.edit(text)
    await asyncio.sleep(time)
    await event.delete()

# مخزن مؤقت للمعلومات الأصلية (بديل لـ sql_helper)
original_data = {}

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^\.انتحال(?:\s|$)([\s\S]*)"))
async def impersonate(event):
    me = await hellas.get_me()
    # جلب الشخص المراد انتحاله
    if event.is_reply:
        reply = await event.get_reply_message()
        user = await hellas.get_entity(reply.sender_id)
    else:
        return await hel_edit(event, "**⚠️ يجب الرد على رسالة الشخص أولاً!**")

    if user.id == 29827519: # حماية المطور (ايديك)
        return await hel_edit(event, "**❌ لا تحاول تنتحل المطور!**")

    await event.edit("**🔄 جاري عملية الانتحال...**")
    
    # حفظ المعلومات الأصلية قبل التغيير
    full_me = await hellas(GetFullUserRequest(me.id))
    original_data["fname"] = me.first_name or ""
    original_data["lname"] = me.last_name or ""
    original_data["about"] = full_me.full_user.about or ""

    # جلب معلومات الضحية
    full_victim = await hellas(GetFullUserRequest(user.id))
    v_first = user.first_name or ""
    v_last = user.last_name or ""
    v_bio = full_victim.full_user.about or ""

    # تحميل صورة الضحية
    photo = await hellas.download_profile_photo(user.id)

    try:
        # تغيير الاسم والبايو
        await hellas(functions.account.UpdateProfileRequest(
            first_name=v_first,
            last_name=v_last,
            about=v_bio
        ))
        # رفع الصورة
        if photo:
            file = await hellas.upload_file(photo)
            await hellas(functions.photos.UploadProfilePhotoRequest(file=file))
            os.remove(photo) # حذف الصورة من السيرفر بعد الرفع
        
        await hel_edit(event, "**✅ تم انتحال الحساب بنجاح!**")
    except Exception as e:
        await hel_edit(event, f"**❌ فشل الانتحال:**\n`{e}`")

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^\.اعادة$"))
async def revert_original(event):
    if "fname" not in original_data:
        return await hel_edit(event, "**⚠️ لا توجد بيانات أصلية محفوظة للعودة إليها!**")

    await event.edit("**🔄 جاري استعادة معلوماتك الأصلية...**")
    try:
        await hellas(functions.account.UpdateProfileRequest(
            first_name=original_data["fname"],
            last_name=original_data["lname"],
            about=original_data["about"]
        ))
        
        # حذف آخر صورة (صورة الضحية) للعودة للقديمة
        photos = await hellas.get_profile_photos("me", limit=1)
        if photos:
            await hellas(functions.photos.DeletePhotosRequest(id=[
                types.InputPhoto(
                    id=photos[0].id,
                    access_hash=photos[0].access_hash,
                    file_reference=photos[0].file_reference
                )
            ]))
            
        await hel_edit(event, "**✅ تم استعادة حسابك بنجاح!**")
        original_data.clear()
    except Exception as e:
        await hel_edit(event, f"**❌ فشل الاستعادة:**\n`{e}`")

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^\.انتحال_الدردشه(?:\s|$)([\s\S]*)"))
async def chat_fake(event):
    if not event.is_group and not event.is_channel:
        return await hel_edit(event, "**⚠️ هذا الأمر يعمل في المجموعات والقنوات فقط!**")

    target = event.pattern_match.group(1).strip()
    if not target:
        return await hel_edit(event, "**⚠️ أرسل يوزر القناة المراد انتحالها مع الأمر.**")

    await event.edit("**🔄 جاري انتحال الدردشة...**")
    try:
        victim_chat = await hellas(GetFullChannelRequest(target))
        current_chat = await hellas(GetFullChannelRequest(event.chat_id))

        # حفظ الأصلي
        original_data[f"{event.chat_id}_name"] = current_chat.chats[0].title
        original_data[f"{event.chat_id}_about"] = current_chat.full_chat.about or ""

        # تنفيذ الانتحال
        await hellas(functions.channels.EditTitleRequest(
            channel=event.chat_id,
            title=victim_chat.chats[0].title
        ))
        await hellas(functions.messages.EditChatAboutRequest(
            peer=event.chat_id,
            about=victim_chat.full_chat.about or ""
        ))
        
        photo = await hellas.download_profile_photo(target)
        if photo:
            file = await hellas.upload_file(photo)
            await hellas(functions.channels.EditPhotoRequest(event.chat_id, file))
            os.remove(photo)

        await hel_edit(event, "**✅ تم انتحال الدردشة بنجاح!**")
    except ChatAdminRequiredError:
        await hel_edit(event, "**❌ أحتاج صلاحيات أدمن لتغيير معلومات القناة!**")
    except Exception as e:
        await hel_edit(event, f"**❌ خطأ:** `{e}`")

@hellas.on(events.NewMessage(outgoing=True, pattern=r"^\.اعادة_الدردشه$"))
async def revert_chat(event):
    name_key = f"{event.chat_id}_name"
    if name_key not in original_data:
        return await hel_edit(event, "**⚠️ لم يتم حفظ بيانات هذه الدردشة سابقاً!**")

    await event.edit("**🔄 جاري استعادة معلومات الدردشة الأصلية...**")
    try:
        await hellas(functions.channels.EditTitleRequest(
            channel=event.chat_id,
            title=original_data[name_key]
        ))
        await hellas(functions.messages.EditChatAboutRequest(
            peer=event.chat_id,
            about=original_data[f"{event.chat_id}_about"]
        ))
        
        # حذف الصورة المنتحلة
        async for photo in hellas.iter_profile_photos(event.chat_id, limit=1):
            await hellas(functions.photos.DeletePhotosRequest(id=[
                types.InputPhoto(id=photo.id, access_hash=photo.access_hash, file_reference=photo.file_reference)
            ]))

        await hel_edit(event, "**✅ تم استعادة الدردشة بنجاح!**")
        del original_data[name_key]
    except Exception as e:
        await hel_edit(event, f"**❌ فشل الاستعادة:** `{e}`")
