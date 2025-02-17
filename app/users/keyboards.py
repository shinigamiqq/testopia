from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
)

MAIN_MENU_KB = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Мои чек-листы 📝"),
            KeyboardButton(text="Мои устройства 📱"),
        ],
        [
            KeyboardButton(text="Статистика 📊"),
        ],
    ],
    resize_keyboard=True,
)
