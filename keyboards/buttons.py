from aiogram.types import (KeyboardButton, Message, ReplyKeyboardMarkup, ReplyKeyboardRemove, )
from aiogram.utils.keyboard import ReplyKeyboardBuilder


def create_keyboard():
    kb_builder = ReplyKeyboardBuilder()

    day = ['неделю', 'понедельник', 'вторник', 'среду', 'четверг', 'пятницу', 'субботу']

    buttons: list[KeyboardButton] = [
        KeyboardButton(text=f'Расписание на {i}') for i in day
    ]

    kb_builder.row(*buttons, width=1)
    return kb_builder




