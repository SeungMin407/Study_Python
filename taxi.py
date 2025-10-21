def solution(n, s, a, b, fares):
    INF = int(1e9)
    graph = [[INF] * n for _ in range(n)]
    for i in range(n): graph[i][i] = 0

    for f in fares:
        x, y, c = f
        graph[x - 1][y - 1] = c
        graph[y - 1][x - 1] = c

    for k in range(n):
        for i in range(n):
            for j in range(n):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
    min_val = graph[s - 1][a - 1] + graph[s - 1][b - 1]

    for i in range(n):
        min_val = min(min_val, graph[s - 1][i] + graph[i][a - 1] + graph[i][b - 1])

    return min_val