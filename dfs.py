
def dfs(root):
    depth = 35
    maxDepth = 0
    frontier = list()
    closed = set()
    frontier.append(root)
    if root.isGoal():
        path = root.find_path()
        return path, len(closed), len(frontier), maxDepth
    while len(frontier) != 0:
        value = frontier.pop()
        closed.add(value)
        for neighborhood in reversed(root.state.getNeighborhood(value)):
            # print(neighborhood.state.puzzle)
            # print(neighborhood.depth)
            if neighborhood.depth <= depth:
                if neighborhood not in closed or neighborhood not in frontier:
                    if neighborhood.isGoal():
                        path = neighborhood.find_path()
                        maxDepth = max(neighborhood.depth, neighborhood.parent.depth)
                        return path, len(closed), len(frontier), maxDepth
                    frontier.append(neighborhood)
    return -1, len(closed), len(frontier), maxDepth