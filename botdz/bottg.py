import random
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.filters import Command
from dotenv import load_dotenv
import os

load_dotenv()
bot = Bot(os.getenv('TOKEN'))
dp = Dispatcher()

menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Камень"), KeyboardButton(text="Ножницы"), KeyboardButton(text="Бумага")]
    ],
    resize_keyboard=True,
)

@dp.message(Command("start"))
async def start_game(message: types.Message):
    await message.answer("Давай сыграем в 'Камень, ножницы, бумага'. Выбери ход:", reply_markup=menu)

@dp.message(lambda msg: msg.text in ["Камень", "Ножницы", "Бумага"])
async def play_game(message: types.Message):
    user_choice = message.text
    bot_choice = random.choice(["Камень", "Ножницы", "Бумага"])
    result = (
        "Ничья" if user_choice == bot_choice else
        "Вы победили" if (user_choice, bot_choice) in [("Камень", "Ножницы"), ("Ножницы", "Бумага"), ("Бумага", "Камень")] else
        "Вы проиграли"
    )
    await message.answer(f"Вы выбрали: {user_choice}\nБот выбрал: {bot_choice}\nРезультат: {result}")

async def main():
    print("Бот запущен")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
