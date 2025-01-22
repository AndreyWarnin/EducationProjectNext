import aiogram
from aiogram.contrib.fsm_storage.memory import MemoryStorage

api = input('Введите token:')
bot = aiogram.Bot(token=api)
dp = aiogram.Dispatcher(bot, storage=MemoryStorage())

@dp.message_handler(commands=['start'])
async def start(message):
    print('Привет! Я бот помогающий твоему здоровью.')

@dp.message_handler()
async def all_messages(message):
    print('Введите команду /start, чтобы начать общение.')

aiogram.executor.start_polling(dp, skip_updates=True)