from aiogram .types import Message, InlineKeyboardButton, InlineKeyboardMarkup
from texts import *

async def Answer1(m:Message):
    await m.answer("Да, на данный момент посмотреть отзывы можно во Вконтакте. В разделе обсуждений.")

async def Answer2(m:Message):
    await m.answer("Для того, чтобы определить точный размер по нашей размерной сетке, измерьте обхват груди, талии и бедер с помощью мерной ленты. При выборе между двумя размерами — сделайте предпочтение в сторону большего. Так же можете использовать данные уже имеющихся удобных для вас вещей и сравнить их со значениями в таблице.")

async def Answer3(m:Message):
    await m.answer("Онлайн оплата картами Visa, MasterCard, МИР.")

async def Answer4(m:Message):
    await m.answer("По всей России через CDEK")

async def Answer5(m:Message):
    await m.answer("Вы вправе отказаться от товара надлежащего качества в течение 7 календарных дней после получения, в случае если произошла ошибка не с вашей стороны. При возврате товаров надлежащего качества стоимость доставки и комиссия за перевод платежа не возмещаются.")

async def Answer6(m:Message):
    keyboard = InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardButton("Белая мужская рубашка", callback_data="Товар 1"))
    keyboard.add(InlineKeyboardButton("Джинсы мужские", callback_data="Товар 2"))
    await m.answer("Выберите товар:", reply_markup=keyboard)

def SetupAnswers(dp):
    dp.register_message_handler(Answer1, text=btn1)
    dp.register_message_handler(Answer2, text=btn2)
    dp.register_message_handler(Answer3, text=btn3)
    dp.register_message_handler(Answer4, text=btn4)
    dp.register_message_handler(Answer5, text=btn5)
    dp.register_message_handler(Answer6, text=goods)