import win32gui
import win32con
import time
def TestSetWorldTransform():
    wc = win32gui.WNDCLASS()
    print(dir(win32con))
    wc.lpszClassName = 'test_win32gui_1'
    wc.style =  win32con.CS_GLOBALCLASS|win32con.CS_VREDRAW
    wc.hbrBackground = win32con.COLOR_WINDOW+1
    class_atom=win32gui.RegisterClass(wc)
    hwnd = win32gui.CreateWindow(wc.lpszClassName,
        'Spin the Lobster!',
        win32con.WS_CAPTION|win32con.WS_VISIBLE,
        100,100,900,900, 0, 0, 0, None)
    while(True):
        win32gui.ShowWindow(hwnd, win32con.SW_SHOWNORMAL)
        win32gui.UpdateWindow(hwnd)

TestSetWorldTransform()
