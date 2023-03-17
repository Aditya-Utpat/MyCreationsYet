from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.uix.label import MDLabel
from kivy.core.window import Window
from kivy.lang import Builder
build = lambda : Builder.load_string('''
<StartScreen>:
    MDLabel:
        text:'A game of'
        halign:'center'
        valign:'top'
        font_size:'50px'
        pos_hint:{'center_x':0.5,'center_y':0.80}
    MDLabel:
        text:'XO'
        halign:'center'
        valign:'top'
        font_size:'100px'
        pos_hint:{'center_x':0.5,'center_y':0.65}
    MDFlatButton:
        text:'Start Game'
        halign:'center'
        valign:'top'
        font_size:'20px'
        pos_hint:{'center_x':0.5,'center_y':0.45}
        theme_text_color:'Custom'
        text_color:self.theme_cls.primary_color
        on_release:root.manager.current='game'
<GameScreen>:
    name: 'game'
    MDLabel:
        id:L
        text:'X turn'
        halign:'center'
        valign:'top'
        font_size:'50px'
        pos_hint:{'center_x':0.5,'center_y':0.80}
    MDFloatingActionButton:
        id:1
        halign:'center'
        valign:'top'
        font_size:'50px'
        pos_hint:{'center_x':0.20,'center_y':0.70}
        on_release: root.press(1)
        icon:'checkbox-blank-circle'
    MDFloatingActionButton:
        id:2
        halign:'center'
        valign:'top'
        font_size:'50px'
        pos_hint:{'center_x':0.5,'center_y':0.70}
        on_release: root.press(2)
        icon:'checkbox-blank-circle'
    MDFloatingActionButton:
        id:3
        halign:'center'
        valign:'top'
        font_size:'50px'
        pos_hint:{'center_x':0.80,'center_y':0.70}
        on_release: root.press(3)
        icon:'checkbox-blank-circle'
    MDFloatingActionButton:
        id:4
        halign:'center'
        valign:'top'
        font_size:'50px'
        pos_hint:{'center_x':0.20,'center_y':0.5}
        on_release: root.press(4)
        icon:'checkbox-blank-circle'
    MDFloatingActionButton:
        id:5
        halign:'center'
        valign:'top'
        font_size:'50px'
        pos_hint:{'center_x':0.5,'center_y':0.5}
        on_release: root.press(5)
        icon:'checkbox-blank-circle'
    MDFloatingActionButton:
        id:6
        halign:'center'
        valign:'top'
        font_size:'50px'
        pos_hint:{'center_x':0.80,'center_y':0.5}
        on_release: root.press(6)
        icon:'checkbox-blank-circle'
    MDFloatingActionButton:
        id:7
        halign:'center'
        valign:'top'
        font_size:'50px'
        pos_hint:{'center_x':0.20,'center_y':0.30}
        on_release: root.press(7)
        icon:'checkbox-blank-circle'
    MDFloatingActionButton:
        id:8
        halign:'center'
        valign:'top'
        font_size:'50px'
        pos_hint:{'center_x':0.5,'center_y':0.30}
        on_release: root.press(8)
        icon:'checkbox-blank-circle'
    MDFloatingActionButton:
        id:9
        halign:'center'
        valign:'top'
        font_size:'50px'
        pos_hint:{'center_x':0.80,'center_y':0.30}
        on_release: root.press(9)
        icon:'checkbox-blank-circle'
<OverScreen>:
    MDLabel:
        id:L
        halign:'center'
        valign:'top'
        font_size:'50px'
        pos_hint:{'center_x':0.50,'center_y':0.50}
    MDFlatButton:
        text:'Restart'
        halign:'center'
        valign:'top'
        font_size:'20px'
        pos_hint:{'center_x':0.50,'center_y':0.40}
        on_release: app.restart()
        theme_text_color:'Custom'
        text_color:self.theme_cls.primary_color
''')
build()
turn ='X'
state = {1:None,2:None,3:None,4:None,5:None,6:None,7:None,8:None,9:None}
class StartScreen(Screen):
    pass
class GameScreen(Screen):

    def press(self,id):
        global turn
        combs = {1:[[1,2,3],[1,4,7],[1,5,9]],2:[[1,2,3],[2,5,8]],3:[[1,2,3],[3,5,7],[3,6,9]],4:[[4,5,6],[1,4,7]],5:[[2,5,8],[4,5,6],[3,5,7],[1,5,9]],6:[[3,6,9],[4,5,6]],7:[[7,8,9],[3,5,7],[1,4,7]],8:[[2,5,8],[7,8,9]],9:[[7,8,9],[3,6,9],[1,5,9]]}
        ps = 0
        if turn == 'X':

            if state[id] == None:
                state[id] = 'X'
                self.ids[str(id)].icon = 'alpha-x-circle-outline'
                for i in combs[id]:
                    for j in i:
                        if state[j] == 'X':
                            ps+=1
                        else:
                            ps=0
                            break

                    if ps == 3:
                        self.ids['L'].text = 'X wins'
                        self.manager.screens[2].ids['L'].text = 'X wins'
                        self.manager.current = 'over'
                        break
                    else:
                        if None not in state.values():
                            self.manager.screens[2].ids['L'].text = 'Tie'
                            self.manager.current = 'over'
                        else:
                            turn = 'O'
                            self.ids['L'].text = 'O turn'
        else:
            if state[id] == None:
                state[id] = 'O'
                self.ids[str(id)].icon = 'alpha-o-circle-outline'
                for i in combs[id]:
                    for j in i:
                        if state[j] == 'O':
                            ps+=1
                        else:
                            ps=0
                            break
                    if ps == 3:
                        self.manager.screens[2].ids['L'].text = 'O wins'
                        self.manager.current = 'over'
                        break
                    else:
                        if None not in state.values():
                            self.manager.screens[2].ids['L'].text = 'Tie'
                            self.manager.current = 'over'
                        else:
                            turn = 'X'
                            self.ids['L'].text = 'X turn'
class OverScreen(Screen):
    pass
class XOApp(MDApp):
    def restart(self):
        global state
        global turn
        turn ='X'
        state = {1:None,2:None,3:None,4:None,5:None,6:None,7:None,8:None,9:None}
        self.sm.current = 'start'
        for i in range(1,10):
            self.sm.screens[1].ids[str(i)].icon='checkbox-blank-circle'
        self.sm.screens[1].ids['L'].text='X turn'
    def build(self):
        self.sm = ScreenManager()
        self.sm.add_widget(StartScreen(name ='start'))
        self.sm.add_widget(GameScreen(name='game'))
        self.sm.add_widget(OverScreen(name='over'))
        self.theme_cls.primary_palette="Red"
        print(self.sm.screens)
        return self.sm
XOApp().run()
