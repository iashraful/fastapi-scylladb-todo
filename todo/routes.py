from fastapi import APIRouter

from todo.views import TaskView


todo_router = APIRouter(
    prefix="/tasks",
    responses={404: {"description": "Not found"}},
)

todo_router.add_api_route("/", TaskView.list, methods=["GET"])
todo_router.add_api_route("/", TaskView.create, methods=["POST"])
todo_router.add_api_route("/{id}/", TaskView.update, methods=["PUT"])
