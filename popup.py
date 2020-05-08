"""Generate a pop-up window for Timey."""
try:                        # Python2  
    from Tkinter import *       # capital 'T'
    import Tkinter.font as font
    import thread 
except ImportError:         # Python3
    from tkinter import *       # lowercase 't'
    import tkinter.font as font
    import _thread as thread    # Note: backward compatibility
import time


def alert_popup(title, message, path):
    
    root=init_window(title)
    make_stubborn(root)

    #structure
    padding(root, 2, 15)
    make_label(root, message, 20)
    make_label(root, path, 9)
    padding(root, 2, 9)
    make_quit(root, "OK")
    
    mainloop()

def init_window(t): #title
    box = Tk()
    box.title(t)
    w = 600     # popup window width
    h = 200     # popup window height
    sw = box.winfo_screenwidth()
    sh = box.winfo_screenheight()    
    x = (sw - w)/2
    y = (sh - h)/2
    box.geometry('%dx%d+%d+%d' % (w, h, x, y))
    return box

# disable [x] and exit of tkinter window
def disable_event():
        pass
    
def make_stubborn(box):
    box.overrideredirect(True)
    box.protocol("WM_DELETE_WINDOW", disable_event)
    
def padding(box, h, f):     #height, font size
    p = Label(box, text='', height = h)
    p['font'] = font.Font(size=f)
    p.pack()

def make_label(box, t, f):  #text, font size
    lbl = Label(box, text=t, height = 1)
    lbl['font'] = font.Font(size=f)
    lbl.pack()

#window destroy button
def make_quit(box, txt):    #button text 
    b = Button(box, text=txt, command = box.destroy, width=10, state='disabled')
    b.pack()
    thread.start_new_thread(stall, (b, ))

#enable button after 30 sec
def stall(object):
    print("stall running")
    time.sleep(30)
    object.config(state = 'normal')
    
    
if(__name__ == "__main__"):
    alert_popup("Timey", "Up you go!", "Time to stretch")
