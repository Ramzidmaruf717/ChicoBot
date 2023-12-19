from loader import dp
from aiogram import types
from keyboards.default.users import *

#Mahsulotlar Bosilganda Hamma narsa chiqadigan funksiyani ishlatamiz

@dp.message_handler(text="Mahsulotlar")
async def main_buttons_handler(msg: types.message):
    text = "bosh menyusiga hush kelibsiz"
    await msg.answer(text=text,reply_markup=chicco_main_menu)

@dp.message_handler(text="Kiyimlar")
async def main_buttons_handler(msg: types.message):
    text = "Kiyimlarni turini va narxini kormoqchi bolsangiz @Maruf717 telegramiga murojat qiling"
    await msg.answer(text=text)

@dp.message_handler(text="Yumshoq Oyinchoqlar")
async def main_buttons_handler(msg: types.message):
    text = "yumshoq oyinchoqlarni turini va narxini kormoqchi bolsangiz @Maruf717 telegramiga murojat qiling"
    await msg.answer(text=text)



@dp.message_handler(text="Qog'irchoqlar")
async def main_buttons_handler(msg: types.message):
    text = "qog'irchoqlar menyusiga hush kelibsiz"
    await msg.answer(text=text,reply_markup=dolls_main_menu)

@dp.message_handler(text="Oyinchoqlar")
async def toy_buttons_handler(msg: types.message):
    text = "oyinchoqlar menyusiga hush kelibsiz"
    await msg.answer(text=text,reply_markup=toys_main_menu)


@dp.message_handler(text="Moshinalar")
async def toy_buttons_handler(msg: types.message):
    text = "moshinalar menyusiga hush kelibsiz"
    await msg.answer(text=text,reply_markup=cars_main_menu)


@dp.message_handler(text="qog'irchoqlar")
async def toy_buttons_handler(msg: types.message):
    text = "qog'irchoqlar menyusiga hush kelibsiz"
    await msg.answer(text=text,reply_markup=dolls_main_menu)

@dp.message_handler(text="Akkumulatorli Moshinalar")
async def toy_buttons_handler(msg: types.message):
    text = " akkumulatorli moshinalar menyusiga hush kelibsiz"
    await msg.answer(text=text, reply_markup=battery_cars_main_menu)


@dp.message_handler(text="Har Hil Setlar")
async def toy_buttons_handler(msg: types.message):
    text = "Setlar menyusiga hush kelibsiz"
    await msg.answer(text=text,reply_markup=set_menu)

#hodunoklar
@dp.message_handler(text="chicco 4-in-1")
async def stroller_command_handler(msg: types.Message):
    text = f"rasmini kormoqchi bolsangiz @Maruf717 telegramiga murojat qiling "
    await msg.answer(text=text,reply_markup=hodunok_back_menu)

@dp.message_handler(text="chicco 2-in-1")
async def stroller_command_handler(msg: types.Message):
    text = f"rasmini kormoqchi bolsangiz @Maruf717 telegramiga murojat qiling"
    await msg.answer(text=text,reply_markup=hodunok_back_menu)

@dp.message_handler(text="chicco-balance-bike")
async def stroller_command_handler(msg: types.Message):
    text = f"rasmini kormoqchi bolsangiz @Maruf717 telegramiga murojat qiling"
    await msg.answer(text=text,reply_markup=hodunok_back_menu)

@dp.message_handler(text="chicco 3-in-1")
async def stroller_command_handler(msg: types.Message):
    text = f"rasmini kormoqchi bolsangiz @Maruf717 telegramiga murojat qiling"
    await msg.answer(text=text ,reply_markup=hodunok_back_menu)



#krovatlar

@dp.message_handler(text="piere cardin bed")
async def stroller_command_handler(msg: types.Message):
    text = f"rasmini kormoqchi bolsangiz @Maruf717 telegramiga murojat qiling"
    await msg.answer(text=text,reply_markup=krovatlar_back_menu)


@dp.message_handler(text="hauck-mini-bed")
async def stroller_command_handler(msg: types.Message):
    text = f"rasmini kormoqchi bolsangiz @Maruf717 telegramiga murojat qiling"
    await msg.answer(text=text,reply_markup=krovatlar_back_menu)

@dp.message_handler(text="Mon-bed")
async def stroller_command_handler(msg: types.Message):
    text = f"rasmini kormoqchi bolsangiz @Maruf717 telegramiga murojat qiling"
    await msg.answer(text=text ,reply_markup=krovatlar_back_menu)

@dp.message_handler(text="chicco-bed")
async def stroller_command_handler(msg: types.Message):
    text = f"rasmini kormoqchi bolsangiz @Maruf717 telegramiga murojat qiling"
    await msg.answer(text=text,reply_markup=krovatlar_back_menu)


@dp.message_handler(text="cam-bed")
async def stroller_command_handler(msg: types.Message):
    text = f"rasmini kormoqchi bolsangiz @Maruf717 telegramiga murojat qiling"
    await msg.answer(text=text,reply_markup=krovatlar_back_menu)

#belanchaklar

