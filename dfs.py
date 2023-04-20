def dfs(root):
    depth = 20
    maxDepth = 0
    frontier = list()
    closed = set()
    frontier.append(root)
    if root.isGoal():
        path, lenPath = root.find_path()
        return path, lenPath, len(closed), len(frontier), maxDepth
    while len(frontier) != 0:
        value = frontier.pop()
        if value.depth <= depth:
            maxDepth = max(value.depth, maxDepth)
            if value not in closed:
                closed.add(value)
                for neighborhood in root.state.getNeighborhood(value):
                    if value.isGoal():
                        path, lenPath = value.find_path()
                        return path, lenPath, len(closed), len(frontier), maxDepth
                    if neighborhood not in closed:
                        frontier.append(neighborhood)

    return -1, len(closed), len(frontier), maxDepth