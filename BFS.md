# 프로그래머스 연습문제 미로탈출

 1 x 1 크기의 칸들로 이루어진 직사각형 격자 형태의 미로에서 탈출하려고 합니다. 각 칸은 통로 또는 벽으로 구성되어 있으며, 벽으로 된 칸은 지나갈 수 없고 통로로 된 칸으로만 이동할 수 있습니다. 통로들 중 한 칸에는 미로를 빠져나가는 문이 있는데, 이 문은 레버를 당겨서만 열 수 있습니다. 레버 또한 통로들 중 한 칸에 있습니다. 따라서, 출발 지점에서 먼저 레버가 있는 칸으로 이동하여 레버를 당긴 후 미로를 빠져나가는 문이 있는 칸으로 이동하면 됩니다. 이때 아직 레버를 당기지 않았더라도 출구가 있는 칸을 지나갈 수 있습니다. 미로에서 한 칸을 이동하는데 1초가 걸린다고 할 때, 최대한 빠르게 미로를 빠져나가는데 걸리는 시간을 구하려 합니다.

미로를 나타낸 문자열 배열 `maps`가 매개변수로 주어질 때, 미로를 탈출하는데 필요한 최소 시간을 return 하는 solution 함수를 완성해주세요. 만약, 탈출할 수 없다면 -1을 return 해주세요.

# **입출력 예** :

![image.png](attachment:d5b150b2-a5d8-45a8-99be-01570c8c4e39:image.png)

maps = ["SOOOL","XXXXO","OOOOO","OXXXX","OOOOE"]

result = 16

## **BFS(Breadth-First Search) 알고리즘**

BFS는 시작 노드에서 가까운 노드부터 차례대로 탐색하는 방법이다.

구체적으로, 시작 노드를 큐에 넣고, 큐에서 노드를 하나 씩 꺼내며 그 노드와 인접한 노드 중 아직 방문하지 않은 노드를 큐에 넣는다.

이 과정을 반복하면 시작 노드로부터의 최단 거리(모든 간선의 가중치가 동일할 때)를 구할 수 있다.

### 동작 과정

![image.png](attachment:09f2c94e-5c45-409d-b08f-401ebe4dfedb:image.png)

다음과 같은 경로가 있을 때, 초기 상태는 큐에 1번 노드가 들어가 있는 상태이다.

![image.png](attachment:bc04c77a-7a8a-4f14-8818-0f976743fed8:image.png)

![image.png](attachment:750c7ba2-2385-4367-9901-8d9fb700d6b4:image.png)

큐에서 1번 노드를 꺼내고 인접한 2, 3번 노드를 넣는다.

![image.png](attachment:574ca5e1-586a-438a-b09f-5bca66152a82:image.png)

2번 노드를 꺼내고 인접한 8번 노드를 넣는다. 큐에서 값을 꺼낼 때, 순차적 탐색을 위해 첫 번째 자료를 꺼내고, 값을 넣을 때는 마지막 인덱스에 넣는다.

![image.png](attachment:4de77492-a2cf-4651-9e25-a12b764675e5:image.png)

3번 노드를 큐에서 꺼내고 4, 5번 노드를 넣는다. 이후 8번 노드를 꺼내고, 6, 7번 노드를 넣는다.

![image.png](attachment:7b8c7eda-6b86-4cd6-894d-116191802e04:image.png)

더 이상 탐색할 노드가 없으므로 큐에서 값을 순차적으로 꺼낸다.

![image.png](attachment:511b4e78-bfda-4884-8787-1285cb213a42:image.png)

큐에 값이 없으면 프로그램은 종료된다.

## **BFS 알고리즘 구현**

