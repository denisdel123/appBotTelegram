import json

from aiogram import Bot, Dispatcher, executor, types
from dotenv import load_dotenv
import os
from aiogram.types.web_app_info import WebAppInfo

load_dotenv()
bot_key = os.environ.get("BOT")
bot = Bot(bot_key)
botDP = Dispatcher(bot)


@botDP.message_handler(commands=['start'])
async def start(message: types.Message):
    markup = types.InlineKeyboardMarkup()
    btn = types.InlineKeyboardButton('Открыть веб страницу', web_app=WebAppInfo(url='https://itproger.com'))
    markup.add(btn)
    await message.answer('hello my frend', reply_markup=markup)

@botDP.message_handler(commands=['web_app_data'])
async def web_app(message: types.Message):
    res = json.loads(message.web_app_data.data)
    await message.answer(f'Name: {res["name"]}. Email: {res["email"]}. Phone: {res["phone"]}.')

    

executor.start_polling(botDP)
