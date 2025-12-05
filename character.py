import stub
import random

availableStubs = stub.stubGeneration


# a tile type
class Character:
    def __init__(self, symbol):
        self.symbol = symbol
        self.stubs = []


# this is where point methods (stubs) get generated
    def getRandomStubs(self, stubCount):
        for i in range(stubCount):
            st = random.choice(range(len(availableStubs)))
            addStub = availableStubs[st]
            self.stubs.append(stub.Stub((random.random() * (addStub[1][1] - addStub[1][0])) + addStub[1][0], addStub[0], self.symbol))

    def getSymbol(self):
        return self.symbol


# calculate points for this one character on a board
    def calculatePoints(self, board):
        totalPoints = [0, 0]
        for stub in self.stubs:
            points = stub.calculatePoints(board)
            if points[1] == 0:
                totalPoints[0] += points[0]
            else:
                totalPoints[1] += points[0]
        return totalPoints