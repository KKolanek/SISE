import sys
import bfs
import dfs


class Graf:
    def __init__(self, puzzle):
        graf, w, k = load(sys.argv[3])
        self.sizeW = w
        self.sizeK = k
        self.puzzle = puzzle
        self.depth = 0


    def move(self, course):
        newPuzzle = self.puzzle[:]
        index0 = newPuzzle.index(0)
        R = index0 % self.sizeW
        L = index0 % self.sizeW
        D = index0 + self.sizeW
        U = index0 - self.sizeW
        if course == "R":
            if R < (self.sizeW-1):
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
    def getNeighborhood(value):
        actions = [*sys.argv[2]]
        neighborhood = []
        for action in actions:
            neighborhoodState = value.state.move(action)
            temp = value.depth
            neighborhoodNode = State(neighborhoodState, value, action, temp + 1)
            neighborhood.append(neighborhoodNode)
        return neighborhood


class State:
    def __init__(self, state, parent, action, depth):
        self.state = state
        self.parent = parent
        self.action = action
        self.depth = depth

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

def load(name):
    with open("4x4/" + name, "r") as f:
        lines = f.read().splitlines()
    size = lines[0]
    graf = []
    for i in lines[1:len(lines)]:
        graf += i.split(" ")
    graf = [int(i) for i in graf]
    f.close()
    return graf, int(size[0]), int(size[2])

def save(dane, name, *solve):
    f = open(name, mode='w')
    if dane.__len__() == 0:
        f.write("-1")
    else:
        f.write(str(dane.__len__()))
        if solve:
            f.write("\n" + str(solve[0]))
            f.write("\n" + str(solve[1]))
            f.write("\n" + str(solve[2]))
        else:
            f.write("\n" + str(dane))
    f.close()

def main():
    graf, w, k = load(sys.argv[3])
    path, visited, closed, depth = 0, 0, 0, 0
    root = State(Graf(graf), None, None, 0)
    if sys.argv[1] == "bfs":
        path, visited, closed, depth = bfs.bfs(root)
    elif sys.argv[1] == "dfs":
        path, visited, closed, depth = dfs.dfs(root)
    save(path, sys.argv[4])
    save(path, sys.argv[5], visited, closed, depth)
    print(str(path), visited, closed, depth)


if __name__ == "__main__": main()