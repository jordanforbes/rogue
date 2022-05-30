import numpy as np
from random import randint as r


def createZField(rows=r(2,9),columns=r(2,9)):
    field = np.zeros((rows,columns))
    return field


def main():
    field = createZField()
    print(field)

if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
