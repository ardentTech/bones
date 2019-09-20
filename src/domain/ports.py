import abc
from typing import List

from domain.entities import Todo


class ITodoReadRepository(abc.ABC):

    @abc.abstractmethod
    def get_all(self) -> List[Todo]:
        pass


class ITodoWriteRepository(abc.ABC):

    @abc.abstractmethod
    def add(self, todo: Todo) -> None:
        pass
