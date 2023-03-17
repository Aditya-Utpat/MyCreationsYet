from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

from kivy.uix.widget import Widget
from kivy.graphics import Rectangle, Color, Line

from random import random
import time

class DrawingWidget(Widget):
    def on_touch_down(self, touch):
        #self.rect_colour.rgb = (random(), random(), random())
        #print('touch pos is {}'.format(touch.pos))
        super(DrawingWidget, self).on_touch_down(touch)

        with self.canvas:
            Color(1,0,0 )
            self.line = Line(points=[touch.pos[0], touch.pos[1]], width=2)

    def on_touch_move(self, touch):
        self.line.points = self.line.points + [touch.pos[0], touch.pos[1]]
    def on_touch_up(self,touch):
        print(self.line.points)
        self.line.points = [0.0,0.0]
class DrawingApp(App):

    def build(self):
        root_widget = DrawingWidget()
        return root_widget

DrawingApp().run()
