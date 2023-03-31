import sys
import bfs


class Graf:
    def __init__(self, puzzle):
        graf, w, k = odczyt(sys.argv[3])
        self.sizeW = w
        self.sizeK = k
        self.puzzle = puzzle

    def move(self, course):
        newPuzzle = self.puzzle[:]
        index0 = newPuzzle.index(0)
        R = index0 % self.sizeW
        L = index0 % self.sizeW
        D = index0 + self.sizeK
        U = index0 - self.sizeK
        if course == "R":
            if R < (self.sizeK - 1):
                newPuzzle[index0 + 1], newPuzzle[index0] = newPuzzle[index0], newPuzzle[index0 + 1]
        if course == "D":
            if D < (self.sizeW * self.sizeK):
                newPuzzle[index0 + self.sizeW], newPuzzle[index0] = newPuzzle[index0], newPuzzle[index0 + self.sizeW]
        if course == "L":
            if L > 0:
                newPuzzle[index0 - 1], newPuzzle[index0] = newPuzzle[index0], newPuzzle[index0 - 1]
        if course == "U":
            if U >= 0:
                newPuzzle[index0 - self.sizeW], newPuzzle[index0] = newPuzzle[index0], newPuzzle[index0 - self.sizeW]

        return Graf(newPuzzle)

    @staticmethod
    def getNeighborhood(value, actions):
        neighborhood = []
        for action in actions:
            neighborhoodState = value.state.move(action)
            neighborhoodNode = State(neighborhoodState, value, action)
            neighborhood.append(neighborhoodNode)
        return neighborhood


class State:
    def __init__(self, state, parent, action):
        self.state = state
        self.parent = parent
        self.action = action

    def find_path(self):
        path = []
        node = self
        while node.parent is not None:
            path.append(node.action)
            node = node.parent
        path.reverse()
        return path

    def isGoal(self):
        return self.state.puzzle == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0]

def odczyt(name):
    with open("4x4/" + name, "r") as f:
        lines = f.read().splitlines()
    size = lines[0]
    graf = []
    for i in lines[1:5]:
        graf += i.split(" ")
    graf = [int(i) for i in graf]
    f.close()
    return graf, int(size[0]), int(size[2])

def zapis(dane, name, *solve):
    f = open(name, mode='w')
    if dane.__len__() == 0:
        f.write("-1")
    else:
        f.write(str(dane.__len__()))
        if solve:
            f.write("\n" + str(solve[0]))
            f.write("\n" + str(solve[1]))
        else:
            f.write("\n" + str(dane))
    f.close()

def main():
    graf, w, k = odczyt(sys.argv[3])
    path, visited, queue = 0, 0, 0
    root = State(Graf(graf), None, None)
    actions = [*sys.argv[2]]
    if sys.argv[1] == "bfs":
        path, visited, queue = bfs.bfs(root, actions)
    zapis(path, sys.argv[4])
    zapis(path, sys.argv[5], visited, queue)
    print(str(path), visited, queue)


if __name__ == "__main__": main()