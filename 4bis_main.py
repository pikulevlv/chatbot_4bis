import logging
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.utils import executor

from config import TOKEN
logging.basicConfig(level=logging.DEBUG)

bot = Bot(TOKEN)
dp = Dispatcher(bot)

loggingmiddleware = LoggingMiddleware()
dp.middleware.setup(loggingmiddleware)

if __name__ == '__main__':
    print("token: ", TOKEN)
    executor.start_polling(dp)
