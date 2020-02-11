import logging

import inject

from app.messages import Message
from app.ports import ITodoRepository
from domain.entities import Todo


logger = logging.getLogger(__name__)


class NewTodoHandler(object):

    @inject.autoparams("repository")
    def __init__(self, repository: ITodoRepository):
        self.repository = repository

    def __call__(self, cmd: Message) -> None:
        validated_data = Todo.validate(title=cmd.title)
        self.repository.add(Todo(**validated_data))
