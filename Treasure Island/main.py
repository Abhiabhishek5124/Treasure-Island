from random import randint

class IslandClass:
    def __init__(self):
        Sand = '.'
        self.__Grid = [[Sand for _ in range(30)] for _ in range(10)]

    def GetSquare(self, x, y):
        return self.__Grid[x][y]

    def HideTreasure(self):
        Treasure = 'T'
        x = randint(0, 9)
        y = randint(0, 29)
        while self.__Grid[x][y] == Treasure:
            x = randint(0, 9)
            y = randint(0, 29)
        self.__Grid[x][y] = Treasure

    def DigHole(self, x, y):
        Treasure = 'T'
        Hole = 'O'
        Foundtreasure = 'X'
        if self.__Grid[x][y] == Treasure:
            self.__Grid[x][y] = Foundtreasure
        else:
            self.__Grid[x][y] = Hole

def DisplayGrid(island):
    for i in range(10):
        for j in range(30):
            print(island.GetSquare(i, j),2)
        print()

def StartDig(island):
    Valid = False
    while not Valid:  # validate down position
        try:
            x = int(input("Enter the row position (0 to 9): "))
            if 0 <= x <= 9:
                Valid = True
        except:
            Valid = False

    Valid = False
    while not Valid:  # validate across position
        try:
            y = int(input("Enter the column position (0 to 29): "))
            if 0 <= y <= 29:
                Valid = True
        except:
            Valid = False

    island.DigHole(x, y)

# Main code
Island = IslandClass()
DisplayGrid(Island)

for _ in range(3):
    Island.HideTreasure()

StartDig(Island)
DisplayGrid(Island)
