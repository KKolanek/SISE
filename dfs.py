def dfs(root):
    depth = 20
    maxDepth = 0
    frontier = []
    closed = set()
    frontier.append(root)
    if root.isGoal():
        path, lenPath = root.find_path()
        return path, lenPath, len(closed)+len(frontier), len(frontier), maxDepth
    while len(frontier) != 0:
        value = frontier.pop()
        closed.add(value)
        # if value.depth <= depth:
        #     maxDepth = max(value.depth, maxDepth)
        queue = root.state.getNeighborhood(value)
        for neighborhood in reversed(queue):
            if neighborhood.depth <= depth:
                maxDepth = max(neighborhood.depth, maxDepth)
                if tuple(neighborhood.state.puzzle) not in closed or neighborhood.state.puzzle not in frontier:
                    if neighborhood.isGoal():
                        path, lenPath = neighborhood.find_path()
                        return path, lenPath, len(closed) + len(frontier), len(frontier), maxDepth
                    frontier.append(neighborhood)
    return -1, None, len(closed)+len(frontier), len(frontier), maxDepth