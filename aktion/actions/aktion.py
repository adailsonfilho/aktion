from abc import ABC, abstractmethod


class Aktion(ABC):

    def __init__(self):
        ABC.__init__(self)

    @abstractmethod
    def __act__(self, *args, **kargs):
        raise NotImplementedError

    def act(self, *args, **kargs):
        return self.__act__(*args, **kargs)
