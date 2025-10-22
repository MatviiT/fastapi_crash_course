from fastapi import APIRouter, Depends
from schemas import STaskAdd, STask, STaskId
from typing import Annotated
from reposetory import TaskReposetory


router = APIRouter(
    prefix="/tasks",
    tags=["Таски"]
)


@router.post("")
async def add_task(
        task: Annotated[STaskAdd, Depends()]
) -> STaskId:
    task_id = await TaskReposetory.add_one(task)
    return {"ok": True, "task_id": task_id}


@router.get("")
async def get_task() -> list[STask]:
    tasks = await TaskReposetory.find_all()
    return {"data": tasks}
