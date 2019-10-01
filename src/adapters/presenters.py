import abc
from typing import Any


class IPresenter(abc.ABC):

    @abc.abstractmethod
    def __call__(self, data: Any):
        pass


class NoOpPresenter(IPresenter):

    def __call__(self, data: Any):
        return data
