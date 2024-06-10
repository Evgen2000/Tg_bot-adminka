import asyncio
import os

from aiogram import Bot, Dispatcher, types
from aiogram.enums import ParseMode
from aiogram.client.bot import DefaultBotProperties
#from aiogram.fsm.strategy import FSMStrategy

from dotenv import find_dotenv, load_dotenv
from user_private import user_private_router
from user_group import user_group_router
from admin_private import admin_router
from bot_cmds_list import private


load_dotenv(find_dotenv())


ALLOWED_UPDATES = ['message, edited_message']
# Получаем токен из переменных окружения
token = os.getenv('TOKEN')

# Инициализируем бота с использованием параметра default
bot = Bot(token=token, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
bot.my_admins_list = []


# Создаем диспетчер
dp = Dispatcher()
dp.include_router(user_private_router)
dp.include_router(user_group_router)
dp.include_router(admin_router)


async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    # await bot.delete_my_commands(scope=types.BotCommandScopeAllPrivateChats())
    await bot.set_my_commands(commands=private, scope=types.BotCommandScopeAllPrivateChats())
    await dp.start_polling(bot, allowed_updates=ALLOWED_UPDATES)


asyncio.run(main())
