def EdgeCounter(graph):
    counter = 0
    for i in range(1,n):
        for j in range(i):
            if graph[i][j] == 1:
                counter += 1
    return counter

n = int(input())
graph = [[int(j) for j in input().split()] for i in range(n)]
print(EdgeCounter(graph))