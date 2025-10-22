from fastapi import FastAPI

from database import delete_tables, create_tables

from contextlib import asynccontextmanager
from router import router as tasks_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    await delete_tables()
    await create_tables()
    print("база очищена")
    print("база готова до роботи")
    yield
    print("вимкнення")

app = FastAPI(lifespan=lifespan)


app.include_router(tasks_router)
