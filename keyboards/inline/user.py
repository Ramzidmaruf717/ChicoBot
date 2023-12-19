from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton

work_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Subscribe",url="https://t.me/mytestbotramziddin"),
            InlineKeyboardButton(text="tekshirish",callback_data="check")
        ]
    ]
)
