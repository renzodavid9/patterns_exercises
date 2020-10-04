class App:
    def __init__(self, ui_manager):
        """ App's constructor. """
        self.ui_manager = ui_manager

        self.widgets = self.ui_manager.create_ui()


    def click_button(self):
        """ Clicks an app button. """
        self.widgets.get('button').click()


    def render_button(self):
        """ Renders an app button. """
        return self.widgets.get('button').render()



