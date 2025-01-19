from aiogram.types import ReplyKeyboardMarkup,KeyboardButton,InlineKeyboardMarkup,InlineKeyboardButton

menyu=ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="kiyimlar"),KeyboardButton(text="mevalar")],
        [KeyboardButton(text="shlapalar"),KeyboardButton(text="oyoq kiyimlar")]
    ],
    resize_keyboard=True,
)
meva=InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Olma",callback_data="olma"),InlineKeyboardButton(text="Anor",callback_data="anor")],
        [InlineKeyboardButton(text="Banan", callback_data="banan"),InlineKeyboardButton(text="Nok", callback_data="nok")],

    ]
)
olma=InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Qizil olma",callback_data="qizil olma"),InlineKeyboardButton(text="Yashil olma" ,callback_data="yashil olma")]
    ]
)


