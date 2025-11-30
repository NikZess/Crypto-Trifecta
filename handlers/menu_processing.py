from kbds.inline import get_user_main_btns, get_user_settings_btns

from common.text_for_bot import text_of_bot

async def main_menu(level: int):
    description = text_of_bot["ru"]["main_menu"]
    kbds = get_user_main_btns(level=level)

    return description, kbds

async def settings_menu(level: int):
    description = text_of_bot["ru"]["settings_menu"]
    kbds = get_user_settings_btns(level=level)
    
    return description, kbds

async def get_menu_content(
    level: int,
):
    if level == 0:
        return await main_menu(level=level)
    if level == 5.0:
        return await settings_menu(level=level)