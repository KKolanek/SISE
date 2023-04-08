import heapq

from Pietnastka import h

def astr(root):
    maxDepth = 0
    frontier = []
    heapq.heappush(frontier, (0, root))
    closed = set()
    while len(frontier) != 0:
        value = heapq.heappop(frontier)[1]
        if value.isGoal():
            path = value.find_path()
            maxDepth = max(value.depth, maxDepth)
            return path, len(closed), len(frontier), maxDepth
        if value not in closed:
            closed.add(value)
            for neighborhood in value.state.getNeighborhood(value):
                f = neighborhood.depth + h(neighborhood)
                heapq.heappush(frontier, (f, neighborhood))
                print(neighborhood.state.puzzle)
    return -1, len(closed), len(frontier), maxDepth