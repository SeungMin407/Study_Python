from collections import deque
graph={
    1:[2,3,4],
    2:[1,5],
    3:[1,6],
    4:[1,6],
    5:[2,6],
    6:[3,4,5]
}

def DFS(graph, node, visited=None):
    if visited is None:
        visited = []
    if node not in visited :
        visited.append(node)
        for n in graph[node] :
            DFS(graph,n,visited)
    return visited
print(DFS(graph,1))

def DFS_n(graph,start) :
    visited=[]
    stack=[start]
    while stack:
        node=stack.pop()
        if node not in visited :
            visited.append(node)
            stack.extend(graph[node][::-1])
    return visited
print(DFS_n(graph,1))

def BFS(graph,start) :
    visited=[start]
    q=deque()
    q.append(start)
    while q :
        node=q.popleft()
        for n in graph[node] :
            if n not in visited:
                visited.append(n)
                q.append(n)
    return visited
print(BFS(graph,1))

