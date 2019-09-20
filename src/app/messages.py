import abc
from collections import defaultdict
from dataclasses import dataclass


class CommandAlreadySubscribedError(Exception):
    pass


class Message(abc.ABC):
    pass


@dataclass(frozen=True)
class NewTodoCommand(Message):
    title: str


class MessageBus(object):

    def __init__(self):
        self.subscribers = defaultdict(list)

    def handle(self, msg: Message) -> None:
        subscribers = self.subscribers[type(msg).__name__]
        for subscriber in subscribers:
            subscriber(msg)

    def subscribe_to(self, msg: Message, handler):
        subscribers = self.subscribers[msg.__name__]
        if "Command" in msg.__name__ and len(subscribers) > 0:
            raise CommandAlreadySubscribedError(msg.__name__)
        subscribers.append(handler)
