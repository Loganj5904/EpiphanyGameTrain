import character
import math

# board will have elements of the following format: [char, [x, y]]

class Game():
    def __init__(self, playerCount, turnCount=5, stubCount=1, charString='abcdefghijklmnopqrstuvwxyz'):
        self.boards = []
        for i in range(playerCount):
            self.boards.append([])

        self.stubCount = stubCount
        self.characters = []
        for char in list(charString):
            newChar = character.Character(char)
            newChar.getRandomStubs(self.stubCount)
            self.characters.append(newChar)

        self.currentPlayer = 0          # tracks which player places next
        self.turnsLeft = turnCount      # tracks how many turns remain


    def place(self, char, position):
        try:
            if self.turnsLeft == 0:
                print("out of turns")
            elif self.checkValidMove(position, self.boards[self.currentPlayer]):
                self.boards[self.currentPlayer].append([char, position])
                self.currentPlayer += 1
                if self.currentPlayer > len(self.boards) - 1:
                    self.currentPlayer = 0
                    self.turnsLeft -= 1
            else:
                print("Invalid move, place all tiles adjacent to another tile")
        except:
            print("Not a valid move, try again")


    # checks if the position of the tile placed is adjacent to another tile, if needed
    def checkValidMove(self, position, board):
        if len(board) == 0:
            return True
        for tile in board:
            if math.fabs(tile[1][0] - position[0]) + math.fabs(tile[1][1] - position[1]) == 1:
                return True
        return False


    def calculateTotalPoints(self, player):
        total = 0
        for char in self.characters:
            total += char.calculatePoints(self.boards[player])[0]
        # for i in range(len(self.boards)):
        #     for char in self.characters:
        #         if i != player:
        #             total += char.calculatePoints(self.boards[i])[0]
        #         # else:
        #         #     total -= char.calculatePoints(self.boards[i])[1]
        return total

    def getCharList(self):
        charList = []
        for c in self.characters:
            charList.append(c.symbol)
        return charList


def displayBoard(board):
    lowx=999
    highx=-999
    lowy=999
    highy=-999
    printBoard = ""

    for i in range(len(board)):
        if board[i][1][0] < lowx:
            lowx = board[i][1][0]
        if board[i][1][1] < lowy:
            lowy = board[i][1][1]
        if board[i][1][0] > highx:
            highx = board[i][1][0]
        if board[i][1][1] > highy:
            highy = board[i][1][1]
    width = highx - lowx
    height = highy - lowy
    for i in range((width + 1) * (height + 1)):
        printBoard += "-#"
    printBoard = list(printBoard)
    for i in range(len(board)):
        char = board[i][0]
        pos = (board[i][1][0] + width - highx, board[i][1][1] + height - highy)
        stringPos = (2 * (pos[0] + (pos[1] * (width + 1))))
        printBoard[stringPos] = char
    for i in range(len(printBoard)):
        if i % ((width + 1) * 2) == ((width + 1) * 2) - 1:
            printBoard[i] = "\n"
        if printBoard[i] == "#":
            printBoard[i] = "\t"
    print(''.join(printBoard))

