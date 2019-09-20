import inject

from adapters.repositories import TodoReadMemoryRepository, TodoWriteMemoryRepository
from app.messages import MessageBus, NewTodoCommand
from app.handlers import NewTodoHandler
from domain.ports import ITodoWriteRepository


def di_config(binder):
    binder.bind(ITodoWriteRepository, TodoWriteMemoryRepository())


inject.configure(di_config)

bus = MessageBus()

todo_read_repository = TodoReadMemoryRepository()

bus.subscribe_to(NewTodoCommand, NewTodoHandler())
