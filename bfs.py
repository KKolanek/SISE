from collections import deque

def bfs(root):
    maxDepth = 0
    frontier = deque([root])
    closed = set()
    if root.isGoal():
        path = root.find_path()
        return path, len(closed), len(frontier), maxDepth
    while len(frontier) != 0:
        value = frontier.popleft()
        for neighborhood in root.state.getNeighborhood(value):
            maxDepth = max(neighborhood.depth, maxDepth)
            if neighborhood.isGoal():
                path = neighborhood.find_path()
                return path, len(closed), len(frontier), maxDepth
            if neighborhood not in closed:
                frontier.append(neighborhood)
                closed.add(neighborhood)
    return -1, len(closed), len(frontier), maxDepth