import stub
import random

availableStubs = stub.stubGeneration

class Character:
    def __init__(self, symbol):
        self.symbol = symbol
        self.stubs = []

    def getRandomStubs(self, stubCount):
        for i in range(stubCount):
            st = random.choice(range(len(availableStubs)))
            addStub = availableStubs[st]
            self.stubs.append(stub.Stub((random.random() * (addStub[1][1] - addStub[1][0])) + addStub[1][0], addStub[0], self.symbol))

    def getSymbol(self):
        return self.symbol

    def calculatePoints(self, board):
        totalPoints = [0, 0]
        for stub in self.stubs:
            points = stub.calculatePoints(board)
            if points[1] == 0:
                totalPoints[0] += points[0]
            else:
                totalPoints[1] += points[0]
        return totalPoints