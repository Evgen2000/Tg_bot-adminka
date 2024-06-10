# база для запуска движка ОRM-(Object-Relational Mapping -объектно-реляционное отображение, или преобразование) — технология програм-ния,
# которая связывает базы данных с концепциями ооп яп, создавая «виртуальную объектную базу данных».
import os
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from models import Base

engine = create_async_engine(os.getenv('DB_URL'), echo=True)

session_maker = async_sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)


async def create_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


async def drop_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
