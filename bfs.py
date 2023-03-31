from collections import deque

def bfs(root):
    queue = deque([root])
    visited = set()
    if root.isGoal():
        path = root.find_path()
        return path, len(visited), len(queue)
    while len(queue) != 0:
        value = queue.popleft()
        for neighborhood in root.state.getNeighborhood(value):
            # print(value.state.puzzle)
            if neighborhood.isGoal():
                path = neighborhood.find_path()
                return path, len(visited), len(queue)
            if neighborhood not in visited:
                queue.append(neighborhood)
                visited.add(neighborhood)
    return -1