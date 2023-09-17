from aiogram import Bot,Dispatcher,types
from aiogram.filters import CommandStart
from asyncio import run
from random import choice
bot = Bot("6544520354:AAE8bo_AKRwxH9k2tmAo8jeulWzC73Xi86w")
dp = Dispatcher()
@dp.message(CommandStart())
async def Assalomualaykum(msg:types.Message):
    await msg.answer("VaalekumAssalom")
@dp.message()
async def echo(msg:types.Message):
    text = msg.text
    if text.lower() in ['AssalomuAlaykum', "qalesa", "nima gap"]:
        await msg.answer(choise(["VaalekumAssalom", "Zo'r"]))
async def main():
    await dp.start_polling(bot)
run(main())