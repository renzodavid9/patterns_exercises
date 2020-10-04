from ui_manager.manager import UIManager
from widgets.button.android_button import AndroidButton
from widgets.button.button import Button


class AndroidUIManager(UIManager):
    """ Android UI manager. """

    def create_button(self) -> Button:
      """ Creates and returns an Android button. """
      return AndroidButton()
