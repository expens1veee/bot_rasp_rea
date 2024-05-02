from copy import deepcopy

from aiogram import F, Router
from aiogram.filters import Command, CommandStart
from aiogram.types import CallbackQuery, Message


from rasp_rea_bot.lex.lex import LEXICON
from rasp_rea_bot.scrap.scrap import lst
from rasp_rea_bot.keyboards.buttons import create_keyboard
# from rasp_rea_bot.


router = Router()


@router.message(CommandStart())
async def procces_start_command(message: Message):
    await message.answer(LEXICON[message.text], reply_markup=create_keyboard().as_markup())


@router.message(Command(commands='help'))
async def procces_help_command(message: Message):
    await message.answer(LEXICON[message.text])



@router.message(Command(commands='rasp'))
async def procces_rasp_command(message: Message):
    await message.answer(lst.printLL())


@router.message(F.text == 'Расписание на неделю')
async def procces_rasp_command(message: Message):
    await message.answer(lst.printLL())


@router.message(F.text =='Расписание на понедельник')
async def procces_rasp_command(message: Message):
    curr = lst.head
    await message.answer(lst.print_i_elem(0))


@router.message(F.text == 'Расписание на вторник')
async def procces_rasp_command(message: Message):
    curr = lst.head
    await message.answer(lst.print_i_elem(1))


@router.message(F.text == 'Расписание на среду')
async def procces_rasp_command(message: Message):
    curr = lst.head
    await message.answer(lst.print_i_elem(2))


@router.message(F.text == 'Расписание на четверг')
async def procces_rasp_command(message: Message):
    curr = lst.head
    await message.answer(lst.print_i_elem(3))


@router.message(F.text == 'Расписание на пятницу')
async def procces_rasp_command(message: Message):
    curr = lst.head
    await message.answer(lst.print_i_elem(4))

@router.message(F.text =='Расписание на субботу')
async def procces_rasp_command(message: Message):
        curr = lst.head
        await message.answer(lst.print_i_elem(5))


@router.message()
async def send_warning(message: Message):
        await message.answer(text='Я тебя не понимаю! Используй кнопки под клавиатурой или меню')



