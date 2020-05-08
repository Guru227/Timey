"""Generate a pop-up window for special messages."""
from tkinter import *
import tkinter.font as font
def alert_popup(title, message, path):
    
    root = Tk()
    root.title(title)
    w = 600     # popup window width
    h = 200     # popup window height
    sw = root.winfo_screenwidth()
    sh = root.winfo_screenheight()    
    x = (sw - w)/2
    y = (sh - h)/2
    root.geometry('%dx%d+%d+%d' % (w, h, x, y))
    #top padding
    p1 = Label(root, text='', width = 50, height = 2)
    p1['font'] = font.Font(size=15)
    p1.pack()
    #head label
    head = Label(root, text=message, width = 50, height = 1)
    head['font'] = font.Font(size=20)
    head.pack()
    #quote
    quote = Label(root, text=path, width=120, height = 1)
    quote.pack()
    #padding between button and quote
    p2 = Label(root, text='', width = 50, height = 2)
    p2.pack()
    #button
    b = Button(root, text="OK", command=root.destroy, width=10)
    b.pack()
    mainloop()



