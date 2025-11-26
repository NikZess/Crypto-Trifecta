from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

def get_purchase_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="1 месяц 💸", callback_data="buy_1")],
        [InlineKeyboardButton(text="3 месяца 🤑", callback_data="buy_2")],
        [InlineKeyboardButton(text="1 год 💰", callback_data="buy_3")],
    ])