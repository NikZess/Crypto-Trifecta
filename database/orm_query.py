from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from .models.user import User

async def create_user(
    session: AsyncSession,
    user_id: int,
    first_name: str | None = None,
    last_name: str | None = None,
    phone: str | None = None,
):
    user = User(
        user_id=user_id,
        first_name=first_name,
        last_name=last_name,
        phone=phone
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
