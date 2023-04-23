from collections import deque

def bfs(root):
    maxDepth = 0
    frontier = deque([root])
    closed = set()
    if root.isGoal():
        path, lenPath = root.find_path()
        return path, lenPath, len(closed)+len(closed), len(frontier), maxDepth
    while len(frontier) != 0:
        value = frontier.popleft()
        for neighborhood in root.state.getNeighborhood(value):
            maxDepth = max(neighborhood.depth, maxDepth)
            if neighborhood.isGoal():
                path, lenPath = neighborhood.find_path()
                return path, lenPath, len(closed)+len(closed), len(frontier), maxDepth
            if neighborhood not in closed:
                frontier.append(neighborhood)
                closed.add(neighborhood)
    return -1, None, len(closed)+len(closed), len(frontier), maxDepth