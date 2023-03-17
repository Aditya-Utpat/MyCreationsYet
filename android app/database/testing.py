from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

# Create both screens. Please note the root.manager.current: this is how
# you can control the ScreenManager from kv. Each screen has by default a
# property manager that gives you the instance of the ScreenManager used.
Builder.load_string("""
<MenuScreen>:
    MDFlatButton:
        text: 'Goto settings'
        on_release: root.manager.current = 'settings'
        pos_hint:{'center_x':0.5,'center_y':0.5}
        size_hint_x:0.20
        size_hint_y:0.1
    MDFlatButton:
        text: 'Quit'
        size_hint_x:0.20
        size_hint_y:0.1
        pos_hint:{'center_x':0.5,'center_y':0.6}

<SettingsScreen>:
    BoxLayout:
        Button:
            text: 'My settings button'
        Button:
            text: 'Back to menu'
            on_press: root.manager.current = 'menu'
""")

# Declare both screens
class MenuScreen(Screen):
    pass

class SettingsScreen(Screen):
    pass

class TestApp(MDApp):

    def build(self):
        # Create the screen manager
        sm = ScreenManager()
        sm.add_widget(MenuScreen(name='menu'))
        sm.add_widget(SettingsScreen(name='settings'))

        return sm

if __name__ == '__main__':
    TestApp().run()
