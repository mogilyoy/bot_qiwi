import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types.message import ContentTypes

import config as cfg
import markups as nav 
from db import Database

logging.basicConfig(level=logging.INFO)

bot = Bot(token=cfg.TOKEN)
dp = Dispatcher(bot)

db = Database('database.db')

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    if message.chat.type == 'private':
        if not db.user_exists(message.from_user.id):
            db.add_user(message.from_user.id)
        await bot.send_message(message.from_user.id, f'Привет!\nВы уже отправили: {db.user_money(message.from_user.id)} рублей')



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates = True)
