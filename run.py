#подключение aiogrammmm
import aiogram                                          
from aiogram import Bot, Dispatcher, types, F
from aiogram.types import Message                                            

#подключение asyncio
import asyncio                                          

#подключение объектов и переменных из других файлов
from config import TOKEN
from app.handlers import router

#основня функция запускающяя бота
async def main():
    bot = Bot(TOKEN)
    dp = Dispatcher() 
    dp.include_router(router)
    await dp.start_polling(bot)


#бесконечный цикл шоб бот работал
if __name__ == '__main__':
    asyncio.run(main())
