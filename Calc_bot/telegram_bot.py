from aiogram import Bot, types, Dispatcher, executor
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
import controler as cont
import logger as log


bot = Bot(token="TOKEN")
dp = Dispatcher(bot)


async def on_startup(_):
    print('Бот онлайн')
    


@dp.message_handler(commands=['start', 'help'])
async def command_start(message: types.Message):
    await message.answer('Привет! я бот-калькулятор! Введите Ваши числа в формате 1+2*3-4/5')
  

@dp.message_handler()
async def echo_send(message: types.Message):
    parse = message.text
    my_list = cont.parsing(parse)
    res = cont.calculation(my_list)
    log.log(parse,res)
  
    await message.answer(*res)  

    


executor.start_polling(dp, skip_updates=True, on_startup=on_startup)