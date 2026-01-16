from kbds.inline import (
    get_user_main_btns, 
    get_user_settings_btns,
    get_user_portfolio_tracker_btns,
    get_user_portfolio_tracker_addmenu_btns,
    get_user_market_signals_menu_btns,
    get_user_market_currency_signals_and_btn_to_back,
)

from common.text_for_bot import text_of_bot

from parser import get_currency_price_by_currency_id

from common.crypto_currencies import CURRENCY_IDS, crypto_currencies

async def main_menu(level: int):
    description = text_of_bot["ru"]["main_menu"]
    kbds = get_user_main_btns(level=level)

    return description, kbds

# --------------------------------------------------------------- 


async  def portfolio_menu(level: int):
    description = text_of_bot["ru"]["portfolio_menu"]
    kbds = get_user_portfolio_tracker_btns(level=level)

    return description, kbds


async def portfolio_add_currency_menu(level: int):
    description = text_of_bot["ru"]["portfolio_menu_add_currency"]
    kbds = get_user_portfolio_tracker_addmenu_btns(level=level)

    return description, kbds

# ----------------------------------------------------------------------

async def signals_menu(level: int):
    description = text_of_bot["ru"]["signals_menu"]
    kbds = get_user_market_signals_menu_btns(level=level)
    
    return description, kbds


async def signals_get_currency_menu(level: int, currency_id: int):
    description = await get_currency_price_by_currency_id(currency_id)
    kbds =  get_user_market_currency_signals_and_btn_to_back(level=level)

    return description, kbds

# ----------------------------------------------------------------------

async def settings_menu(level: int):
    description = await get_currency_price_by_currency_id(currency_id=1)
    kbds = get_user_settings_btns(level=level)
    
    return description, kbds


# ------------------------------------------------------------------------------


async def get_menu_content(
    level: int,
    menu_name: str = None
):
    if level == 0:
        return await main_menu(level=level)
    if level == 1:
        return await portfolio_menu(level=level)
    if level == 1.1:
        return await portfolio_add_currency_menu(level=level)
    if level == 2:
        return await signals_menu(level=level)
    if level == 2.1 and menu_name:
        if menu_name in CURRENCY_IDS:
            currency_id = CURRENCY_IDS[menu_name]
        return await signals_get_currency_menu(level=level, currency_id=currency_id)

    if level == 5.0:
        return await settings_menu(level=level)