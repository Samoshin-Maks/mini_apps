from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import Command
import asyncio

API_TOKEN = '7625539703:AAF7nDtV5vndTY2pqREfTkqO4oTv7D13S1Q'

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def cmd_start(message: Message):
    await message.answer("Привет! Нажми кнопку, чтобы пройти тест.")

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())