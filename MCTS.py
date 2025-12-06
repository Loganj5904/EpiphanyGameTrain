import math
import random
import gameThin


# Credit to Single-Player Monte-Carlo Tree Search, Maarten P.D. Schadd et al. for format and help with code

class Node():   # a node on the mcts tree
    def __init__(self, state):
        self.state = state
        self.wins = 0
        self.visits = 0
        self.ressq = 0
        self.parent = None
        self.children = []
        self.sputc = 0

    def setWeight(self, weight):
        self.weight = weight

    def addChild(self, child):
        self.children.append(child)
        child.parent = self

    def isEqual(self, node):
        if self.state == node.state:
            return True
        return False

class MCTSearch():
    def __init__(self, node, turnCount, characters):
        self.root = node
        self.turnCount = turnCount
        self.characters = characters

        self.scoreCheck = 7

    # selects next child to be expanded
    def selection(self):
        selectedChild = self.root
        hasChild = False

        if len(selectedChild.children) > 0:
            hasChild = True
        while hasChild:
            selectedChild = self.selectChild(selectedChild)
            if len(selectedChild.children) == 0:
                hasChild = False
        return selectedChild

    # selectes child on specific node
    def selectChild(self, node):
        if len(node.children) == 0:
            return node

        for child in node.children:
            if child.visits <= 0:
                return child

        max = 0
        selectedChild = None
        for child in node.children:
            weight = child.sputc
            if weight > max:
                max = weight
                selectedChild = child
        return selectedChild

    # expands a leaf node for each possible action
    def expansion(self, leaf):
        if self.isTerminal(leaf):
            return False
        elif leaf.visits == 0:
            return leaf
        else:
            if len(leaf.children) == 0:
                children = self.addChildren(leaf)
                for child in children:
                    if child.state == leaf.state:
                        continue
                    leaf.addChild(child)
                child = self.selectChildNode(leaf)

        return child

    # checks if the game is over
    def isTerminal(self, node):
        if len(node.state) == self.turnCount:
            return True
        return False

    # adds new children to a node
    def addChildren(self, node):
        actionOptions = gameThin.getActions(gameThin.getActionLocations(node.state), self.characters)
        children = []

        for action in actionOptions:
            state = node.state.copy()
            state.append(action)
            childNode = Node(state)
            children.append(childNode)
        return children

    # selects a random child node
    def selectChildNode(self, node):
        return node.children[random.randint(0, len(node.children) - 1)]

    # play a game out with random moves to determine a score
    def rollout(self, node):
        currentState = node.state.copy()
        while not len(currentState) == self.turnCount:
            actions = gameThin.getActions(gameThin.getActionLocations(currentState), self.characters)
            currentState.append(random.choice(actions))
        score = gameThin.calculateTotalPoints(currentState, self.characters)
        if score > self.scoreCheck:
            return 1
        return -1

    # backpropagate and update each node on a rolled out path and add a win to each if necessary
    def backpropagation(self, node, result):
        node.wins += result
        node.ressq += result **2
        node.visits += 1
        self.evalUTC(node)
        current = node
        while self.hasParent(current):
            current = current.parent
            current.wins += result
            current.ressq += result ** 2
            current.visits += 1
            self.evalUTC(current)

    # evaluate the UTC function of a node, and store it in the nodes weights
    def evalUTC(self, node):
        c = 1.4
        w = node.wins
        n = node.visits
        sumsq = node.ressq
        if node.parent == None:
            t = node.visits
        else:
            t = node.parent.visits

        UTC = w/n + c * math.sqrt(math.log(t)/n)
        D = 10000
        mod = math.sqrt((sumsq - n * (w/n)**2 + D)/n)
        node.sputc = UTC + mod
        return node.sputc


    # determine if a node has a parent
    def hasParent(self, node):
        if node.parent is None:
            return False
        return True

    # the run of the algorithm,
    def run(self, iterations=500):
        x = None
        y = None
        for i in range(iterations):
            x = self.selection()
            y = self.expansion(x)
            if y:
                result = self.rollout(y)
                self.backpropagation(y, result)
                gameThin.displayBoard(y.state)

            else:
                result = gameThin.calculateTotalPoints(x.state, self.characters)
                self.backpropagation(x, result)
            try:
                print("Iteration " + str(i) + " Result: " + str(gameThin.calculateTotalPoints(y.state, self.characters)))
            except:
                print("Iteration " + str(i) + " No y")

        return x.state
