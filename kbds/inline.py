from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.filters.callback_data import CallbackData


class MenuCallBack(CallbackData, prefix="menu"):
    level: float
    menu_name: str


def get_purchase_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="1 месяц 💸", callback_data="buy_1")],
        [InlineKeyboardButton(text="3 месяца 🤑", callback_data="buy_2")],
        [InlineKeyboardButton(text="1 год 💰", callback_data="buy_3")],
    ])

def get_user_main_btns(*, level: int, sizes: tuple[int] = (3, 1, 1)) -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardBuilder()

    btns = {
        "📊 Трекер портфеля": "portfolio_tracker",
        "🔔 Сигналы рынка": "market_signals",
        "💵 Курс криптовалют": "cryptocurrency_rate",
        "📖 Помощь": "help_menu",
        "⚙️ Настройки": "settings_menu",
    }

    for text, menu_name in btns.items():
        if menu_name == "portfolio_tracker":
            keyboard.add(InlineKeyboardButton(
                text=text,
                callback_data=MenuCallBack(level=1.0, menu_name=menu_name).pack()
            ))
        
        if menu_name == "market_signals":
            keyboard.add(InlineKeyboardButton(
                text=text,
                callback_data=MenuCallBack(level=2.0, menu_name=menu_name).pack()
            ))
        
        if menu_name == "cryptocurrency_rate":
            keyboard.add(InlineKeyboardButton(
                text=text,
                callback_data=MenuCallBack(level=3.0, menu_name=menu_name).pack()
            ))

        if menu_name == "help_menu":
            keyboard.add(InlineKeyboardButton(
                text=text,
                callback_data=MenuCallBack(level=4.0, menu_name=menu_name).pack()
            ))

        if menu_name == "settings_menu":
            keyboard.add(InlineKeyboardButton(
                text=text,
                callback_data=MenuCallBack(level=5.0, menu_name=menu_name).pack()
            ))

    return keyboard.adjust(*sizes).as_markup()

# PORTFOLIO

def get_user_portfolio_tracker_btns(*, level: int, sizes: tuple[int] = (1, )) -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardBuilder()

    btns = {
        "👜 Добавить валюne в портфель": "add_coin_in_portfolio",
        "🔙 Назад": "back_main_menu",
    }

    for text, menu_name in btns.items():
        if menu_name == "add_coin_in_portfolio":
            keyboard.add(InlineKeyboardButton(
                text=text,
                callback_data=MenuCallBack(level=1.1, menu_name=menu_name).pack()
            ))
        if menu_name == "back_main_menu":
            keyboard.add(InlineKeyboardButton(
                text=text,
                callback_data=MenuCallBack(level=0, menu_name=menu_name).pack()
            ))
    
    return keyboard.adjust(*sizes).as_markup()

def get_user_portfolio_tracker_addmenu_btns(*, level: int, sizes: tuple[int] = (1, 1)) -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardBuilder()

    btns = {
        "🪙 Список доступных валют": "list_of_currency",
        "🔙 Назад": "back_main_menu",
    }

    for text, menu_name in btns.items():
        if menu_name == "list_of_currency":
            keyboard.add(InlineKeyboardButton(
                text=text,
                callback_data=MenuCallBack(level=1.2, menu_name=menu_name).pack()
            ))
        if menu_name == "back_main_menu":
            keyboard.add(InlineKeyboardButton(
                text=text,
                callback_data=MenuCallBack(level=1, menu_name=menu_name).pack()
            ))
    
    return keyboard.adjust(*sizes).as_markup()

# SETTINGS

def get_user_settings_btns(*, level: int, sizes: tuple[int] = (1,)) -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardBuilder()

    btns = {
        "🌍 Язык": "language",
        "🔙 Назад": "back_main_menu",
    }

    for text, menu_name in btns.items():
        if menu_name == "language":
            keyboard.add(InlineKeyboardButton(
                text=text,
                callback_data=MenuCallBack(level=5.1, menu_name=menu_name).pack()
            ))

        if menu_name == "back_main_menu":
            keyboard.add(InlineKeyboardButton(
                text=text,
                callback_data=MenuCallBack(level=0, menu_name=menu_name).pack()
            ))
    
    return keyboard.adjust(*sizes).as_markup()