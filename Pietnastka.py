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
        R = index0 % self.sizeW
        L = index0 % self.sizeW
        D = index0 + self.sizeW
        U = index0 - self.sizeW
        if course == "R":
            if R < (self.sizeW - 1):
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
        if actions == ['m', 'a', 'n', 'h'] or actions == ['h', 'a', 'm', 'm']:
            actions = ['R', 'L', 'U', 'D']
        neighborhood = []
        for action in actions:
            neighborhoodState = value.state.move(action)
            temp = value.depth
            if neighborhoodState.puzzle == value.state.puzzle:
                action = None
            neighborhoodNode = State(neighborhoodState, value, action, temp + 1)
            neighborhood.append(neighborhoodNode)
        return neighborhood


class State:
    def __init__(self, state, parent, action, depth):
        self.state = state
        self.parent = parent
        self.action = action
        self.depth = depth

    def __len__(self):
        return len(self.state.puzzle)

    def __lt__(self, other):
        return self.depth < other.depth

    def __eq__(self, other):
        if isinstance(other, State):
            return self.state == other.state
        return False

    def __hash__(self):
        return hash(tuple(self.state))

    def __getitem__(self, index):
        row, col = divmod(index, self.state.sizeK)
        return self.state.puzzle[row * self.state.sizeW + col]

    def find_path(self):
        path = []
        node = self
        while node is not None:
            if node.action is not None:
                path.append(node.action)
            node = node.parent
        path.reverse()
        return path

    def goal(self):
        lists = self.state.puzzle[:]
        lists.sort()
        lists.remove(0)
        lists.append(0)
        return lists

    def isGoal(self):
        return self.state.puzzle == self.goal()


def hamming(state):
    count = 0
    for i in range(len(state.state.puzzle)):
        if state.state.puzzle[i] != state.goal()[i]:
            count += 1
    return count


def manhattan(state):
    total_distance = 0
    for i in range(len(state.state.puzzle)):
        current_row = i // state.state.sizeW
        current_col = i % state.state.sizeK
        goal_row = (state.state.puzzle[i] - 1) // state.state.sizeW
        goal_col = (state.state.puzzle[i] - 1) % state.state.sizeK
        distance = abs(current_row - goal_row) + abs(current_col - goal_col)
        total_distance += distance
    return total_distance


def h(state):
    val = 0
    heuristic = sys.argv[2]
    if heuristic == "manh":
        val = manhattan(state)
    elif heuristic == "hamm":
        val = hamming(state)
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


def save(dane, name, *solve):
    f = open(name, mode='w')
    if dane != -1:
        f.write(str(dane.__len__()) + "\n")
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
    path, visited, closed, depth = 0, 0, 0, 0
    root = State(Graf(graf), None, None, 0)
    if sys.argv[1] == "bfs":
        path, visited, closed, depth = bfs.bfs(root)
    elif sys.argv[1] == "dfs":
        path, visited, closed, depth = dfs.dfs(root)
    elif sys.argv[1] == "astr":
        path, visited, closed, depth = Astar.astr(root)
    save(path, "Solve/" + sys.argv[4])
    save(path, "Stats/" + sys.argv[5], visited, closed, depth, round(time.process_time(), 3))
    print(str(path), visited, closed, depth, round(time.process_time()*1000, 3))


if __name__ == "__main__": main()
