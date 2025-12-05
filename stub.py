import math


class Stub():
    def __init__(self, pointValue, calculateMethod, applyTo=None):
        self.pointValue = pointValue
        self.calcMethod = calculateMethod
        self.applyToChar = applyTo


    def calculatePoints(self, board):
        # target will be 0 if self, and 1 if enemy
        return self.calcMethod(board, self.pointValue, self.applyToChar)


# give 'val' points for each character
def countChar(board, val, apply):
    total = 0
    for tile in board:
        if tile[0] == apply:
            total += val
    return total, 0


# give val of points per adjacent char
def countAdj(board, val, apply):
    total = 0
    for tile in board:
        if tile[0] == apply:
            for tile2 in board:
                if math.fabs(tile[1][0] - tile2[1][0]) + math.fabs(tile[1][1] - tile2[1][1]) == 1:
                    total += val
    return total, 0


# takes val of points per adjacent char
def minusAdj(board, val, apply):
    total = 0
    for tile in board:
        if tile[0] == apply:
            total += val * 4
            for tile2 in board:
                if math.fabs(tile[1][0] - tile2[1][0]) + math.fabs(tile[1][1] - tile2[1][1]) == 1:
                    total -= val
    return total, 0


def countChar2(board, val, apply):
    total = 0
    for tile in board:
        if tile[0] == apply:
            total += 1
    total *= total
    total *= val
    return total, 0


def rowShare(board, val, apply):
    total = 0
    for tile in board:
        if tile[0] == apply:
            for tile2 in board:
                if tile2[1][0] == tile[1][0] and tile2[1][1] != tile[1][1] and tile2[0] == apply:
                    total += val
                    break
    return total, 0


def colShare(board, val, apply):
    total = 0
    for tile in board:
        if tile[0] == apply:
            for tile2 in board:
                if tile2[1][1] == tile[1][1] and tile2[1][0] != tile[1][0] and tile2[0] == apply:
                    total += val
                    break
    return total, 0


def diagShare(board, val, apply):
    total = 0
    for tile in board:
        if tile[0] == apply:
            for tile2 in board:
                if tile[1][0] + tile[1][1] == tile2[1][0] + tile2[1][1] or math.fabs(tile[1][0] - tile[1][1]) == math.fabs(tile2[1][0] - tile2[1][1]):
                    total += val
                    break
    return total, 0




# format will be: [[method, (valueRange inclusive)]]
stubGeneration = [
    [countChar, (1, 2)],
    [countAdj, (1, 2)],
    [minusAdj, (1, 2)],
    [countChar2, (0.1, 0.3)],
    [rowShare, (1, 3)],
    [colShare, (1, 3)],
    [diagShare, (1, 3)]
]



