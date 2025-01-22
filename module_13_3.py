from asyncio import create_task

import aiogram
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio

api = input('Введите token:')
bot = aiogram.Bot(token=api)
dp = aiogram.Dispatcher(bot, storage=MemoryStorage())

@dp.message_handler(commands=['start'])
async def start(message):
    task = create_task(message.answer('Это отвечает БОТ на команду Start'))

@dp.message_handler()
async def all_messages(message):
    task = create_task(message.answer('Это отвечает БОТ на любое сообщение'))

aiogram.executor.start_polling(dp, skip_updates=True)