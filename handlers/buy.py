from aiogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup, Message, InputMedia
from states import UserStates
from aiogram.dispatcher import FSMContext

async def Buygoods1(c:CallbackQuery):
    keyboard = InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardButton("💲Купить💲", callback_data="Купить 1"))
    await c.message.delete()
    await c.message.answer_photo(caption="Детали:\nАртикул: 280251\nМодель: Antony\nСтрана производства: Словения\nЦвет: Белый\nСостав: 100% хлопок\nРазмер: S-XL\nЦена: 9.999Р", reply_markup=keyboard, photo=r"https://yandex.ru/images/search?from=tabbar&img_url=https%3A%2F%2Fae04.alicdn.com%2Fkf%2FS53e3bc89279f432183448ef1781abb71i.jpeg&lr=10756&pos=0&rpt=simage&text=%D1%80%D1%83%D0%B1%D0%B0%D1%88%D0%BA%D0%B0%20%D0%BC%D1%83%D0%B6%D1%81%D0%BA%D0%B0%D1%8F%20%D0%B1%D0%B5%D0%BB%D0%B0%D1%8F")

async def AskAddress(c:CallbackQuery):
    await UserStates.wait_address.set()
    await c.message.delete()
    await c.message.answer("Введите ваш адрес:\nГород:\nулица:\nдом:\nквартира:")

async def Buygoods2(c:CallbackQuery):
    keyboard = InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardButton("💲Купить💲", callback_data="Купить 2"))
    await c.message.delete()
    await c.message.answer_photo(caption="Детали:\nАртикул: 220443\nМодель: Loader\nСтрана производства: Россия\nЦвет: Синий\nСостав: 98% хлопок, Эластан 2%\nРазмер: S-XL\nЦена: 8.999Р", reply_markup=keyboard, photo=r"https://yandex.ru/images/search?from=tabbar&img_url=https%3A%2F%2Fpapik.pro%2Fuploads%2Fposts%2F2021-12%2F1639298601_34-papik-pro-p-dzhinsi-klipart-35.png&lr=10756&pos=4&rpt=simage&text=%D0%B4%D0%B6%D0%B8%D0%BD%D1%81%D1%8B%20%D0%BC%D1%83%D0%B6%D1%81%D0%BA%D0%B8%D0%B5%20%D0%BD%D0%B0%20%D0%B1%D0%B5%D0%BB%D0%BE%D0%BC%20%D1%84%D0%BE%D0%BD%D0%B5")

async def SendToAdmin(m:Message, state:FSMContext):
    await state.finish()
    await m.bot.send_message(968876784, f"Новая покупка:\n{m.text}\n@{m.from_user.username}")
    await m.answer("Ожидайте ответа продавца, он вскоре свяжется с вами")


def SetupBuy(dp):
    dp.register_callback_query_handler(Buygoods1, lambda c: c.data=="Товар 1")
    dp.register_callback_query_handler(Buygoods2, lambda c: c.data == "Товар 2")
    dp.register_callback_query_handler(AskAddress, lambda c: c.data=="Купить 1")
    dp.register_callback_query_handler(AskAddress, lambda c: c.data == "Купить 2")
    dp.register_message_handler(SendToAdmin, state=UserStates.wait_address)