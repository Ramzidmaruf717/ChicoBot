from aiogram import types
from loader import dp
from keyboards.default.users import *


@dp.message_handler(commands="chicco")
async def cars_command_handler(msg: types.Message):
    text = f"Chicco funksiyasi ishga tushdi"
    await msg.answer(text=text, reply_markup=chicco_main_menu)


@dp.message_handler(text="Krovatlar")
async def stroller_command_handler(msg: types.Message):
    text = f"ozizga mosini tanlang"
    await msg.answer(text=text, reply_markup=bed_menu)


@dp.message_handler(text="Belanchak")
async def stroller_command_handler(msg: types.Message):
    text = f"Belanchaklar haqida malumot olish uchun +998901869380 nomeriga murofat qiling \n\n yoki @Maruf717 telegramiga murojat qiling"
    await msg.answer(text=text)


@dp.message_handler(text="hodunok")
async def stroller_command_handler(msg: types.Message):
    text = f"ozizga mosini tanlang"
    await msg.answer(text=text, reply_markup=hodunok_menu)


@dp.message_handler(text="Kolyaskalar")
async def stroller_command_handler(msg: types.Message):
    text = f"ozizga mosini tanlang"
    await msg.answer(text=text, reply_markup=stroller_menu)





