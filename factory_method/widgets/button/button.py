from __future__ import annotations
from abc import ABC
from abc import abstractmethod

class Button(ABC):
    """ Abstract representation of a button. """

    @abstractmethod
    def click(self):
        """ Manages a button click. """
        pass

    @abstractmethod
    def render(self) -> str:
        """ Renders a button. """
        pass
