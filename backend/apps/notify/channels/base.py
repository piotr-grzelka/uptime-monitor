from abc import ABC


class BaseChannel(ABC):
    """
    Base class for all notification channels
    """

    def kind(self):
        """
        Should return unique channel identifier
        """
        return self.__class__.__name__

    def form_fields(self):
        """
        Should return form field for channel
        @return:
        """
        raise NotImplementedError("Form fields not implemented")
