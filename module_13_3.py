from asyncio import create_task

import aiogram
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio

api = input('Введите token:')
bot = aiogram.Bot(token=api)
dp = aiogram.Dispatcher(bot, storage=MemoryStorage())

@dp.message_handler(commands=['start'])
async def start(message):
    task = create_task(message.answer('Привет! Я бот помогающий твоему здоровью.'))

@dp.message_handler()
async def all_messages(message):
    task = create_task(message.answer('Введите команду /start, чтобы начать общение.'))

aiogram.executor.start_polling(dp, skip_updates=True)