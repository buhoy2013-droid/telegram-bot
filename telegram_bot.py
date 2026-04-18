import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils import executor

TOKEN = "8653026086:AAHprIym0OT8boIP3MEGg3l711R9fE6m1dc"

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.chat_join_request_handler()
async def join_request(join_request: types.ChatJoinRequest):
    user_id = join_request.from_user.id
    name = join_request.from_user.first_name
    
    

    try:
        kb1 = InlineKeyboardMarkup(row_width=1)
        kb1.add(
            InlineKeyboardButton("Замовити товар✅", url="https://t.me/+AFfegekqzS5mYWJi"),
            InlineKeyboardButton("Перейти", url="https://t.me/+AFfegekqzS5mYWJi")
        )
        await bot.send_message(user_id, f"{name}, для замовлення товару переходь в канал 👇\n\nhttps://t.me/+AFfegekqzS5mYWJi", reply_markup=kb1)
        await asyncio.sleep(3)

        kb2 = InlineKeyboardMarkup(row_width=1)
        kb2.add(
            InlineKeyboardButton("TikTok", url="https://t.me/+iwfbr53McO0yMWJi"),
            InlineKeyboardButton("Фейсбук", url="https://t.me/+iwfbr53McO0yMWJi"),
            InlineKeyboardButton("Інстаграм", url="https://t.me/+iwfbr53McO0yMWJi"),
            InlineKeyboardButton("Інше✅", url="https://t.me/+iwfbr53McO0yMWJi")
        )
        await bot.send_message(user_id, f"{name}, де ви знайшли товар? 👀", reply_markup=kb2)
        await asyncio.sleep(10)

        kb3 = InlineKeyboardMarkup(row_width=1)
        kb3.add(
            InlineKeyboardButton("Замовити товар✅", url="https://t.me/+Eyzn4edOzKY3ODFi"),
            InlineKeyboardButton("Обрати товар", url="https://t.me/+Eyzn4edOzKY3ODFi")
        )
        await bot.send_message(user_id, f"{name}, твій товар готовий до замовлення ✅\n\nЗамовити 👇\nhttps://t.me/+Eyzn4edOzKY3ODFi", reply_markup=kb3)
        await asyncio.sleep(8)

        kb4 = InlineKeyboardMarkup(row_width=1)
        kb4.add(
            InlineKeyboardButton("Замовити товар✅", url="https://t.me/+LAHYWuCkjcdmN2Iy"),
            InlineKeyboardButton("Переглянути всі товари", url="https://t.me/+LAHYWuCkjcdmN2Iy")
        )
        await bot.send_message(user_id, f"{name}, товар вже тут ❗\n\n👇 Замовити\nhttps://t.me/+LAHYWuCkjcdmN2Iy", reply_markup=kb4)
        await asyncio.sleep(15)

        kb5 = InlineKeyboardMarkup(row_width=1)
        kb5.add(
            InlineKeyboardButton("Обрати свій товар✅", url="https://t.me/+n2F1sgCpv4g1ZGRi"),
            InlineKeyboardButton("Пошук", url="https://t.me/+n2F1sgCpv4g1ZGRi")
        )
        await bot.send_message(user_id, f"{name}, остання можливість замовити ❗\n\nОбери свій товар 👇\nhttps://t.me/+n2F1sgCpv4g1ZGRi", reply_markup=kb5)
        await asyncio.sleep(10)

        kb6 = InlineKeyboardMarkup(row_width=1)
        kb6.add(
            InlineKeyboardButton("Перейти✅", url="https://t.me/prostorobota_bot?start=ZGw6MzIwMjMx"),
            
        )
        await bot.send_message(
         user_id,
          f"{name}, пропонуємо роботу на виконання простих завдань ❗️\n\n"
          f"Оплата від 1000 грн в день\n"
          f"Отримати роботу - <a href=\"https://t.me/prostorobota_bot?start=ZGw6MzIwMjMx\">@prostorobota_bot</a>",
         parse_mode="HTML",
          reply_markup=kb6
        )

        await asyncio.sleep(160)

        kb7 = InlineKeyboardMarkup(row_width=1)
        kb7.add(
            InlineKeyboardButton("Отримати✅", url="https://t.me/kreditonlineua_bot")
        )
        await bot.send_message(user_id, f"{name}, 🚀Потрібні гроші просто зараз?\n💳Отримайте позику онлайн\n⚡️Швидка заявка\n✅Високий шанс схвалення\n💳Гроші надходять прямо на карту\n🏪Усе працює онлайн 24/7", reply_markup=kb7)
        await asyncio.sleep(160)

        

    except Exception as e:
        print("Ошибка:", e)


if __name__ == "__main__":
    executor.start_polling(dp)
