import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
from aiogram.filters import Command

API_TOKEN = '7625539703:AAF7nDtV5vndTY2pqREfTkqO4oTv7D13S1Q'

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def cmd_start(message: Message):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(
                text="Пройти тест",
                web_app=WebAppInfo(url="https://mini-apps-ebon.vercel.app/main.html")
            )
        ]
    ])
    await message.answer("Привет! Нажми кнопку, чтобы пройти тест.", reply_markup=keyboard)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())