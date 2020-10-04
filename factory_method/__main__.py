from app.app import App
from app.environments import Environments
from ui_manager.android_manager import AndroidUIManager
from ui_manager.ios_manager import IOSUIManager


ui_managers = {
  Environments.ANDROID: AndroidUIManager,
  Environments.IOS: IOSUIManager,
}

android_app = App(ui_managers.get(Environments.ANDROID)())
ios_app = App(ui_managers.get(Environments.IOS)())

print(android_app.render_button())
android_app.click_button()

print()

print(ios_app.render_button())
ios_app.click_button()
