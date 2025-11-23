from tkinter import *
from tkinter import ttk
from pprint import pprint

stored_x = None
stored_y = None

root = Tk()
frame = ttk.Frame(root, padding=10)
frame.grid()
ttk.Label(frame, text="Hello World!").grid(column=0, row=0)
ttk.Button(frame, text="Quit", command=root.destroy).grid(column=1, row=0)

# create a fullscreen that exists above all other elements
screen = Toplevel(root)
screen.attributes("-fullscreen", True)
screen.attributes("-alpha", 0.4)

# add a canvas to that frame
canvas = Canvas(screen, cursor="cross", background="black")
canvas.pack(fill="both", expand=True)

def press(pos):
    global stored_x, stored_y
    stored_x = pos.x
    stored_y = pos.y

def release(pos):
    global stored_x, stored_y
    canvas.create_rectangle(
        stored_x, stored_y, 
        pos.x, pos.y, 
        fill="green"
    )

def move(pos):
    global stored_x, stored_y
    canvas.delete("all")
    canvas.create_rectangle(
        stored_x, stored_y, 
        pos.x, pos.y, 
        fill="green"
    )

screen.bind("<ButtonPress-1>", press)
screen.bind("<ButtonRelease-1>", release)
screen.bind("<B1-Motion>", move)

mainloop()