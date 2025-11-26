from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update

from .models.user import User

async def create_user(
    session: AsyncSession,
    user_id: int,
    access_status: bool,
    first_name: str | None = None,
    last_name: str | None = None,
    phone: str | None = None,
):
    user = User(
        user_id=user_id,
        first_name=first_name,
        last_name=last_name,
        phone=phone,
        access_status=access_status,
    )
    session.add(user)
    await session.commit()
    return user

async def get_user_by_user_id(
    session: AsyncSession,
    user_id: int,
) -> User:
    stmt = await session.execute(
        select(User).where(User.user_id == user_id)
    )
    user = stmt.scalar_one_or_none()
    return user

async def change_access_status_user(
    session: AsyncSession,
    user_id: int,
):
    stmt = (
        update(User)
        .where(User.user_id == user_id)
        .values(access_status = True)
    )
    await session.execute(stmt)
    await session.commit()

async def get_user_access_status(
    session: AsyncSession,
    user_id: int
):
    stmt = await session.execute(
        select(User.access_status).where(User.user_id == user_id)
    )
    user_access_status = stmt.scalar()
    return user_access_status
