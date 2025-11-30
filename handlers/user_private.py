from aiogram import Router, types
from aiogram.filters import CommandStart, Command

from sqlalchemy.ext.asyncio import AsyncSession

from database.orm_query import create_user, get_user_by_user_id, get_user_access_status

from common.text_for_bot import text_of_bot

user_private_router = Router()

@user_private_router.message(CommandStart())
async def start_cmd_handler(message: types.Message, session: AsyncSession):
    check_user = await get_user_by_user_id(session=session, user_id=message.from_user.id)
    if check_user is None:
        await create_user(
            session=session,
            user_id=message.from_user.id,
            first_name=message.from_user.first_name,
            last_name=message.from_user.last_name,
            phone=None,
            access_status=False,
        )    
    user_access_status = await get_user_access_status(session=session, user_id=message.from_user.id)
    if user_access_status == False:
        await message.answer("Купи подписку или введи промокод: /subscribe - Подписка, промокод просто введите и отправьте")    
    else:
        await message.answer(text_of_bot["ru"]["main_menu"])