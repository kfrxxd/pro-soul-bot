import asyncio

from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo

TOKEN = "8344609605:AAGYwgD-pM16JKDEAh9KpKfm9DZsiCuYFIo"

bot = Bot(token=TOKEN)
dp = Dispatcher()


@dp.message(CommandStart())
async def start(message: types.Message):

    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="Открыть приложение",
                    web_app=WebAppInfo(
                        url="https://t.me/pro_soulBot/pro_soul"
                    )
                )
            ]
        ]
    )

    await message.answer(
        "Добро пожаловать ✨\n\nНажми кнопку ниже чтобы открыть приложение.",
        reply_markup=keyboard
    )


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())