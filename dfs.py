def dfs(root):
    depth = 25
    maxDepth = 0
    frontier = list()
    closed = set()
    frontier.append(root)
    if root.isGoal():
        path = root.find_path()
        return path, len(closed), len(frontier), maxDepth
    while len(frontier) != 0:
        value = frontier.pop()
        if value.depth <= depth:
            maxDepth = max(value.depth, maxDepth)
            if value not in closed:
                closed.add(value)
                for neighborhood in root.state.getNeighborhood(value):
                    if value.isGoal():
                        path = value.find_path()
                        return path, len(closed), len(frontier), maxDepth
                    if neighborhood not in closed:
                        frontier.append(neighborhood)

    return -1, len(closed), len(frontier), maxDepth

# private static boolean dfs(String parameter) {
#         State g = StateManager.getGoalState();
#         State s = StateManager.getBeginningState();
#
#         if (s.equals(g)) {
#             resultState = s;
#             return true;
#         }
#
#         Stack<State> S = new Stack<>(); // open states
#         Set<State> T = new HashSet<>(); // closed states
#
#         s.depth = 0;
#         S.push(s);
#         while (!S.isEmpty()) {
#             State v = S.pop();
#
#             if(v.depth > 20)
#                 continue;
#
#             if(v.depth > maxRecursionDepth)
#                 maxRecursionDepth = v.depth;
#
#             if (v.equals(g)) {
#                 resultState = v;
#                 return true;
#             }
#
#             if (!T.contains(v)) {
#                 T.add(v); processedStates++;
#                 State[] neighbours = StateManager.getNeighbours(v);
#                 for (int i = 0; i < 4; i++) {
#                     State n = switch (parameter.charAt(i)) {
#                         case 'L' -> neighbours[0];
#                         case 'R' -> neighbours[1];
#                         case 'U' -> neighbours[2];
#                         case 'D' -> neighbours[3];
#                         default -> null;
#                     };
#
#                     if(n == null)
#                         continue;
#
#                     if (n.equals(g)) {
#                         resultState = n;
#                         return true;
#                     }
#
#                     if (!T.contains(n)) {
#                         n.depth = v.depth + 1;
#                         S.push(n); visitedStates++;
#                     }
#                 }
#             }
#         }
#         return false;
#     }