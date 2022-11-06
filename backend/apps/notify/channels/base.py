from abc import ABC

from django.core.validators import EmailValidator


class BaseChannel(ABC):
    def kind(self):
        return self.__class__.__name__
