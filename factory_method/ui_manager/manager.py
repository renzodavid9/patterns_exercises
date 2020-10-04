from __future__ import annotations
from abc import ABC, abstractmethod
from widgets.button.button import Button


class UIManager(ABC):
    """
    UI Manager for each specific operative system.
    """

    @abstractmethod
    def create_button(self) -> Button:
        """ Creates and returns a new instance of a button."""
        pass

    def create_ui(self):
        """ Returns a dict with instances of widgets to use in the UI."""

        return {
          'button': self.create_button()
        }
