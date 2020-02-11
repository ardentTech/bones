from typing import List

from app.ports import ITodoRepository
from domain.entities import Todo


_todos = {}


class TodoMemoryRepository(ITodoRepository):

    def add(self, todo: Todo) -> None:
        _todos[todo.title] = todo.__dict__

    def get_all(self) -> List[Todo]:
        return list(_todos.values())
