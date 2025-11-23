from tkinter import *
from tkinter import ttk
from pprint import pprint

# store bounds of the rectangle to observe
start_x = None
start_y = None
end_x = None
end_y = None

# create a fullscreen that exists above all other elements
screen = Tk()
screen.attributes("-fullscreen", True)
screen.attributes("-alpha", 0.4)

# add a canvas to that screen
canvas = Canvas(screen, cursor="cross", background="black")
canvas.pack(fill="both", expand=True)

# define handlers for mouse press, release, and move
def press(pos):
    global start_x, start_y
    start_x = pos.x
    start_y = pos.y

def release(pos):
    global end_x, end_y
    end_x = pos.x
    end_y = pos.y

def move(pos):
    global start_x, start_y
    canvas.delete("all")
    canvas.create_rectangle(
        start_x, start_y, 
        pos.x, pos.y, 
        fill="green"
    )

def quit(_):
    screen.quit()

# attach handlers
screen.bind("<ButtonPress-1>", press)
screen.bind("<ButtonRelease-1>", release)
screen.bind("<B1-Motion>", move)
screen.bind("q", quit)

def setup_screen():
    mainloop()
    print(start_x, start_y, end_x, end_y)

setup_screen()