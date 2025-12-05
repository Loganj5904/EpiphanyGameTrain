import gameThin
import copy

MAX = 100000000
MIN = -100000000


class ABPrune:
    def __init__(self, turnCount, characters):
        self.turnCount = turnCount
        self.characters = characters

    def minimax(self, depth, index, boards, maxPlayer, alpha, beta):
        if depth <= 5:
            print(depth)
        if depth == self.turnCount * 2:
            return boards
        if maxPlayer:
            best = MIN
            possibleActions = gameThin.getActions(gameThin.getActionLocations(boards[0]), self.characters)
            bestBoards = copy.deepcopy(boards)

            for i in range(len(possibleActions)):
                newBoards = boards[:]
                newBoards[0] = boards[0][:]
                # MAX
                newBoards[0].append(possibleActions[i])
                newBoards = self.minimax(depth + 1, index * 2 + i, newBoards, False, alpha, beta)
                value = gameThin.calculateTotalPoints(newBoards[0], self.characters) - gameThin.calculateTotalPoints(newBoards[1], self.characters)
                if value > best:
                    best = value
                    bestBoards = copy.deepcopy(newBoards)
                alpha = max(alpha, best)
                if beta <= alpha:
                    break
            return bestBoards
        else:
            best = MAX
            possibleActions = gameThin.getActions(gameThin.getActionLocations(boards[1]), self.characters)
            bestBoards = copy.deepcopy(boards)

            for i in range(len(possibleActions)):
                newBoards = boards[:]
                newBoards[1] = boards[1][:]
                # MIN
                newBoards[1].append(possibleActions[i])
                newBoards = self.minimax(depth + 1, index * 2 + i, newBoards[:], True, alpha, beta)
                value = gameThin.calculateTotalPoints(newBoards[0], self.characters) - gameThin.calculateTotalPoints(newBoards[1], self.characters)
                if value < best:
                    best = value
                    bestBoards = copy.deepcopy(newBoards)
                beta = min(beta, best)

                if beta <= alpha:
                    break
            return bestBoards
