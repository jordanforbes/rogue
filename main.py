import numpy as np
from random import randint
from tkinter import *

def r(x=3,y=7):
    return randint(x,y)

def createZField(rows=r(),columns=r()):
    zfield = np.zeros((rows,columns))
    return zfield

def drawField(rows,columns):
    zfield = createZField(rows, columns)
    field = ""
    for row in zfield:
        field += "| "
        for tile in row:
            if tile == 0:
                field += " . "
        field += " |\n"
    return field

def drawWindow(rows,columns):
    field = str(drawField(r(),r()))
    window = Tk()
    window.title("main")
    window.configure(width=400, height=400)
    window.geometry("400x400")

    label = Label(window, text=field)
    label.pack()

    window.mainloop()

def main():
    field = createZField()
    print(field)
    drawWindow(20,20)

if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
