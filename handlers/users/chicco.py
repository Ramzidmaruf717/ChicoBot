from aiogram import types
from aiogram.dispatcher import FSMContext
from states.user import RegisterState
from loader import dp
from keyboards.default.users import *
from aiogram.types import ReplyKeyboardRemove
from utils.db_api.user_commands import *
from handlers.users.companies import *
from handlers.users.products import *
from handlers.users.backs import *


@dp.message_handler(commands="chicco")
async def cars_command_handler(msg: types.Message):
    text = f"Chicco funksiyasi ishga tushdi"
    await msg.answer(text=text, reply_markup=globalic_menu)


@dp.message_handler(commands="admin")
async def cars_command_handler(msg: types.Message):
    text = f"agar kamchilingiz bolsa @ramzid_mar telegramiga murojat qiling"
    await msg.answer(text=text)




#Sotib Olish Tugmasini Ishlatamiz

@dp.message_handler(text="Sotib Olmoqchiman")
async def stroller_command_handler(msg: types.Message):
    text = f"Sotib Olish uchun +998901869380 nomeriga murojan qiling \n\n  yoki @Maruf717 telegramiga murojat qiling"
    await msg.answer(text=text,reply_markup=main_back_menu)


