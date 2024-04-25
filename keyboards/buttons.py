from aiogram.types import (KeyboardButton, Message, ReplyKeyboardMarkup, ReplyKeyboardRemove, )
from aiogram.utils.keyboard import ReplyKeyboardBuilder






def create_keyboard():
    kb_builder = ReplyKeyboardBuilder()


    day = ['неделю','понедельник','вторник','среду','четверг','пятницу','субботу']

    buttons : list[KeyboardButton] = [
        KeyboardButton(text=f'Расписание на {i}') for i in day
    ]



    kb_builder.row(*buttons,width=1);
    return kb_builder

# button_1 = KeyboardButton(text='расписание на неделю')
# button_2 = KeyboardButton(text='расписание на понедельник')
# button_3 = KeyboardButton(text='расписание на вторник')
# button_4 = KeyboardButton(text='расписание на среду')
# button_5 = KeyboardButton(text='расписание на четверг')
# button_6 = KeyboardButton(text='расписание на пятницу')
# button_7 = KeyboardButton(text='расписание на субботу')


