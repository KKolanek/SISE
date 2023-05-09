import os
import sys
import Astar
import bfs
import dfs
import time

class State:

    def __init__(self, puzzle, parent, action, depth):
        self.parent = parent
        self.action = action
        self.depth = depth
        graf, w, k = load(sys.argv[3])
        self.sizeW = w
        self.sizeK = k
        self.puzzle = puzzle

    def __iter__(self):
        return iter(self.puzzle)

    def __lt__(self, other):
        return self.depth < other.depth

    def __eq__(self, other):
        if isinstance(other, State):
            return tuple(self.puzzle) == tuple(other.puzzle)
        return False

    def __hash__(self):
        return hash(tuple(self.puzzle))

    def find_path(self):
        path = []
        node = self
        while node is not None and node.action is not None:
            path.append(node.action)
            node = node.parent
        path.reverse()
        lenPath = len(path)
        path = "".join(path)
        path = path[0:lenPath]
        return path, lenPath

    def goal(self):
        lists = self.puzzle[:]
        lists.sort()
        lists.remove(0)
        lists.append(0)
        return lists

    def isGoal(self):
        return self.puzzle == self.goal()

    def move(self, course):
        newPuzzle = self.puzzle[:]
        index0 = newPuzzle.index(0)
        R = index0 % self.sizeK
        L = index0 % self.sizeK
        D = index0 + self.sizeW
        U = index0 - self.sizeW
        if course == "R":
            if R < (self.sizeK - 1):
                newPuzzle[index0 + 1], newPuzzle[index0] = newPuzzle[index0], newPuzzle[index0 + 1]
            else:
                return None
        if course == "D":
            if D < (self.sizeW * self.sizeK):
                newPuzzle[index0 + self.sizeW], newPuzzle[index0] = newPuzzle[index0], newPuzzle[index0 + self.sizeW]
            else:
                return None
        if course == "L":
            if L > 0:
                newPuzzle[index0 - 1], newPuzzle[index0] = newPuzzle[index0], newPuzzle[index0 - 1]
            else:
                return None
        if course == "U":
            if U >= 0:
                newPuzzle[index0 - self.sizeW], newPuzzle[index0] = newPuzzle[index0], newPuzzle[index0 - self.sizeW]
            else:
                return None
        return newPuzzle

    def getNeighborhood(self):
        actions = [*sys.argv[2]]
        if actions == ['m', 'a', 'n', 'h'] or actions == ['h', 'a', 'm', 'm']:
            actions = ['R', 'L', 'U', 'D']
        neighborhood = []
        for action in actions:
            puzzle = self.move(action)
            temp = self.depth
            neighborhoodNode = State(puzzle, self, action, temp + 1)
            if puzzle is not None:
                neighborhood.append(neighborhoodNode)
        return neighborhood


def hamming(value):
    count = 0
    for i in range(len(value.puzzle)):
        if value.puzzle[i] != 0 and value.puzzle[i] != value.goal()[i]:
            count += 1
    return count


def manhattan(value):
    total_distance = 0
    for i in range(value.sizeW):
        for j in range(value.sizeK):
            tile = value.puzzle[i * value.sizeW + j]
            if tile != 0:
                goal_i = (tile - 1) // value.sizeW
                goal_j = (tile - 1) % value.sizeK
                total_distance += abs(i - goal_i) + abs(j - goal_j)
    return total_distance


def h(value):
    val = 0
    heuristic = sys.argv[2]
    if heuristic == "manh":
        val = manhattan(value)
    elif heuristic == "hamm":
        val = hamming(value)
    return val


def load(name):
    with open(os.path.join("4x4", name), "r") as f:
        size = next(f).strip().split()
        rows, cols = map(int, size)
        graf = [int(x) for line in f for x in line.split()]
    return graf, rows, cols


def save(dane, lenP, name, *solve):
    with open(name, mode='w') as f:
        if dane != -1:
            f.write(f"{lenP}\n")
        elif dane == -1 and solve:
            f.write("-1\n")
        if solve:
            f.write(f"{solve[0]}\n{solve[1]}\n{solve[2]}\n{solve[3]}")
        else:
            f.write(f"{dane}")

def main():
    graf, rows, columns = load(sys.argv[3])
    path, lenPath, visited, closed, depth = 0, 0, 0, 0, 0
    root = State(graf, None, None, 0)
    if sys.argv[1] == "bfs":
        path, lenPath, visited, closed, depth = bfs.bfs(root)
    elif sys.argv[1] == "dfs":
        path, lenPath, visited, closed, depth = dfs.dfs(root)
    elif sys.argv[1] == "astr":
        path, lenPath, visited, closed, depth = Astar.astr(root)
    save(path, lenPath, "Solve/" + sys.argv[4])
    save(path, lenPath, "Stats/" + sys.argv[5], visited, closed, depth, round(time.process_time(), 3))
    print(str(path), lenPath, visited, closed, depth, round(time.process_time(), 3))


if __name__ == "__main__": main()
