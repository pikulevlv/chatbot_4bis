# pip3 install aiogram
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.utils import executor
from aiogram.types import ContentTypes
from config import TOKEN
import logging
from pathlib import Path
import keyboards as kb
from states import TestStates
import requests
import aiohttp
import asyncio

import reqs

BOT_DIR = Path(__file__).resolve().parent
STICKERS_DIR: Path = BOT_DIR / "stickers"
STICKERS_DIR.mkdir(exist_ok=True)

logging.basicConfig(level=logging.DEBUG)

bot = Bot(TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())

logging_middleware = LoggingMiddleware()
dp.middleware.setup(logging_middleware)

BOT_STATES=TestStates()
USER_STATES = {}

u = 'Интеграция'
p = 'q12345'
url = 'http://37.19.1.247/4bis_itilium_dev3/ru_RU/hs/Telegram/info/order?order='

@dp.message_handler(commands=['menu'])
async def process_command_2(message: types.Message):
    await message.reply("Выберите пункт меню", reply_markup=kb.inline_kb_full)


@dp.callback_query_handler(lambda c: c.data == 'button1')
async def process_callback_button1(callback_query: types.CallbackQuery):
    USER_STATES[callback_query.from_user.id]=BOT_STATES.TEST_STATE_1
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'Введите номер обращения (например: 000032387')



@dp.callback_query_handler(lambda c: c.data == 'button2')
async def process_callback_button2(callback_query: types.CallbackQuery):
    USER_STATES[callback_query.from_user.id]=BOT_STATES.TEST_STATE_2
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'Ваша заявка передана координатору')


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Здравствуйте! Вас приветствует чат-бот компании Фобизнес 🖖. "
                        "Для перехода в меню наберите /menu или нажмите кнопку на дополнительной клавиатуре.", reply_markup=kb.greet_kb)

# @dp.message_handler()
# async def echo_message(msg: types.Message):
#     await bot.send_message(msg.from_user.id, msg.text)

@dp.message_handler()
async def echo_message(message: types.Message):
    state = USER_STATES[message.from_user.id]
    if state == BOT_STATES.TEST_STATE_1:
        try:
            arg = message.text
            r = requests.get(url + arg, auth=(u.encode('utf-8').decode('latin1'), p))
            r.encoding = 'utf-8-sig'
            print("req:", r.text)
            raw = r.text.split(', ')
            d = {}
            for r in raw:
                kv = r.split(' : ')
                d[kv[0]] = kv[1]
            USER_STATES[message.from_user.id] = BOT_STATES.TEST_STATE_0
            return await message.answer(f"Исполнитель по запросу #{arg}: {d['employee']}. "
                                        f"Статус запроса: {d['status']}. "
                                        f"Планируемая дата завершения: {d['datePlan']}")
        except:
            USER_STATES[message.from_user.id] = BOT_STATES.TEST_STATE_0
            return await message.answer(f"Ваш запрос '{message.text}' не может быть обработан. Перейдите в меню (/menu) "
                                        f"и нажмите кнопку 'Узнать статус обращения', чтобы выполнить повторный запрос.")
    else:
        USER_STATES[message.from_user.id] = BOT_STATES.TEST_STATE_0
        return await message.answer(f'Нажмите /menu и нажмите кнопку "Узнать статус обращения", '
                                    f'чтобы сделать запрос')

#
# @dp.message_handler(content_types=ContentTypes.PHOTO)
# async def echo_foto(message: types.Message):
#     return await message.answer_photo(
#         message.photo[-1].file_id,
#         caption=f"Вы написали: {message.caption!r}",
#
#     )
#
# @dp.message_handler(content_types=ContentTypes.STICKER | ContentTypes.ANIMATION)
# async def forward_any_sticker(message: types.Message):
#     file_id = message.sticker.file_id
#     await bot.download_file_by_id(
#         file_id = file_id,
#         destination= STICKERS_DIR / f"sticker_{file_id}.{'TGS' if message.sticker.is_animated else 'webp'}",
#     )
#     return await message.forward(message.chat.id)


if __name__ == '__main__':
    # print("Bot token:", TOKEN)
    executor.start_polling(dp)