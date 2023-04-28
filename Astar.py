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
                return path, lenPath, len(closed)+len(frontier), len(frontier), maxDepth
            closed.add(value)
            for neighbor in root.graf.getNeighborhood(value):
                if neighbor not in closed:
                    f = neighbor.depth + h(neighbor)
                    heapq.heappush(frontier, (f, neighbor))
    return -1, None, len(closed)+len(frontier), len(frontier), maxDepth