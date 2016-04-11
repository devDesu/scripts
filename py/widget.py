import ImageGrab
import win32gui
import thread
from time import sleep

from Tkinter import *
root = Tk()
root.wm_attributes("-topmost", 1)
var = StringVar()
var.set('hello')
lb = Label(root, textvariable=var)

lb.pack()

def gPx():
    px=ImageGrab.grab().load()
    _, _, tupl = win32gui.GetCursorInfo()
    #print tupl
    var.set(px[int(tupl[0]),int(tupl[1])])#win32gui.GetCursorPos(point)]
    root.after(200,gPx)

root.after(10,gPx)
#thread.start_new_thread(gPx, ())
root.mainloop()
