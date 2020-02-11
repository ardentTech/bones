import inject

from adapters.repositories import TodoMemoryRepository
from adapters.views import TodoListView
from app.handlers import NewTodoHandler
from app.messages import MessageBus, NewTodoCommand
from app.ports import ITodoRepository


def di_config(binder):
    binder.bind(ITodoRepository, TodoMemoryRepository())


inject.configure(di_config)

bus = MessageBus()

bus.subscribe_to(NewTodoCommand, NewTodoHandler())

todo_list_view = TodoListView()
