import inject

from app.messages import Message
from domain.entities import Todo
from domain.ports import ITodoWriteRepository


class NewTodoHandler(object):

    @inject.autoparams("repository")
    def __init__(self, repository: ITodoWriteRepository):
        self.repository = repository

    def __call__(self, cmd: Message):
        self.repository.add(Todo(title=cmd.title))
