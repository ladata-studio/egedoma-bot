from aiogram import Dispatcher, Bot, types
from utils import get_random_words
import os

TOKEN = os.environ.get('TELEGRAM_BOT_TOKEN')
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands="start")
async def start(message: types.Message):
  text = "Привет! Чтобы получить код, используй команду /getcode"
  await message.answer(text, parse_mode="Markdown")


@dp.message_handler(commands="getcode")
async def start(message: types.Message):
  #  generate hash and sent it to the server with user_data
  password = " ".join(get_random_words(4))
  text = f'👇 Вот код для входа на 127.0.0.1:8000:\n\n`{password}`'
  await message.answer(text, parse_mode="Markdown")