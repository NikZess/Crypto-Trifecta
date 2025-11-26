from aiogram import Router, types
from aiogram.filters import CommandStart, Command

from sqlalchemy.ext.asyncio import AsyncSession

from database.orm_query import create_user, get_user_by_user_id

user_private_router = Router()

@user_private_router.message(CommandStart())
async def start_cmd_handler(message: types.Message, session: AsyncSession):
    await message.answer("Привет!")
    user = await get_user_by_user_id(
        session=session,
        user_id=message.from_user.id,
    )
    if user is None:
        await message.answer("Нажми команду: /reg")
    else:
        await message.answer("Ты в боте")
    
@user_private_router.message(Command("reg"))
async def reg_cmd_handler(message: types.Message, session: AsyncSession):
    check_user = await get_user_by_user_id(session=session, user_id=message.from_user.id)
    if check_user is None:
        await create_user(
            session=session,
            user_id=message.from_user.id,
            first_name=message.from_user.first_name,
            last_name=message.from_user.last_name,
            phone=None,
        )
        await message.answer("Успешная регистрация")
    else:
        await message.answer("Вы уже в бд")