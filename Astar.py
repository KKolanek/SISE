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
            # print(priority)
            if value.isGoal():
                path = value.find_path()
                maxDepth = max(value.depth, maxDepth)
                return path, len(closed), len(frontier), maxDepth
            closed.add(value)
            # print(value.state.puzzle)
            for neighborhood in root.state.getNeighborhood(value):
                if neighborhood not in closed:
                    f = neighborhood.depth + h(neighborhood)
                    heapq.heappush(frontier, (f, neighborhood))
                    # print(f)
                    # print(neighborhood.state.puzzle)
    return -1, len(closed), len(frontier), maxDepth