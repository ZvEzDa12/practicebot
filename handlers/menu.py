from aiogram.types import Message, KeyboardButton, ReplyKeyboardMarkup
from texts import btn1,btn2,btn3,btn4,btn5,goods

async def menumessage(m:Message):
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row(KeyboardButton(btn1), KeyboardButton(btn2))
    keyboard.row(KeyboardButton(btn3), KeyboardButton(btn4))
    keyboard.row(KeyboardButton(btn5), KeyboardButton(goods))
    await m.answer("Выберите вопрос:", reply_markup=keyboard)

def SetupMenu(dp):
    dp.register_message_handler(menumessage, commands="start")