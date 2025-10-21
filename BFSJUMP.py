from collections import deque
def solution(col, row, hole):
    graph = [[0] * col for _ in range(row)]
    for c, r in hole:   
        graph[abs(r-row)][c-1] = -1   # 함정 표시  
    visited = [[[0] * 2 for _ in range(col)] for _ in range(row)]
    visited[row-1][0][1] = True
    q = deque()
    q.append((row-1, 0, 1))
    dx = [-1, 1, 0, 0]
    dy = [0, 0, 1, -1]
    
    answer = 0

    while q:

        for _ in range(len(q)):
            x, y, flag = q.popleft()

            if x == 0 and y == col-1:
                return answer

            for i in range(4):
                nx,ny = x + dx[i],y+dy[i]

                if 0 <= nx < row and 0 <= ny < col and not graph[nx][ny] and not visited[nx][ny][flag]:
                    visited[nx][ny][flag] = True
                    q.append((nx, ny, flag))
                
                if flag:
                    nx += dx[i]
                    ny += dy[i]
                    if 0 <= nx < row and 0 <= ny < col and not graph[nx][ny] and not visited[nx][ny][0]:
                        visited[nx][ny][0] = True
                        q.append((nx, ny, 0))
        answer += 1
    return -1