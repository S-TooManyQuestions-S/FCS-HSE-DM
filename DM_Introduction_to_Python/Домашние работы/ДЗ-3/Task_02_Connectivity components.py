import sys


def CountOfCC(N):
    # изначально ни одна вершина не является посещенной
    visited = [False] * (N + 1)
    components = list()
    # количество компонент связности (точки входящие в компоненту сами компонентой не являются)
    NComp = 0
    for i in range(1, N + 1):
        if not visited[i]:
            components.append([i])
            NComp += 1
            DFS(i, visited, components[len(components)-1])
    return NComp, components


# обход в глубину для подсчета компонент связности
def DFS(start, visited, currComp):
    # помечаем данную вершину как пройденную
    visited[start] = True
    # пробегаемся по связанным с ней вершинам
    for v in graph[start]:
        # если вершина не была посещена - рекурсивно запускаем функцию
        if not visited[v]:
            currComp.append(v)
            DFS(v, visited, currComp)


sys.setrecursionlimit(100000)
# открываем файл с входными данными
inpStream = open("input.txt", 'r')
# N - количество вершин
# M - количество ребер
N, M = list(map(int, inpStream.readline().split()))
graph = [list() for i in range(N+1)]
# необходимо найти: все связные подграфы данного графа (компоненты связности) и вывести их количество
for m in range(M):
    i, j = list(map(int, inpStream.readline().split()))
    graph[i].append(j)
    graph[j].append(i)

NComp, components = CountOfCC(N)
print(NComp)
for i in components:
    print(len(i))
    print(*sorted(i))



