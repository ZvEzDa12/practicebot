from aiogram .types import Message
from texts import *

async def Answer1(m:Message):
    await m.answer("Ты хороший")

async def Answer2(m:Message):
    await m.answer("Ты хороший1")

async def Answer3(m:Message):
    await m.answer("Ты хороший2")

async def Answer4(m:Message):
    await m.answer("Ты хороший3")

async def Answer5(m:Message):
    await m.answer("Ты хороший4")

async def Answer6(m:Message):
    await m.answer("Ты хороший5")

def SetupAnswers(dp):
    dp.register_message_handler(Answer1, text=btn1)
    dp.register_message_handler(Answer2, text=btn2)
    dp.register_message_handler(Answer3, text=btn3)
    dp.register_message_handler(Answer4, text=btn4)
    dp.register_message_handler(Answer5, text=btn5)
    dp.register_message_handler(Answer6, text=btn6)