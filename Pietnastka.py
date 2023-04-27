import sys
import Astar
import bfs
import dfs
import time

class Graf:

    def __init__(self, puzzle):
        graf, w, k = load(sys.argv[3])
        self.sizeW = w
        self.sizeK = k
        self.puzzle = puzzle

    def __iter__(self):
        return iter(self.puzzle)

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
        return Graf(newPuzzle)


    @staticmethod
    def getNeighborhood(value):
        actions = [*sys.argv[2]]
        if actions == ['m', 'a', 'n', 'h'] or actions == ['h', 'a', 'm', 'm']:
            actions = ['R', 'L', 'U', 'D']
        neighborhood = []
        for action in actions:
            neighborhoodState = value.state.move(action)
            temp = value.depth
            neighborhoodNode = State(neighborhoodState, value, action, temp + 1)
            if neighborhoodState is not None:
                neighborhood.append(neighborhoodNode)
        return neighborhood


class State:
    def __init__(self, state, parent, action, depth):
        self.state = state
        self.parent = parent
        self.action = action
        self.depth = depth

    def __lt__(self, other):
        return self.depth < other.depth

    def __eq__(self, other):
        if isinstance(other, State):
            return self.state.puzzle == other.state.puzzle
        return False

    def __hash__(self):
        return hash(tuple(self.state.puzzle))

    def __str__(self):
        return str(self.state.puzzle)

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
        lists = self.state.puzzle[:]
        lists.sort()
        lists.remove(0)
        lists.append(0)
        return lists

    def isGoal(self):
        return self.state.puzzle == self.goal()


def hamming(value):
    count = 0
    for i in range(len(value.state.puzzle)):
        if value.state.puzzle[i] != value.goal()[i]:
            count += 1
    return count


def manhattan(value):
    total_distance = 0
    for i in range(len(value.state.puzzle)):
        current_row = i // value.state.sizeW
        current_col = i % value.state.sizeK
        goal_row = (value.state.puzzle[i] - 1) // value.state.sizeW
        goal_col = (value.state.puzzle[i] - 1) % value.state.sizeK
        distance = abs(current_row - goal_row) + abs(current_col - goal_col)
        total_distance += distance
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
    with open("4x4/" + name, "r") as f:
        lines = f.read().splitlines()
    size = lines[0]
    graf = []
    for i in lines[1:len(lines)]:
        graf += i.split(" ")
    graf = [int(i) for i in graf]
    return graf, int(size[0]), int(size[2])


def save(dane, lenP, name, *solve):
    f = open(name, mode='w')
    if dane != -1:
        f.write(str(lenP) + "\n")
    elif dane == -1 and solve:
        f.write("-1\n")
    if solve:
        f.write(str(solve[0]))
        f.write("\n" + str(solve[1]))
        f.write("\n" + str(solve[2]))
        f.write("\n" + str(solve[3]))
    else:
        f.write(str(dane))
    f.close()


def main():
    graf, w, k = load(sys.argv[3])
    path, lenPath, visited, closed, depth = 0, 0, 0, 0, 0
    root = State(Graf(graf), None, None, 0)
    if sys.argv[1] == "bfs":
        path, lenPath, visited, closed, depth = bfs.bfs(root)
    elif sys.argv[1] == "dfs":
        path, lenPath, visited, closed, depth = dfs.dfs(root)
    elif sys.argv[1] == "astr":
        path, lenPath, visited, closed, depth = Astar.astr(root)
    save(path, lenPath, "Solve/" + sys.argv[4])
    save(path, lenPath, "Stats/" + sys.argv[5], visited, closed, depth, round(time.process_time(), 3))
    print(str(path), visited, closed, depth, round(time.process_time(), 3))


if __name__ == "__main__": main()
