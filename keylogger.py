from pynput.keyboard import Listener
from os import system

con = False
def release(key):
    global con
    if str(key)== "'c'" and con == True:
        system('C:\\Users\\aditya\\Desktop\\Windows_Terminal_Shortcut.lnk')
        con= False
def press(key):
    global con
    if str(key) == "Key.f1":
        con = True
with Listener(on_release=release,on_press=press) as l:
    l.join()
