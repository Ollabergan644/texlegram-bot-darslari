import asyncio
from gc import callbacks

from aiogram import Bot, Dispatcher,types,F
from aiogram.filters import Command
from button import *

from button import menyu

bot = Bot(token="8073848134:AAFEVrwF28p8oipGq1chtH4BRYvwGe5R5w8")
dp = Dispatcher()

@dp.message(Command("start"))
async def cmd_start(message:types.Message):
    await message.answer("Botga hush kelibsiz",reply_markup=menyu)

@dp.message(F.text=="kiyimlar")
async def cmd_kiyimlar(message:types.Message):
    await message.answer_photo(photo="https://ae04.alicdn.com/kf/S4873c319bc8e46c6ac6ac2bf5d2353acY.jpg",caption="Tanlang",reply_markup=menyu)
@dp.message(F.text=="mevalar")
async def cmd_meva(message:types.Message):
    await message.answer_photo(photo="https://img-s1.onedio.com/id-5a76cf5ac543b4f524a788da/rev-0/w-1200/h-792/f-jpg/s-9f715fb62d5aa6b3996a99c29d2f72766fedd496.jpg",caption="mevani tanlang",reply_markup=meva)
    await message.delete()

@dp.callback_query(F.data=="olma")
async def cmd_olma(callback:types.CallbackQuery):
    await callback.message.answer_photo(photo="https://svetofornadom.ru/upload/iblock/220/kv09u7s9q18jzo9aqw0bgmjfexhced1k/apples.jpg",reply_markup=olma)
    await callback.message.delete()

sadsaddfsaasasdas

asdsadsadasd


asd
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
