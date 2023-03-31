from collections import deque

def bfs(root, actions):
    queue = deque([root])
    visited = set()
    if root.isGoal():
        path = root.find_path()
        return path, len(visited), len(queue)
    while len(queue) != 0:
        value = queue.popleft()
        for neighborhood in root.state.getNeighborhood(value, actions):
            # print(value.state.puzzle)
            if value.isGoal():
                path = value.find_path()
                return path, len(visited), len(queue)
            if neighborhood not in visited:
                queue.append(neighborhood)
                visited.add(neighborhood)
    return -1