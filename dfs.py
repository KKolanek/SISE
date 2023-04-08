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
        if value.depth < depth:
            for neighborhood in reversed(root.state.getNeighborhood(value)):
                depthM = neighborhood.depth
                # print(neighborhood.state.puzzle)
                if neighborhood not in closed and neighborhood not in frontier:
                    if neighborhood.isGoal():
                        path = neighborhood.find_path()
                        maxDepth = max(neighborhood.depth, depthM)
                        return path, len(closed), len(frontier), maxDepth
                    frontier.append(neighborhood)
            del neighborhood
    return -1, len(closed), len(frontier), maxDepth