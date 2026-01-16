from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncSession, create_async_engine

from database.models.base import Base
from config import settings

engine = create_async_engine(url="sqlite+aiosqlite:///./bot.db", echo=True)
session_maker = async_sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)

async def create_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

async def drop_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)