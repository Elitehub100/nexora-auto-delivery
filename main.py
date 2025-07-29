from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.utils import executor
import logging

logging.basicConfig(level=logging.INFO)

# Your updated bot token here:
BOT_TOKEN = "8440109945:AAHsyuMmbKwD7lFOez9Fe86Zwjxzr0azCvo"

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start_handler(message: Message):
    # Reply once with success message
    await message.reply("✅ Hello! Nexora Auto Bot is working successfully.")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
