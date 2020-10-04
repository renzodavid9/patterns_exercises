from ui_manager.manager import UIManager
from widgets.button.button import Button
from widgets.button.ios_button import IOSButton


class IOSUIManager(UIManager):
    """ iOS UI manager. """

    def create_button(self) -> Button:
      """ Creates and returns an iOS button. """
      return IOSButton()
