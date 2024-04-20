from copy import deepcopy

from aiogram import F, Router
from aiogram.filters import Command, CommandStart
from aiogram.types import CallbackQuery, Message

from rasp_rea_bot.lex.lex import LEXICON
from rasp_rea_bot.scrap.scrap import lst
from rasp_rea_bot.scrap.linked_list import LinkedList
from rasp_rea_bot.scrap.scrap import rasp



router = Router()


@router.message(CommandStart())
async def procces_start_command(message: Message):
    await message.answer(LEXICON[message.text])


@router.message(Command(commands='help'))
async def procces_help_command(message: Message):
    await message.answer(LEXICON[message.text])



@router.message(Command(commands='rasp'))
async def procces_rasp_command(message: Message):
    await message.answer(lst.printLL())


@router.message()
async def send_echo(message: Message):
    await message.send_copy(chat_id=message.chat.id)



