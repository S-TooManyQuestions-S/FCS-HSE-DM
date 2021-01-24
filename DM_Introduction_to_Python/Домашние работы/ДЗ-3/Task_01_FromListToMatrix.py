# n - количество вершин в графе
# m - количество ребер в графе
n, m = list(map(int, input().split()))
graph = [[0 for j in range(n)] for i in range(n)]

# внесение информации о ребрах
for counter in range(m):
    i, j = list(map(int, input().split()))
    graph[i-1][j-1] = graph[j-1][i-1] = 1

# вывод матрицы смежности
for i in range(n):
    print()
    for j in range(n):
        print(graph[i][j], end=" ")


