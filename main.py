import os
import asyncio
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from dotenv import load_dotenv
from python_aternos import Client

# Загружаем переменные из .env
load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")
ATERNOS_USER = os.getenv("ATERNOS_USER")
ATERNOS_PASS = os.getenv("ATERNOS_PASS")
ADMIN_ID = int(os.getenv("ADMIN_ID"))

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# Инициализация Aternos
aternos = Client.from_credentials(ATERNOS_USER, ATERNOS_PASS)
server = aternos.list_servers()[0]

@dp.message(Command("start"))
async def start(message: types.Message):
    if message.from_user.id == ADMIN_ID:
        await message.answer("TwistBot активен! Команды: /status, /start_server, /stop_server")

@dp.message(Command("status"))
async def status(message: types.Message):
    server.fetch()
    await message.answer(f"Статус сервера: {server.status}")

@dp.message(Command("start_server"))
async def start_server(message: types.Message):
    server.start()
    await message.answer("Запуск запущен!")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())