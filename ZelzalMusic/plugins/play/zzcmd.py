#▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒✯ ʑᴇʟᴢᴀʟ_ᴍᴜsɪᴄ ✯▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
#▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒✯  T.me/ZThon   ✯▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
#▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒✯ T.me/Zelzal_Music ✯▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒

import asyncio
from pyrogram import Client, filters
from strings.filters import command
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, CallbackQuery, InlineKeyboardMarkup, Message
from typing import Union
from pyrogram.types import InlineKeyboardButton
from ZelzalMusic import app
                                       
                                       
                                       
@app.on_callback_query(filters.regex("zzzback"))
async def mpdtsf(_, query: CallbackQuery):
   await query.edit_message_text(
       f"""**» مرحبـاً عـزيـزي**\n**- استخـدم الازرار بالاسفـل لـ تصفـح اوامـر الميـوزك 🥁**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "• اوامــر التشغيــل •", callback_data="zzzll"),
                ],[
                    InlineKeyboardButton(
                        "• اوامــر القنــاة •", callback_data="zzzch"),
                ],[
                    InlineKeyboardButton(
                        "• اوامــر الادمــن •", callback_data="zzzad"),
                ],
            ]
        ),
    )





@app.on_callback_query(filters.regex("zzzll"))
async def elkatob(_, query: CallbackQuery):
   await query.edit_message_text(
       f"""ٴ**•────‌‌‏✯ ʑ_ᴍᴜsɪᴄ ✯──‌‌‏─‌‌‏─•**
**- قائمــة اوامــر التشغيــل ✅ :**
ٴ**•────‌‌‏✯ ʑ_ᴍᴜsɪᴄ ✯──‌‌‏─‌‌‏─•**
تشغيل + اسم الاغنية
**- لــ تـشـغـيل اغـنـيـة فـي الـمكـالـمـة الـصـوتـيـة**
فيديو + اسم المقـطـع
**- لــ تـشـغـيل فيـديـو فـي الـمكـالـمـة المـرئيـة**
ايقاف / انهاء / اسكت
**- لـ إيقـاف تـشغـيـل الـمـوسـيـقـى فـي المكـالمـة**
وقف / توقف
**- لـ إيقـاف تشغيـل الموسيـقـى فـي المكالمـة مـؤقتـاً**
كمل / كملي
**- لـ إسـتـئـنـاف تـشغـيـل الـمـوسـيـقـى فـي المكـالمـة**
تخطي
**- لـ تخطـي الاغنيـة وتشغيـل الاغنيـة التاليـه**
ريستارت
**- لـ إعـادة تشغيـل البـوت**
بحث + الاسـم
**- لـ تحميـل الاغانـي والمقـاطـع الصوتيـه مـن اليوتيـوب**
الاغاني
**- لـ معـرفـة الاغـانـي المـوجـودة فـي قائمـة الانتظـار**
بنج
**- لـ عـرض سـرعـة تشغيـل البـوت**
ٴ**•────‌‌‏✯ ʑ_ᴍᴜsɪᴄ ✯──‌‌‏─‌‌‏─•**""",
       reply_markup=InlineKeyboardMarkup(
          [
               [
                    InlineKeyboardButton(
                        "رجـوع", callback_data="zzzback"),
               ],
          ]
        ),
    )




@app.on_callback_query(filters.regex("zzzad"))
async def zzzad(_, query: CallbackQuery):
   await query.edit_message_text(
       f"""ٴ**•────‌‌‏✯ ʑ_ᴍᴜsɪᴄ ✯──‌‌‏─‌‌‏─•**
**- قائمــة اوامــر الادمــن ✅ :**
ٴ**•────‌‌‏✯ ʑ_ᴍᴜsɪᴄ ✯──‌‌‏─‌‌‏─•**
بنج
**- لـ عـرض سـرعـة تشغيـل البـوت**
الاعدادات
**- لـ عـرض اعـدادات البــوت**
ٴ⋆┄─┄─┄─┄─┄─┄─┄─┄⋆
**- قائمــة اوامــر الـرتب ✅ :**
ٴ⋆┄─┄─┄─┄─┄─┄─┄─┄⋆
رفع ادمن
**- لـ رفـع شخـص ادمـن فـي البـوت**
تنزيل ادمن
**- لــ تـنزيل شخـص مـن قائمـة ادمنيـة البـوت**
الادمنيه
**- لـ عـرض قائمـة ادمنيـة البـوت**
ٴ**•────‌‌‏✯ ʑ_ᴍᴜsɪᴄ ✯──‌‌‏─‌‌‏─•**""",
       reply_markup=InlineKeyboardMarkup(
          [
               [
                    InlineKeyboardButton(
                        "رجـوع", callback_data="zzzback"),
               ],
          ]
        ),
    )



@app.on_callback_query(filters.regex("zzzch"))
async def zzzch(_, query: CallbackQuery):
   await query.edit_message_text(
       f"""ٴ**•────‌‌‏✯ ʑ_ᴍᴜsɪᴄ ✯──‌‌‏─‌‌‏─•**
**- قائمــة اوامــر التشغيــل فـي القنــاة ✅ :**
ٴ**•────‌‌‏✯ ʑ_ᴍᴜsɪᴄ ✯──‌‌‏─‌‌‏─•**
**- ارفـع البـوت إشـراف في القنـاة و شغـل مباشـر**
**- ارسـل (/channelplay او ربط) + يـوزر القنـاة لـ الربـط**
**- ثم استخـدم الاوامــر بالاسفـل لـ التشغيـل**
ٴ⋆┄─┄─┄─┄─┄─┄─┄─┄⋆
تشغيل + اسم الاغنية
**- لــ تـشـغـيل اغـنـيـة فـي الـمكـالـمـة الـصـوتـيـة**
فيديو + اسم المقـطـع
**- لــ تـشـغـيل فيـديـو فـي الـمكـالـمـة المـرئيـة**
ايقاف / انهاء / اسكت
**- لـ إيقـاف تـشغـيـل الـمـوسـيـقـى فـي المكـالمـة**
وقف / توقف
**- لـ إيقـاف تشغيـل الموسيـقـى فـي المكالمـة مـؤقتـاً**
كمل / استئناف
**- لـ إسـتـئـنـاف تـشغـيـل الـمـوسـيـقـى فـي المكـالمـة**
تخطي
**- لـ تخطـي الاغنيـة وتشغيـل الاغنيـة التاليـه**
ٴ⋆┄─┄─┄─┄─┄─┄─┄─┄⋆
/seek + عـدد الثـوانـي
**- لـ تقديـم الاغنيـه لـ الامـام**
/seekback + عـدد الثـوانـي
**- لـ إرجـاع الاغنيـه لـ الخـلف**
ٴ**•────‌‌‏✯ ʑ_ᴍᴜsɪᴄ ✯──‌‌‏─‌‌‏─•**""",
       reply_markup=InlineKeyboardMarkup(
          [
               [
                    InlineKeyboardButton(
                        "رجـوع", callback_data="zzzback"),
               ],
          ]
        ),
    )
