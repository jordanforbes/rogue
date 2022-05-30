import numpy as np
from random import randint
from tkinter import *

MIN = 3
MAX = 7

def r(x = MIN,y = MAX):
    return randint(x, y)

def createZField(rows = r(), columns = r()):
    zfield = np.zeros((rows,columns))
    return zfield

def addUnit(num, zfield, coords):
    x = coords[0]
    y = coords[1]

    tile = zfield[y][x]

    #collision
    if tile == 0:
        zfield[y][x] = num

    elif zfield[y][x+1]:
        zfield[y][x+1] = num
    elif zfield[y][x-1]:
        zfield[x][x-1] = num

    return zfield

def drawField(rows,columns):
    zfield = createZField(rows,columns)
    zfield = addUnit(1, zfield, (r(0, 9), r(0, 9)))
    zfield = addUnit(2, zfield, (r(0, 9), r(0, 9)))
    field = ""
    field += f"{'___' * columns}\n"
    for row in zfield:
        field += "| "
        for tile in row:
            if tile == 1:
                field += "@"
            elif tile == 2:
                field += "#"
            elif tile == 0:
                field += " . "
        field += " |\n"
    field += f"{'___' * columns}"
    return field



def drawWindow( rows, columns):
    field = str(drawField(10,10))
    window = Tk()
    window.title("main")
    window.configure(width=400, height=400)
    window.geometry("400x400")
    title = Label(window, text="ROGUE")
    title.pack()
    label = Label(window, text=field)
    label.pack()

    window.mainloop()

def main():
    drawWindow(20,20)

if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
