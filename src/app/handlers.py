import logging

import inject

from app.messages import Message
from domain.entities import Todo
from domain.ports import ITodoWriteRepository


logger = logging.getLogger(__name__)


class NewTodoHandler(object):

    @inject.autoparams("repository")
    def __init__(self, repository: ITodoWriteRepository):
        self.repository = repository

    def __call__(self, cmd: Message):
        validated_data = Todo.validate(title=cmd.title)
        self.repository.add(Todo(**validated_data))
