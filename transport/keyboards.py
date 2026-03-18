from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def get_main_menu():
    kb = [
        [KeyboardButton(text="💤 Гибернация")],
        [KeyboardButton(text="📑 Вкладки"), KeyboardButton(text="📸 Скриншот")],
    ]

    return ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        one_time_keyboard=False,
        input_field_placeholder="Выберите действие..."
    )
