from tkinter import *

root = Tk()
canvas = Canvas(
    root,
    bg="yellow",
    height=250,
    width=250
)
line = canvas.create_line(
    0, 0, 
    250, 250, 
    fill="green"
)
canvas.pack()
root.mainloop()