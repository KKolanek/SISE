def dfs(root):
    depth = 20
    maxDepth = 0
    frontier = list()
    closed = set()
    frontier.append(root)
    if root.isGoal():
        path, lenPath = root.find_path()
        return path, lenPath, len(closed)+len(closed), len(frontier), maxDepth
    while len(frontier) != 0:
        value = frontier.pop()
        closed.add(value)
        if value.depth < depth:
            maxDepth = max(value.depth, maxDepth)
            queue = root.state.getNeighborhood(value)
            for neighborhood in reversed(queue):
                if neighborhood not in closed and neighborhood not in frontier:
                    if value.isGoal():
                        path, lenPath = value.find_path()
                        return path, lenPath, len(closed) + len(closed), len(frontier), maxDepth
                    frontier.append(neighborhood)
    return -1, None, len(closed)+len(closed), len(frontier), maxDepth