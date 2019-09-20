from typing import List

from domain.entities import Todo
from domain.ports import ITodoReadRepository, ITodoWriteRepository


_todos = {}


class TodoReadMemoryRepository(ITodoReadRepository):

    def get_all(self) -> List[Todo]:
        return list(_todos.values())


class TodoWriteMemoryRepository(ITodoWriteRepository):

    def add(self, todo: Todo) -> None:
        _todos[todo.title] = todo.__dict__
