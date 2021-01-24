def IsOriented(graph):
    for i in range(n):
        if graph[i][i] == 1:
            return False
        for j in range(n):
            if graph[i][j] != graph[j][i]:
                return False
    return True


n = int(input())
graph = [[int(j) for j in input().split()] for i in range(n)]

print("YES" if IsOriented(graph) else "NO")

