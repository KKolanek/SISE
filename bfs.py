from collections import deque

class Graf:
    def __init__(self, puzzle):
        self.size = 4
        self.puzzle = puzzle

    def move(self, course):
        newPuzzle = self.puzzle[:]
        index0 = newPuzzle.index(0)
        R = index0 % self.size
        L = index0 % self.size
        D = index0 + self.size
        U = index0 - self.size
        if course == "R":
            if R < (self.size - 1):
                newPuzzle[index0 + 1], newPuzzle[index0] = newPuzzle[index0], newPuzzle[index0 + 1]
        if course == "D":
            if D < (self.size * self.size):
                newPuzzle[index0 + self.size], newPuzzle[index0] = newPuzzle[index0], newPuzzle[index0 + self.size]
        if course == "L":
            if L > 0:
                newPuzzle[index0 - 1], newPuzzle[index0] = newPuzzle[index0], newPuzzle[index0 - 1]
        if course == "U":
            if U >= 0:
                newPuzzle[index0 - self.size], newPuzzle[index0] = newPuzzle[index0], newPuzzle[index0 - self.size]

        return Graf(newPuzzle)


class State:
    def __init__(self, state, parent, action):
        self.state = state
        self.parent = parent
        self.action = action


def getNeighborhood(value):
    actions = ["L", "R", "U", "D"]
    neighborhood = []
    for action in actions:
        neighborhoodState = value.state.move(action)
        neighborhoodNode = State(neighborhoodState, value, action)
        neighborhood.append(neighborhoodNode)
    return neighborhood


def find_path(node):
    path = []
    while node.parent is not None:
        path.append(node.action)
        node = node.parent
    path.reverse()
    return path

def isgoal(state):
    return state == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0]

def bfs(graf):
    root = State(Graf(graf), None, None)
    queue = deque([root])
    visited = set()
    if isgoal(root.state.puzzle):
        path = find_path(root)
        return path, len(visited), len(queue)
    while len(queue) != 0:
        value = queue.popleft()
        for neighborhood in getNeighborhood(value):
            print(value.state.puzzle)
            if isgoal(value.state.puzzle):
                path = find_path(value)
                return path, len(visited), len(queue)
            if neighborhood not in visited:
                queue.append(neighborhood)
                visited.add(neighborhood)
    print(visited)
    return 0

def main():
    graf = [1, 2, 3, 4,
            5, 6, 7, 8,
            10, 13, 11, 12,
            9, 14, 0, 15]
    print(bfs(graf))


if __name__ == "__main__": main()
