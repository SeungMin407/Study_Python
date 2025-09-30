from collections import deque
graph={
    "A":["B","C","D"],
    "B":["A","E"],
    "C":["A","F","G"],
    "D":["A","H"],
    "E":["B","I"],
    "F":["C","J"],
    "G":["C"],
    "H":["D"],
    "I":["E"],
    "J":["F"]
}

def DFS(node, graph, visited=None):
    if visited is None:
        visited = []
    if node not in visited:
        visited.append(node)
        for neighbor in graph[node]:
            DFS(neighbor, graph, visited)
    return visited
def dfs(start,graph):
    visited=[]
    q=deque()
    q.append(start)
    while q:
        node=q.pop()
        if node not in visited:
            visited.append(node)
            q.extend(graph[node][::-1])
    return visited
print(DFS("A",graph))