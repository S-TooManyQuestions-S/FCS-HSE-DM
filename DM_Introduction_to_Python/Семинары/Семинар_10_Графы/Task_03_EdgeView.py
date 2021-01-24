def EdgesByMatrix(graph):
    for i in range(n):
        for j in range(i+1,n):
            if graph[i][j] == 1:
                print(i + 1, j + 1)

n = int(input())
graph = [[int(j) for j in input().split()] for i in range(n)]
EdgesByMatrix(graph)