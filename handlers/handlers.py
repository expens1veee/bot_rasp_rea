from copy import deepcopy

from aiogram import F, Router
from aiogram.filters import Command, CommandStart
from aiogram.types import CallbackQuery, Message

from rasp_rea_bot.lex.lex import LEXICON
from rasp_rea_bot.scrap.scrap import lst
from rasp_rea_bot.keyboards.buttons import create_keyboard
from rasp_rea_bot.scrap.linked_list import LinkedList
from rasp_rea_bot.scrap.scrap import rasp



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



# @router.message(Command(commands='Расписание на понедельник'))
# async def procces_rasp_command(message: Message):
#     await message.answer(lst.data)


@router.message(Command(commands='Расписание на вторник'))
async def procces_rasp_command(message: Message):
    await message.answer(lst.printLL())


@router.message(Command(commands='Расписание на среду'))
async def procces_rasp_command(message: Message):
    await message.answer(lst.printLL())


@router.message(Command(commands='Расписание на четверг'))
async def procces_rasp_command(message: Message):
    await message.answer(lst.printLL())


@router.message(Command(commands='Расписание на пятницу'))
async def procces_rasp_command(message: Message):
    await message.answer(lst.printLL())


@router.message(Command(commands='Расписание на субботу'))
async def procces_rasp_command(message: Message):
    await message.answer(lst.printLL())


@router.message()
async def send_echo(message: Message):
    if message.text == 'Расписание на неделю':
        await message.answer(lst.printLL())
    if message.text == 'Расписание на понедельник':
        curr = lst.head
        await message.answer(curr.data)
    # await message.send_copy(chat_id=message.chat.id)
    if message.text == 'Расписание на вторник':
        curr = lst.head
        await message.answer(curr.next.data)
    if message.text == 'Расписание на среду':
        curr = lst.head
        await message.answer(curr.next.next.data)
    if message.text == 'Расписание на четверг':
        curr = lst.head
        await message.answer(curr.next.next.next.data)
    if message.text == 'Расписание на пятницу':
        curr = lst.head
        await message.answer(curr.next.next.next.next.data)
    if message.text == 'Расписание на субботу':
        curr = lst.head
        await message.answer(curr.next.next.next.next.next.data)



