from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.graphics import Rectangle, Color, Line
a='''
MDTextField:
    hint_text: "Enter username"
    helper_text: "or click on forgot username"
    helper_text_mode: "on_focus"
    icon_right: "android"
    icon_right_color: app.theme_cls.primary_color
    pos_hint:{'center_x': 0.5, 'center_y': 0.5}
    size_hint_x:None
    width:300
    '''
class w(Widget):
    def on_touch_down(self,touch):
        with self.canvas:
            Color(1,0,0 )
            self.line = Line(points=[touch.pos[0], touch.pos[1]], width=2)
    def on_touch_move(self, touch):
        self.line.points = self.line.points + [touch.pos[0], touch.pos[1]]

class DrawingApp(MDApp):

    def build(self):
        self.theme_cls.primary_palette="Green"
        screen= Screen()
        username = Builder.load_string(a)
        screen.add_widget(w())
        screen.add_widget(username)
        return screen

DrawingApp().run()
