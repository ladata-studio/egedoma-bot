from aiogram import Dispatcher, Bot, types
from utils import get_random_words
from app_requests import save_hash, save_user
import os

TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
BASE_URL = os.getenv('BASE_URL')
print(TOKEN)
print(BASE_URL)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands="start")
async def start(message: types.Message):
    text = "Привет! Чтобы получить код, используй команду /getcode"
    await message.answer(text, parse_mode="Markdown")


@dp.message_handler(commands="getcode")
async def start(message: types.Message):
    password = " ".join(get_random_words(4))
    save_hash(password, message['from'])

    user_photo_file_id = await get_user_photo_file_id(message['from']['id'])
    save_user(message['from'], user_photo_file_id)
    
    text = f'👇 Вот код для входа на {BASE_URL}:\n\n`{password}`'
    await message.answer(text, parse_mode="Markdown")

    # user_photo = await bot.get_file(user_photo_file_id)
    # user_photo_temp_path = user_photo['file_path']
    # print(f"https://api.telegram.org/file/bot{TOKEN}/{user_photo_temp_path}")


async def get_user_photo_file_id(user_id):
    user_photos = await bot.get_user_profile_photos(user_id=user_id)
    if (user_photos['total_count'] > 0):
        user_photo_file_id = user_photos['photos'][0][0]['file_id']
        return user_photo_file_id
    return None
