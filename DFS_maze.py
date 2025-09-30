from collections import deque
maze=[[0,0,1,0,1],
      [1,0,1,0,0],
      [0,0,1,1,0],
      [0,1,0,0,0],
      [0,0,0,1,1]
]
def DFS(maze, node, goal, cost=0, visited=None, min_cost=float('inf')):
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    x, y = node
    m, n = len(maze), len(maze[0])

    if visited is None:
        visited = [[False]*n for _ in range(m)]
    visited[y][x] = True

    if node == goal:
        return min(cost,min_cost)

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and maze[ny][nx] != 1 and not visited[ny][nx]:
            min_cost=DFS(maze, (nx, ny), goal, cost+1, visited, min_cost)

    visited[y][x] = False 
    return min_cost

start = (0,0)
goal = (3,0)
result = DFS(maze, start, goal)
print("최소 cost:", result if result!=float('inf') else -1)