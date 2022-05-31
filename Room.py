import numpy as np
from random import randint

MIN = 3
MAX = 7

def r(x = MIN,y = MAX):
    return randint(x, y)

class Room:
    def __init__(self, rows=r(), columns=r()):
        self.rows = rows
        self.columns = columns
        self.zFloor = ""
        self.floor = ""
        self.newFloor(rows,columns)
        print(self.floor)

    def getFloor(self):
        return self.floor

    def newFloor(self, rows=r(), columns=r()):
        self.rows = rows
        self.columns = columns
        self.createZFloor(rows, columns)
        self.addUnit(1, (1,1))
        self.addUnit(2,(2,2))
        self.drawFloor()
        return self

    def createZFloor(self,rows, columns):
        self.zFloor = np.zeros((rows, columns))
        return self

    def addUnit(self,num, coords):
        x = coords[0]
        y = coords[1]

        print(self.zFloor[y][x], num)
        # collision
        if self.zFloor[y][x] == 0.0:
            print("free")
            self.zFloor[y][x] = num

        elif self.zFloor[y][x + 1] == 0.0:
            print("look right", self.zFloor[y][x+1])
            self.zFloor[y][x + 1] = num

        elif self.zFloor[y][x - 1] == 0.0:
            print("look left", self.zFloor[y][x-1])

            self.zFloor[x][x - 1] = num

        return self

    def drawFloor(self):
        rows = self.rows
        cols = self.columns

        # self.zFloor = self.addUnit(1, (0, 0))
        # self.zFloor = self.addUnit(2, (1, 1))

        self.floor = f"{'___' * cols }\n"
        for row in self.zFloor:
            self.floor += "| "
            for tile in row:
                if tile == 1:
                    self.floor += " @ "
                elif tile == 2:
                    self.floor += " # "
                elif tile == 0:
                    self.floor += "  .  "
            self.floor += " |\n"
        self.floor += f"{'___' * cols}"
        return self

r = Room(5, 5)