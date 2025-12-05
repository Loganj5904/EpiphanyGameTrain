import character
import math

# board will have elements of the following format: [char, [x, y]]
# game will have elements of the following format: [currentPlayer, turnsLeft, chars, [board1, board2,...,boardn]]


def createGame(playerCount, turnCount=5, stubCount=1, charString='abcdefghijklmnopqrstuvwxyz'):
    game = []
    boards = []
    for i in range(playerCount):
        boards.append([])
    characters = []
    for char in list(charString):
        newChar = character.Character(char)
        newChar.getRandomStubs(stubCount)
        characters.append(newChar)

    currentPlayer = 0          # tracks which player places next
    turnsLeft = turnCount      # tracks how many turns remain
    game = [currentPlayer, turnsLeft, characters, boards]
    return game

def generateCharacters(stubCount=1, charString='abcdefghijklmnopqrstuvwxyz'):
    characters = []
    for char in list(charString):
        newChar = character.Character(char)
        newChar.getRandomStubs(stubCount)
        characters.append(newChar)
    return characters


def place(game, char, position):
    try:
        if game[1] == 0:        # check if there are turns left
            print("out of turns")
        elif checkValidMove(position, game[3][game[0]]):    # game[3][game[0]] check the board of the current player
            game[3][game[0]].append([char, position])
            game[0] += 1
            if game[0] > len(game[3]) - 1:
                game[0] = 0
                game[1] -= 1
        else:
            print("Invalid move, place all tiles adjacent to another tile")
    except:
        print("Not a valid move, try again")
    return game


def simulate(game, char, position):     # use this in the simulation of the game, or just to play the game without considering a second player
    try:
        if game[1] == 0:        # check if there are turns left
            print("out of turns")
        elif checkValidMove(position, game[3][game[0]]):    # game[3][game[0]] check the board of the current player
            game[3][game[0]].append([char, position])
            game[1] -= 1

        else:
            print("Invalid move, place all tiles adjacent to another tile")
    except:
        print("Not a valid move, try again")
    return game


# checks if the position of the tile placed is adjacent to another tile, if needed
def checkValidMove(position, board):
    if len(board) == 0:
        return True
    for tile in board:
        if math.fabs(tile[1][0] - position[0]) + math.fabs(tile[1][1] - position[1]) == 1:
            return True
    return False


def calculateTotalPoints(board, characters):
    total = 0
    for char in characters:
        total += char.calculatePoints(board)[0]
    return total


def getSymbolList(characters):
    charList = []
    for c in characters:
        charList.append(c.symbol)
    return charList


def getActionLocations(targetState):
    availableLocations = []
    for tile in targetState:
        primedLocations = []
        if not availableLocations.__contains__([tile[1][0] + 1, tile[1][1]]):
            primedLocations.append([tile[1][0] + 1, tile[1][1]])
        if not availableLocations.__contains__([tile[1][0] - 1, tile[1][1]]):
            primedLocations.append([tile[1][0] - 1, tile[1][1]])
        if not availableLocations.__contains__([tile[1][0], tile[1][1] + 1]):
            primedLocations.append([tile[1][0], tile[1][1] + 1])
        if not availableLocations.__contains__([tile[1][0], tile[1][1] - 1]):
            primedLocations.append([tile[1][0], tile[1][1] - 1])
        for t in targetState:
            if primedLocations.__contains__(t[1]):
                primedLocations.remove(t[1])
        for p in primedLocations:
            if not availableLocations.__contains__(p):
                availableLocations.append(p)
    if len(availableLocations) == 0:
        availableLocations.append([5, 5])
    return availableLocations


def getActions(locations, characters):
    actions = []
    for l in locations:
        for c in characters:
            if type(c) == character.Character:
                actions.append([c.symbol, l])
            else:
                actions.append([c, l])
    return actions



def displayBoard(board):
    lowx=999
    highx=-999
    lowy=999
    highy=-999
    printBoard = ""
    if len(board) == 0:
        print('-')
    else:
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

