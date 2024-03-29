import os
import logging
from aiogram import Bot, Dispatcher, executor, types
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def echo(message: types.Message):
   await message.reply('Start')


@dp.message_handler(commands=['help'])
async def echo(message: types.Message):
   await message.reply('Вы обратились к справке бота')


if __name__ == '__main__':
   logging.basicConfig(level=logging.INFO)
   executor.start_polling(dp, skip_updates=True)