from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message, ReplyKeyboardRemove
from loader import dp
from keyboards.default import menu

@dp.message_handler(Command("start"))
async def show_menu(message:Message):
    await message.answer("Hi user!", reply_markup=menu)

@dp.message_handler(Text(equals=["Aizhan", "Asem", "Dina", "Ulbosh", "Merey", "Yuki", "Aruzhan"]))
async def get_food(message:Message):
    await message.answer(f"Hello {message.text}. Welcome",
                         reply_markup=ReplyKeyboardRemove())

