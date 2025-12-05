import random
import time

import game
import gameThin
import MCTS
import character
import stub
import abPruning


def main():
    testGame = game.Game(1, turnCount=10, stubCount=2)
    # testActions = [('a', 2, 2), ('b', 2, 3), ('c', 3, 2), ('d', 3, 3), ('e', 3, 4), ('f', 4, 4), ('g', 4, 5), ('h', 5, 5), ('i', 6, 5), ('j', 7, 5), ('k', 8, 5)]
    # for i in range(len(testActions)):
    while testGame.turnsLeft > 0:
        action = input("place a tile: char, x, y: ")
        actions = action.split(", ")
        # actions = testActions[i]
        testGame.place(actions[0], [int(actions[1]), int(actions[2])])
        game.displayBoard(board=testGame.boards[0])
        print(testGame.calculateTotalPoints(0))


def mctsMain():
    charString = 'abcde'
    stubCount = 1
    characters = []
    for char in list(charString):
        newChar = character.Character(char)
        newChar.getRandomStubs(stubCount)
        characters.append(newChar)

    turnCount = 5

    searchTree = MCTS.MCTSearch(MCTS.Node([]), turnCount, characters)
    board = searchTree.run(iterations=500)


def abMain():
    ab = abPruning.ABPrune(5, gameThin.generateCharacters(2, 'abcd'))
    boards = [[], []]
    start = time.time()
    top = ab.minimax(0, 0, boards, True, -100000000, 100000000)
    print(time.time() - start)
    gameThin.displayBoard(top[0])
    print(gameThin.calculateTotalPoints(top[0], ab.characters))
    brek = True



mctsMain()