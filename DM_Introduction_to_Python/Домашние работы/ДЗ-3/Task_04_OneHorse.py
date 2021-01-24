def AddDependencies(x, y):
    # влево вниз
    if x - 2 > 0 and y - 1 > 0 and not visited[x-2][y-1]:
        Q.enqueue((x - 2, y - 1))
        visited[x - 2][y - 1] = visited[x][y] + 1
    # влево вверх
    if x - 2 > 0 and y + 1 <= N and not visited[x-2][y+1]:
        Q.enqueue((x - 2, y + 1))
        visited[x-2][y+1] = visited[x][y] + 1
    # вниз влево
    if x - 1 > 0 and y - 2 > 0 and not visited[x-1][y-2]:
        Q.enqueue((x - 1, y - 2))
        visited[x-1][y-2] = visited[x][y] + 1
    # вниз вправо
    if x + 1 <= N and y - 2 > 0 and not visited[x+1][y-2]:
        Q.enqueue((x + 1, y - 2))
        visited[x+1][y-2] = visited[x][y] + 1
    # вправо вниз
    if x + 2 <= N and y - 1 > 0 and not visited[x+2][y-1]:
        Q.enqueue((x + 2, y - 1))
        visited[x+2][y-1] = visited[x][y] + 1
    # вправо вверх
    if x + 2 <= N and y + 1 <= N and not visited[x+2][y+1]:
        Q.enqueue((x + 2, y + 1))
        visited[x+2][y+1] = visited[x][y] + 1
    # вверх вправо
    if x + 1 <= N and y + 2 <= N and not visited[x+1][y+2]:
        Q.enqueue((x + 1, y + 2))
        visited[x+1][y+2] = visited[x][y] + 1
    # вверх и влево
    if x - 1 > 0 and y + 2 <= N and not visited[x-1][y+2]:
        Q.enqueue((x - 1, y + 2))
        visited[x-1][y+2] = visited[x][y] + 1


class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.insert(0, item)

    def dequeue(self):
        return self.queue.pop()

    def size(self):
        return len(self.queue)

    def isEmpty(self):
        return self.queue == []


# N - количество клеток на шахматной доске
N = int(input())
# получение конечной и начальных позиций
startP = tuple(map(int, input().split()))
endP = tuple(map(int, input().split()))

visited = [[0 for _ in range(N+1)] for __ in range(N+1)]

Q = Queue()
Q.enqueue(startP)

while not Q.isEmpty():
    m = Q.dequeue()
    AddDependencies(m[0], m[1])

print(visited[endP[0]][endP[1]])
