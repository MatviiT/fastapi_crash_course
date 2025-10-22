from typing import Optional
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


# Підключення до бази даних SQLite (асинхронне)
engine = create_async_engine("sqlite+aiosqlite:///tasks.db")
new_session = async_sessionmaker(engine, expire_on_commit=False)


class Model(DeclarativeBase):
    # """Базова модель для ORM"""
    pass


class TaskOrm(Model):
    # """ORM-модель таблиці tasks"""
    __tablename__ = "tasks"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    description: Mapped[Optional[str | None]]


async def create_tables():
    # """Створення таблиць у базі"""
    async with engine.begin() as conn:
        await conn.run_sync(Model.metadata.create_all)


async def delete_tables():
    # """Видалення таблиць із бази"""
    async with engine.begin() as conn:
        await conn.run_sync(Model.metadata.drop_all)
