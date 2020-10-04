from widgets.button.button import Button


class AndroidButton(Button):
    """ Android button. """

    def click(self):
        """ Manages an Android button click. """
        print('Android button clicked!')


    def render(self) -> str:
        """ Renders an Android button. """
        return f'<buttonAndroid>Android! Click me!</buttonAndroid>'