```python
from collections import deque

def bfs(start, end, maps):
	# 탐색할 방향
    dy = [0, 1, -1, 0]
    dx = [1, 0, 0, -1]

    n = len(maps)       # 세로
    m = len(maps[0])    # 가로
    visited = [[False]*m for _ in range(n)]
    que = deque()
    flag = False

    # 시작점 찾기
    for i in range(n):
        for j in range(m):
        	# 출발하고자 하는 지점이라면 시작점의 좌표를 기록함
            if maps[i][j] == start:
                que.append((i, j, 0)) #언패킹이 용이한 튜플로 저장
                # 별도의 cost 리스트를 만들지 않고 que에 바로 기록(0)
                visited[i][j] = True
                flag = True; break
                # 시작 지점은 한 개만 존재하기 때문에 찾으면 바로 나옴
        if flag: break

    # BFS 알고리즘 수행 (핵심)
    while que:
        y, x, cost = que.popleft()

        if maps[y][x] == end:
            return cost

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            # maps 범위내에서 벽이 아니라면 지나갈 수 있음
            if 0<= ny <n and 0<= nx <m and maps[ny][nx] !='X' and (not visited[ny][nx]):
                que.append((ny, nx, cost+1))
                visited[ny][nx] = True

    return -1	# 탈출할 수 없다면

def solution(maps):
    path1 = bfs('S', 'L', maps)	# 시작 지점 --> 레버
    path2 = bfs('L', 'E', maps) # 레버 --> 출구

    # 둘다 -1 이 아니라면 탈출할 수 있음
    if path1 != -1 and path2 != -1:
        return path1 + path2

    return -1
```

### 큐(Queue)

큐(Queue)는 자료를 오른쪽(뒤)에서 넣고, 왼쪽(앞)에서 꺼내는 선입선출(FIFO) 구조를 가진다.

파이썬에서 리스트로 큐를 구현할 경우, `pop(0)`을 사용하면 맨 앞 원소를 꺼낸 뒤 나머지 원소들을 앞으로 당기는 과정이 필요하기 때문에 O(n)의 시간 복잡도를 가진다.

이를 효율적으로 처리하기 위해, 양쪽 끝에서 O(1) 시간에 원소를 넣고 뺄 수 있는 `collections.deque`의 `append()`와 `popleft()`를 사용하여 큐를 구현한다.

## **DFS(Depth-First Search) 알고리즘**

![image.png](attachment:fef83230-486e-4a71-bc43-d51698ccd2b0:image.png)

DFS는 시작 정점에서 출발하여 인접한 정점들을 재귀적(혹은 스택 이용)으로 방문하며, 이미 방문한 정점은 다시 방문하지 않고, 각 분기(branch)마다 가능한 가장 깊은 정점(멀리 있는 노드)까지 탐색한 뒤, 더 이상 갈 곳이 없으면 되돌아가(backtracking) 다른 경로를 탐색하는 알고리즘이다.

DFS 알고리즘 구현

```python
def dfs(y, x, ey, ex, maps, visited, cost, min_cost):
    # 출구 좌표에 도달하면 최솟값 갱신
    if (y, x) == (ey, ex):
        return min(min_cost, cost)

    dy = [0, 1, -1, 0]
    dx = [1, 0, 0, -1]
    n, m = len(maps), len(maps[0])

    for i in range(4):
        ny, nx = y + dy[i], x + dx[i]
        if 0 <= ny < n and 0 <= nx < m and maps[ny][nx] != 'X' and not visited[ny][nx]:
            visited[ny][nx] = True
            min_cost = dfs(ny, nx, ey, ex, maps, visited, cost + 1, min_cost) #재귀 호출
            visited[ny][nx] = False  # 백트래킹
												# for문의 순서에 의해 방문처리를 꺼도 노드를 재방문하지 않음		
    return min_cost

def find_path(start, end, maps):
    n, m = len(maps), len(maps[0])
    visited = [[False]*m for _ in range(n)]
    sy, sx = start
    ey, ex = end

    visited[sy][sx] = True
    min_cost = dfs(sy, sx, ey, ex, maps, visited, 0, float('inf'))
		#숫자 비교연산을 위해 최소 거리 초깃 값은 float('inf')로 설정
    return min_cost if min_cost != float('inf') else -1

def solution(maps):
    n, m = len(maps), len(maps[0])
    start = lever = end = None

    # 좌표 찾기
    for i in range(n):
        for j in range(m):
            if maps[i][j] == 'S':
                start = (i, j)
            elif maps[i][j] == 'L':
                lever = (i, j)
            elif maps[i][j] == 'E':
                end = (i, j)

    path1 = find_path(start, lever, maps)  # S → L
    path2 = find_path(lever, end, maps)    # L → E

    if path1 != -1 and path2 != -1:
        return path1 + path2
    return -1
```
