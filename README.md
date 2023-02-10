# Glorious-Model-O-Profile-Change
Python code + ahk script for assigning a hotkey to switch between two profiles 
* ctr + f12 for profile 1
* ctr + f11 for profile 2
* ctr + f10 for profile 3


**the main issue are these messages** 

    profile1   = lambda: win32gui.PostMessage(hwnd,win32con.WM_USER+119,int("421DCB",16),1)
    profile2   = lambda: win32gui.PostMessage(hwnd,win32con.WM_USER+119,int("400BDE",16),1)
    profile3   = lambda: win32gui.PostMessage(hwnd,win32con.WM_USER+119,int("4228B7",16),1)

    
which are [win32 user defined messages](https://docs.microsoft.com/en-us/windows/win32/winmsg/wm-user).
the wparams (421DCB, 400BDE, 4228B7) are the ones the switch the profile (not apply it just change it) are likley different for every installation,
I had to get them using [Microsoft Spy++](https://learn.microsoft.com/en-us/visualstudio/debugger/introducing-spy-increment?view=vs-2022) and then clicking on each profile to get the wparam of the message.

Steps:
1. create a new venv called venv
2. pip install pywin32
3. get the wparams 
4. have the script run on startup
    
