from fastapi import APIRouter, HTTPException, Depends
from app.models import Task, TaskCreate
from app.services import TaskService

router = APIRouter()
service = TaskService()

@router.get("/")
def home():
    return {"message": "Task API"}

@router.get("/tasks")
def list_tasks():
    return service.get_all()

@router.get("/tasks/{task_id}")
def get_task(task_id: int):
    task = service.get(task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@router.post("/tasks", status_code=201)
def create_task(task: TaskCreate):
    return service.create(task)

@router.put("/tasks/{task_id}")
def update_task(task_id: int, task: TaskCreate):
    updated = service.update(task_id, task)
    if not updated:
        raise HTTPException(status_code=404, detail="Task not found")
    return updated

@router.delete("/tasks/{task_id}", status_code=204)
def delete_task(task_id: int):
    deleted = service.delete(task_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Task not found")
