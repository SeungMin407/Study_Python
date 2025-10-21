import copy
from collections import deque
ice_map=[[0,0,1,1,0],
     [0,0,0,1,1],
     [1,1,1,1,1],
     [0,0,0,0,0]]
def BFS(ice,result=0) :
    freezed = copy.deepcopy(ice)
    n, m = len(ice), len(ice[0]) #세로/가로
    dx = [0, 1, 0, -1] 
    dy = [-1, 0, 1, 0] 
    q=deque()
    flag=False
    for i in range(n) : #시작점 정하기
        for j in range(m) :
            if freezed[i][j]==0:
                flag=True
                q.append((i,j))
                freezed[i][j]=1
                result+=1 #시작점 있으면 결과 1 추가
                break
        if flag : break
    while q:
        y,x = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= ny < n and 0 <= nx < m and freezed[ny][nx] == 0:
                q.append((ny, nx))
                freezed[ny][nx] = 1
    if 0 in [j for i in freezed for j in i]: #0이 남아있으면 재귀 호출
        result=BFS(freezed, result)
    return result
print(BFS(ice_map))
