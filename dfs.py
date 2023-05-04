def dfs(root):
    depth = 20
    maxDepth = 0
    frontier = []
    closed = set()
    frontier.append(root)
    if root.isGoal():
        path, lenPath = root.find_path()
        return path, lenPath, len(closed)+len(frontier), len(closed), maxDepth
    while len(frontier) != 0:
        value = frontier.pop()
        closed.add(value)
        queue = value.getNeighborhood()
        for neighbor in reversed(queue):
            if neighbor.depth <= depth:
                maxDepth = max(neighbor.depth, maxDepth)
                if neighbor not in closed:
                    if neighbor.isGoal():
                        path, lenPath = neighbor.find_path()
                        return path, lenPath, len(closed) + len(frontier), len(closed), maxDepth
                    frontier.append(neighbor)
                    closed.add(neighbor)
    return -1, None, len(closed)+len(frontier), len(closed), maxDepth
