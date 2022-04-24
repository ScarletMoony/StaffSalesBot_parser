from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import json

import urls
import config
from selparser import get_data

bot = Bot(token=config.TOKEN)
dp = Dispatcher(bot)

async def send_parsed(msg, url):
    get_data(url=url)
    with open('./.parsed.json', 'rb') as file:
        parsed = json.load(file)
    for i in range(0, len(parsed)):
        await bot.send_message(msg.from_user.id, f'{parsed[i].get("name")}\n{parsed[i].get("sizes")}\n{parsed[i].get("price")}  {parsed[i].get("old_price")}  {parsed[i].get("discount")}\n{parsed[i].get("href")}')
        await bot.send_photo(msg.from_user.id, photo=f'{parsed[i].get("img_link")}')


@dp.message_handler(commands=['start'])
async def start_message(msg: types.Message):
    await bot.send_message(msg.from_user.id, 'Hi')
    await msg.reply('Here all commands:\n/sweatshirts_hoodies\n/sneakers\n/tshirts\n/jackets\n/bottoms\n')

@dp.message_handler(commands=['sweatshirts_hoodies'])
async def get_jachets(msg: types.Message):
    await send_parsed(msg=msg, url=urls.sweatshirts_hoodies)

@dp.message_handler(commands=['bottoms'])
async def get_jachets(msg: types.Message):
    await send_parsed(msg=msg, url=urls.bottoms)
    
@dp.message_handler(commands=['jackets'])
async def get_jachets(msg: types.Message):
    await send_parsed(msg=msg, url=urls.jackets)
    
@dp.message_handler(commands=['tshirts'])
async def get_jachets(msg: types.Message):
    await send_parsed(msg=msg, url=urls.tshirts)
    
@dp.message_handler(commands=['sneakers'])
async def get_jachets(msg: types.Message):
    await send_parsed(msg=msg, url=urls.sneakers)
        

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=print('Bot is up'))