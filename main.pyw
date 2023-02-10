import win32api, win32con, win32gui
import time
import sys




def leftClick(x,y,hwnd,sleep=0.1,sleepAfter=0.2,dontMove = False):
        """Click at pixel xy."""
        lParam = win32api.MAKELONG(x, y)
        if dontMove == False:
            win32gui.PostMessage(hwnd, win32con.WM_MOUSEMOVE, 0, lParam)
        win32gui.PostMessage(hwnd, win32con.WM_LBUTTONDOWN,
                                win32con.MK_LBUTTON, lParam)
        win32gui.PostMessage(hwnd, win32con.WM_LBUTTONUP,
                                win32con.MK_LBUTTON, lParam)
        time.sleep(sleepAfter)
        
def get_children(hwnd, param):
    child_handles.append(hwnd)    
child_handles = []





hwnd = win32gui.FindWindow(None,"Glorious Model O Software")
win32gui.EnumChildWindows(hwnd, get_children, None)

box = child_handles[11]#handle to box containing profiles
apply = child_handles[3]#handle to apply button
profile1   = lambda: win32gui.PostMessage(hwnd,win32con.WM_USER+119,int("421DCB",16),1)
profile2   = lambda: win32gui.PostMessage(hwnd,win32con.WM_USER+119,int("400BDE",16),1)
profile3   = lambda: win32gui.PostMessage(hwnd,win32con.WM_USER+119,int("4228B7",16),1)


leftClick(0,0,box)
arg = sys.argv[1]
if arg == "profile1":
    profile1()
elif arg == "profile2":
    profile2()
elif arg == "profile3":
    profile3()
leftClick(0,0,apply)