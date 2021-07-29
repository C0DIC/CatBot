import logging
import requests
from aiogram import Bot, Dispatcher, executor, types

api_token = '1910080285:AAHNEAiSL7dAofE_88b0PMPqlZqbfHTWeB8'

# Logging
logging.basicConfig(level=logging.INFO)

bot = Bot(api_token)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start_command(msg: types.Message):
    await msg.reply("Привет :3\nЯ просто кидаю фоточки, которые ты попросишь")


@dp.message_handler(commands=['cats'])
async def cat_command(msg: types.Message):
    response = requests.get('https://api.thecatapi.com/v1/images/search')
    data = response.json()[0].get('url')

    if data[-3::] != "gif":
        await bot.send_photo(msg.chat.id, data)
    else:
        await bot.send_animation(msg.chat.id, data)


if __name__ == '__main__':
    executor.start_polling(dp, timeout=0, relax=0, skip_updates=False)
