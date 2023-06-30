from aiogram import Bot, Dispatcher
from aiogram.utils.executor import start_polling
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from handlers import SetupHandlers

def main():
    bot = Bot("5761796030:AAH1vEewZ80_EG4FQVFlCm3rBZx9m9TXtT0")
    dp = Dispatcher(bot, storage=MemoryStorage())
    start_polling(dp, on_startup=OnStartUp)

async def OnStartUp(dp):
    SetupHandlers(dp)

main()