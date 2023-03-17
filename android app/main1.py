from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.widget import Widget
from kivy.graphics import Rectangle, Color, Line
from plyer import storagepath
import os

Builder.load_file('ui.kv')
path = str(storagepath.get_documents_dir())

try:
    os.mkdir(os.path.join(path+'\\Typewriter'))
except Exception as e:
    print(e)
path = path + '\\Typewriter'
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
class StartScreen(Screen):
    pass
class MainScreen(Screen):
    def go_doc(self,doc):
        self.manager.current = 'Edit'
        self.manager.screens[2].set_doc(doc)
class EditScreen(Screen):
    def set_doc(self,doc):
        self.doc = doc
        print(self.doc)

class MyApp(MDApp):

    def build(self):
        self.theme_cls.primary_palette="Indigo"

        self.sm= ScreenManager()
        self.sm.add_widget(StartScreen(name='start'))
        self.sm.add_widget(MainScreen(name='Main'))
        self.sm.add_widget(EditScreen(name='Edit'))
        self.sm.screens[2].ids['edit'].add_widget(DrawingWidget(size_hint_y=0.5))
        files = os.listdir(path)
        if len(files) == 0 : self.sm.screens[1].ids['file_list'].add_widget(Builder.load_string('MDLabel:\n    text:"No Files"\n    halign:"center"\n    theme_text_color:"Secondary"'))
        for j in files:
            i = j.split('.')
            print(path)
            if i[1] == 'docx':
                a = 'OneLineAvatarListItem:\n    on_press:root.parent.parent.parent.go_doc(r"'+path+'\\'+j+'")\n    text:"'+i[0]+'"\n    IconLeftWidget:\n        icon:"file-word-outline"\n        on_press:root.parent.parent.parent.go_doc(r"'+path+'\\'+j+'")\n'
                self.sm.screens[1].ids['file_list'].add_widget(Builder.load_string(a))
            elif i[1] == 'pdf':
                a = 'OneLineAvatarListItem:\n    on_press:root.parent.parent.parent.go_doc(r"'+path+'\\'+j+'")\n    text:"'+i[0]+'"\n    IconLeftWidget:\n        icon:"file-pdf-outline"\n        on_press:root.parent.parent.parent.go_doc(r"'+path+'\\'+j+'")\n'
                self.sm.screens[1].ids['file_list'].add_widget(Builder.load_string(a))
            else:
                if len(files) == 0 : self.sm.screens[1].ids['file_list'].add_widget(Builder.load_string('MDLabel:\n    text:"No Files"\n    halign:"center"\n    theme_text_color:"Secondary"'))
        return self.sm
a = MyApp()
a.run()
