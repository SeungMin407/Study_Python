import copy
ice_map=[[0,0,1,1,0],
     [0,0,0,1,1],
     [1,1,1,1,1],
     [0,0,0,0,0]]
def DFS(ice_map):
    dx=[0,0,1,-1]
    dy=[1,-1,0,0]
    ice=copy.deepcopy(ice_map)
    stack=[]
    result=0
    n,m=len(ice),len(ice[0]) #세로/가로
    for i in range(n):
        for j in range(m):
            if ice[i][j]==0:
                result+=1
                stack.append((i,j))
                ice[i][j]=1
                while stack:
                    y,x=stack.pop()
                    for k in range(4):
                        nx,ny=x+dx[k],y+dy[k]
                        if 0<=nx<m and 0<=ny<n and ice[ny][nx]!=1:
                            ice[ny][nx]=1
                            stack.append((ny,nx))
    return result


print(DFS(ice_map))