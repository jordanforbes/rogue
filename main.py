import numpy as np
from random import randint
from tkinter import *
from Room import Room

MIN = 3
MAX = 7


def r(x=MIN, y=MAX):
    return randint(x, y)

global room
room = Room(r(),r())


def randFloor():
    newFloor = room.newFloor(r(),r()).getFloor()
    dungeon.config(text=newFloor)
    print(newFloor)

if __name__ == '__main__':
    window = Tk()

    window.title("main")
    window.configure(width=400, height=400)
    window.geometry("400x400")

    title = Label(window, text="ROGUE")
    title.pack()

    dungeon = Label(window, text=room.getFloor())
    randomize = Button(window, text="randomize", command=randFloor)
    dungeon.pack()
    randomize.pack()

    window.mainloop()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
