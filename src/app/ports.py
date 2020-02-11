import abc
from typing import List

from domain.entities import Todo


class ITodoRepository(abc.ABC):

    @abc.abstractmethod
    def add(self, todo: Todo) -> None:
        pass

    @abc.abstractmethod
    def get_all(self) -> List[Todo]:
        pass
