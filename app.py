import os
import sys
import asyncio

from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from aiogram.enums.parse_mode import ParseMode
from aiogram.client.default import DefaultBotProperties
from aiogram.types import LabeledPrice, PreCheckoutQuery, Message

from sqlalchemy.ext.asyncio import AsyncSession

from dotenv import load_dotenv, find_dotenv

from handlers.user_private import user_private_router
from config import settings
from database.engine import create_db, drop_db, session_maker
from middleware.db import DataBaseSession
from kbds.inline import get_purchase_keyboard

load_dotenv(find_dotenv())

bot = Bot(token=settings.BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()

@dp.message(Command('subscribe'))
async def command_start_handler(message: Message) -> None:
    await message.answer(
        text="Хотите оплатить подписку❓",
        reply_markup=get_purchase_keyboard()
    )

@dp.callback_query(F.data.startswith("buy"))
async def process_callback_query(callback_query: types.CallbackQuery) -> None:
    data = callback_query.data.split('_')

    action = data[1]
    print(action)
    
    prices = []
    description = ''
    
    if action == "1":
        description = 'Подписка на бота (1 месяц) 📑'
        prices = [LabeledPrice(label="Оплата заказа №1", amount=100 * 100)]
    
    elif action == "2":
        description = "Подписка на бота (3 месяца) 📑"
        prices = [LabeledPrice(label="Оплата заказа №2", amount=300 * 100)]

    elif action == "3":
        description = "Подписка на бота (1 год) 📑"
        prices = [LabeledPrice(label="Оплата заказа №3", amount=1200 * 100)]
    
    if prices:
        await bot.send_invoice(
            chat_id=callback_query.from_user.id,
            title=f'Подписка на бота 🤖',
            description=description,
            payload=f'sub{action}',
            provider_token=settings.PROVIDER_TOKEN,
            currency=settings.CURRENCY,
            start_parameter='test',
            prices=prices,
        )

@dp.pre_checkout_query()
async def process_pre_checkout_query(pre_checkout_query: PreCheckoutQuery) -> None:
    await bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)
    
@dp.message(F.successful_payment)
async def process_successful_payment(message: Message, session: AsyncSession) -> None:
    payload_to_message = {
        'sub1': '💵 Подписка на бота 📑',
    }
    response_message = payload_to_message.get(message.successful_payment.invoice_payload, 'Оплата прошла успешно!')
    await message.answer(response_message)
    

    

dp.include_router(user_private_router)

async def on_startup(bot):
    await create_db()
    # await drop_db()

async def on_shutdown(bot):
    print("Bot -- off")

async def main() -> None:
    dp.startup.register(on_startup)
    dp.shutdown.register(on_shutdown)

    dp.update.outer_middleware(DataBaseSession(session_pool=session_maker))

    await bot.delete_webhook(drop_pending_updates=True)
    # await bot.set_my_commands()
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())