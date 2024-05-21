from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardMarkup, InlineKeyboardButton)
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

# main = ReplyKeyboardMarkup(keyboard=[
#     [KeyboardButton(text="Каталог"), KeyboardButton(text="Контакты")],
#     [KeyboardButton(text="Корзина")]
# ],
#     resize_keyboard=True,
#     input_field_placeholder="Выберите пункт меню"
# )
main = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Каталог", callback_data="catalog"),
     InlineKeyboardButton(text="Контакты", callback_data="contacts")],
    [InlineKeyboardButton(text="Корзина", callback_data="bin")]
])


settings = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="YT", url="youtube.com")]
])

cars = ["1", "2", "3"]


async def inline_cars():
    keyboard = InlineKeyboardBuilder()
    for car in cars:
        keyboard.add(InlineKeyboardButton(text=car, url="youtube.com"))
    return keyboard.adjust(2).as_markup()

