from loader import dp
from aiogram import types
from keyboards.default.users import *


# 0rtga menyusi
@dp.message_handler(text="hodunoklar menyusiga qaytish")
async def stroller_command_handler(msg: types.Message):
    text = f"ortga qattingiz"
    await msg.answer(text=text,reply_markup=hodunok_menu)

@dp.message_handler(text="setlar menyusiga qaytish")
async def stroller_command_handler(msg: types.Message):
    text = f"ortga qattingiz"
    await msg.answer(text=text,reply_markup=set_menu)


@dp.message_handler(text="hodunoklar Menyusiga qaytish")
async def stroller_command_handler(msg: types.Message):
    text = f"ortga qattingiz"
    await msg.answer(text=text,reply_markup=hodunok_menu)

@dp.message_handler(text="Bosh Menyusiga qaytish")
async def stroller_command_handler(msg: types.Message):
    text = f"ortga qattingiz"
    await msg.answer(text=text,reply_markup=chicco_main_menu)

@dp.message_handler(text="Mahsulotlar Menyusiga qaytish")
async def stroller_command_handler(msg: types.Message):
    text = f"ortga qattingiz"
    await msg.answer(text=text,reply_markup=globalic_menu)

@dp.message_handler(text="Oyinchoqlar Menyusiga qaytish")
async def stroller_command_handler(msg: types.Message):
    text = f"ortga qattingiz"
    await msg.answer(text=text,reply_markup=toys_main_menu)


@dp.message_handler(text="belanchaklar menyusiga qaytish")
async def stroller_command_handler(msg: types.Message):
    text = f"ortga qattingiz"
    await msg.answer(text=text,reply_markup=belanchak_menu)


@dp.message_handler(text="krovatlar menyusiga qaytish")
async def stroller_command_handler(msg: types.Message):
    text = f"ortga qattingiz"
    await msg.answer(text=text,reply_markup=bed_menu)


@dp.message_handler(text="Menyuga qaytish")
async def stroller_command_handler(msg: types.Message):
    text = f"ortga qaytingiz"
    await msg.answer(text=text,reply_markup=chicco_main_menu)


@dp.message_handler(text="kolyaskalar menyusiga qaytish")
async def stroller_command_handler(msg: types.Message):
    text = f"ortga qattingiz"
    await msg.answer(text=text,reply_markup=stroller_menu)
