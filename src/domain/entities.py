import abc
import logging
from typing import Dict

from cerberus import Validator

from domain.exceptions import ValidationError


logger = logging.getLogger(__name__)


class Entity(abc.ABC):

    @classmethod
    def validate(cls, **kwargs) -> Dict:
        v = Validator(cls.VALIDATION_SCHEMA)
        v.validate(kwargs)
        if v.errors:
            e = ValidationError()
            e.errors = v.errors
            raise e
        else:
            return v.document


class Todo(Entity):

    VALIDATION_SCHEMA = {
        "title": {"minlength": 2, "type": "string"},
        "uid": {"type": "string"}
    }

    def __init__(self, title: str, uid: str) -> None:
        self.title = title
        self.uid = uid
