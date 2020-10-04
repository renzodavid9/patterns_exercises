from widgets.button.button import Button


class IOSButton(Button):
    """ iOS button. """

    def click(self):
        """ Manages an IOS button click. """
        print('iOS button clicked!')


    def render(self) -> str:
        """ Renders an IOS button. """
        return f'<button>iOS button!</button>'
