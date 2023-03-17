from kivymd.app import MDApp
#from kivy import uix
from kivy.core.window import Window
from plyer import gps

class MyApp(MDApp):
    def on_start(self):
        gps.configure(on_location= self.on_gps_location)
        gps.start()
    def on_gps_location(self,**kwargs):
        kwargs['lat'] = 10.0
    def build(self):
        #self.sm = ScreenManager()
        pass
MyApp().run()