@dp.message_handler(text="piere-cardin-belanchak")
async def stroller_command_handler(msg: types.Message):
    text = f"rasmini kormoqchi bolsangiz @Maruf717 telegramiga murojat qiling"
    await msg.answer(text=text,reply_markup=belanchak_back_menu)

@dp.message_handler(text="hauck-belanchak")
async def stroller_command_handler(msg: types.Message):
    text = f"rasmini kormoqchi bolsangiz @Maruf717 telegramiga murojat qiling"
    await msg.answer(text=text,reply_markup=belanchak_back_menu)

@dp.message_handler(text="Mon-belanchak")
async def stroller_command_handler(msg: types.Message):
    text = f"rasmini kormoqchi bolsangiz @Maruf717 telegramiga murojat qiling"
    await msg.answer(text=text,reply_markup=belanchak_back_menu)

@dp.message_handler(text="chicco-belanchak")
async def stroller_command_handler(msg: types.Message):
    text = f"rasmini kormoqchi bolsangiz @Maruf717 telegramiga murojat qiling"
    await msg.answer(text=text,reply_markup=belanchak_back_menu)


@dp.message_handler(text="fisher-price")
async def stroller_command_handler(msg: types.Message):
    text = f"rasmini kormoqchi bolsangiz @Maruf717 telegramiga murojat qiling"
    await msg.answer(text=text,reply_markup=belanchak_back_menu)


#setlar menyusini ishlatamiz
@dp.message_handler(text="Manikur")
async def manikure_handler(msg:types.Message):
    text = "rasmini kormoqchi bolsangiz @Maruf717 telegramiga murojat qiling"
    await msg.answer(text=text)


@dp.message_handler(text="Doctor")
async def manikure_handler(msg:types.Message):
    text = "rasmini kormoqchi bolsangiz @Maruf717 telegramiga murojat qiling"
    await msg.answer(text=text)


@dp.message_handler(text="Kitchen")
async def manikure_handler(msg:types.Message):
    text = "rasmini kormoqchi bolsangiz @Maruf717 telegramiga murojat qiling"
    await msg.answer(text=text)


@dp.message_handler(text="Kosmetika")
async def manikure_handler(msg:types.Message):
    text = "rasmini kormoqchi bolsangiz @Maruf717 telegramiga murojat qiling"
    await msg.answer(text=text)



#qog'irchoqlar
@dp.message_handler(text="yumshoq qog'irchoqlar")
async def doll_handler(msg:types.Message):
    text = "rasmini kormoqchi bolsangiz @Maruf717 telegramiga murojat qiling"
    await msg.answer(text=text)


@dp.message_handler(text="Realistichniy qog'irchoqlar")
async def doll_handler(msg:types.Message):
    text = "rasmini kormoqchi bolsangiz @Maruf717 telegramiga murojat qiling"
    await msg.answer(text=text)


@dp.message_handler(text="chozinchoq qog'irchoqlar")
async def doll_handler(msg:types.Message):
    text = "rasmini kormoqchi bolsangiz @Maruf717 telegramiga murojat qiling"
    await msg.answer(text=text)

@dp.message_handler(text="Koynakli Qog'irchoqlar")
async def doll_handler(msg:types.Message):
    text = "rasmini kormoqchi bolsangiz @Maruf717 telegramiga murojat qiling"
    await msg.answer(text=text)
#battery ishlatish
@dp.message_handler(text="Range Rover")
async def batteryt_handler(msg:types.Message):
    text="rasmini kormoqchi bolsangiz @Maruf717 telegramiga murojat qiling"
    await msg.answer(text=text)

@dp.message_handler(text="Lexus")
async def batteryt_handler(msg:types.Message):
    text="rasmini kormoqchi bolsangiz @Maruf717 telegramiga murojat qiling"
    await msg.answer(text=text)


@dp.message_handler(text="Mersedes")
async def batteryt_handler(msg:types.Message):
    text="rasmini kormoqchi bolsangiz @Maruf717 telegramiga murojat qiling"
    await msg.answer(text=text)


@dp.message_handler(text="Audi")
async def batteryt_handler(msg:types.Message):
    text="rasmini kormoqchi bolsangiz @Maruf717 telegramiga murojat qiling"
    await msg.answer(text=text)

#moshinalar buttonlarini ishlatamiz
@dp.message_handler(text="Rally Moshinasi")
async def car_handler(msg:types.Message):
    text="rasmini kormoqchi bolsangiz @Maruf717 telegramiga murojat qiling"
    await msg.answer(text=text)

@dp.message_handler(text="Hummer Vezdehod")
async def car_handler(msg:types.Message):
    text="rasmini kormoqchi bolsangiz @Maruf717 telegramiga murojat qiling"
    await msg.answer(text=text)

@dp.message_handler(text="Buggy Vezdehod")
async def car_handler(msg:types.Message):
    text="rasmini kormoqchi bolsangiz @Maruf717 telegramiga murojat qiling"
    await msg.answer(text=text)

@dp.message_handler(text="Chaqaloqlar uchun moshinalar")
async def car_handler(msg:types.Message):
    text="rasmini kormoqchi bolsangiz @Maruf717 telegramiga murojat qiling"
    await msg.answer(text=text)


