from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.utils.markdown import text, hide_link, hstrikethrough, hbold
import json

import urls
import config
from selparser import get_data, update_data

bot = Bot(token=config.TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)

async def update_datas():
    update_data()

async def send_parsed(msg, category):
    
    with open(f'./.parsed/{category}.json', 'rb') as file:
        parsed = json.load(file)
    for i in range(0, len(parsed)):
        await bot.send_message(msg.from_user.id, 
                               text(
                                    hbold(f'{parsed[i].get("name")}'),
                                    f'{parsed[i].get("sizes")}',
                                    f'{parsed[i].get("price")}',
                                    hstrikethrough(f'{parsed[i].get("old_price")}'),
                                    hbold(f'{parsed[i].get("discount")}'),
                                    hide_link(f'{parsed[i].get("href")}'),
                                    sep='\n'
                               )
        )
        await bot.send_photo(msg.from_user.id, photo=f'{parsed[i].get("img_link")}')


@dp.message_handler(commands=['start'])
async def start_message(msg: types.Message):
    await bot.send_message(msg.from_user.id, 'Hi')
    await msg.reply('Here all commands:\n/sweatshirts_hoodies\n/sneakers\n/tshirts\n/jackets\n/bottoms\n')
    await msg.reply('If you want to update data just send /update')

@dp.message_handler(commands=['update'])
async def update_parsed(msg: types.Message):
    await update_datas()
    
@dp.message_handler(commands=['sweatshirts_hoodies'])
async def get_sweatshirts_hoodies(msg: types.Message):
    await send_parsed(msg=msg, category='sweatshirts_hoodies')

@dp.message_handler(commands=['bottoms'])
async def get_bottoms(msg: types.Message):
    await send_parsed(msg=msg, category='bottoms')
    
@dp.message_handler(commands=['jackets'])
async def get_jackets(msg: types.Message):
    await send_parsed(msg=msg, category='jackets')
    
@dp.message_handler(commands=['tshirts'])
async def get_tshirts(msg: types.Message):
    await send_parsed(msg=msg, category='tshirts')
    
@dp.message_handler(commands=['sneakers'])
async def get_sneakers(msg: types.Message):
    await send_parsed(msg=msg, category='sneakers')
        

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=print('Bot is up'))