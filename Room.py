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
        self.addUnit(1, (1,1)).addUnit(2,(1,1)).addUnit(2,(1,0)).addUnit(2,(1,1)).addUnit(2,(1,1))
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

        elif self.zFloor[y][x + 1] == 0.0:
            print("look right", self.zFloor[y][x+1])
            x += 1

        elif self.zFloor[y][x - 1] == 0.0:
            print("look left", self.zFloor[y][x-1])
            x -= 1

        elif self.zFloor[y + 1][x] == 0.0:
            print("look up", self.zFloor[y + 1][x])
            y += 1

        elif self.zFloor[y-1][x] == 0.0:
            print("look down", self.zFloor[y-1][x])
            y -= 1

        self.zFloor[y][x] = num
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

    def idTile(self,x,y):
        tile = self.zfield[y][x]
        if tile:
            return tile
        else:
            return False

r = Room(5, 5)