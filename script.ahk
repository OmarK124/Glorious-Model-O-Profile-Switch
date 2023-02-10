#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
; #Warn  ; Enable warnings to assist with detecting common errors.
#SingleInstance Force
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.
^F12::
run, venv\Scripts\pythonw.exe main.pyw profile2
return

^F11::
run, venv\Scripts\pythonw.exe main.pyw profile1
return

^F10::
run, venv\Scripts\pythonw.exe main.pyw profile3
return

