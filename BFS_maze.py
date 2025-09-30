from collections import deque
maze=[[0,0,1,0,1],
      [1,0,1,0,0],
      [0,0,1,1,0],
      [0,1,0,0,0],
      [0,0,0,1,1]
]
def BFS(maze, node, goal):
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    m, n = len(maze), len(maze[0])
    x,y=node
    visited = [[False]*n for _ in range(m)]
    visited[y][x] = True
    q=deque()
    q.append((y,x,0))
    while q:
        y,x,cost=q.popleft()
        if (x, y) == goal:
            return cost
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and maze[ny][nx] != 1 and not visited[ny][nx]:
                visited[ny][nx]=True
                q.append((ny,nx,cost+1))
    return -1

start = (0,0)
goal = (3,1)
result = BFS(maze, start, goal)
print("최소 cost:", result)