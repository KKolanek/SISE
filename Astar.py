import heapq

from Pietnastka import h

def astr(root):
    maxDepth = 0
    frontier = []
    heapq.heappush(frontier, (0, root))
    closed = set()
    while len(frontier) != 0:
        priority, value = heapq.heappop(frontier)
        if value not in closed:
            maxDepth = max(value.depth, maxDepth)
            if value.isGoal():
                path, lenPath = value.find_path()
                return path, lenPath, len(closed)+len(closed), len(frontier), maxDepth
            closed.add(value)
            for neighborhood in root.state.getNeighborhood(value):
                if neighborhood not in closed:
                    f = neighborhood.depth + h(neighborhood)
                    heapq.heappush(frontier, (f, neighborhood))
    return -1, None, len(closed)+len(closed), len(frontier), maxDepth