from typing import List

from app.exceptions import TodoNotFoundError
from app.ports import ITodoRepository
from domain.entities import Todo


_todos = {}


class TodoMemoryRepository(ITodoRepository):

    def add(self, todo: Todo) -> None:
        _todos[todo.uid] = todo.__dict__

    def get(self, uid: str) -> Todo:
        try:
            return _todos[uid]
        except KeyError:
            raise TodoNotFoundError()

    def get_all(self) -> List[Todo]:
        return list(_todos.values())
