from collections import deque

def bfs(root):
    maxDepth = 0
    frontier = deque([root])
    closed = set()
    if root.isGoal():
        path, lenPath = root.find_path()
        return path, lenPath, len(closed)+len(frontier), len(closed), maxDepth
    while len(frontier) != 0:
        value = frontier.popleft()
        closed.add(value)
        for neighbor in value.getNeighborhood():
            maxDepth = max(neighbor.depth, maxDepth)
            if neighbor.isGoal():
                path, lenPath = neighbor.find_path()
                return path, lenPath, len(closed)+len(frontier), len(closed), maxDepth
            if neighbor not in closed:
                frontier.append(neighbor)
                closed.add(neighbor)
    return -1, None, len(closed)+len(frontier), len(closed), maxDepth