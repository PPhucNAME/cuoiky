from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def themCanh(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def DFS(self, v, visited):
        visited[v] = True
        for i in self.graph[v]:
            if visited[i] == False:
                self.DFS(i, visited)

    def SoThanhPhan(self):
        # Khởi tạo tất cả các đỉnh là chưa được duyệt
        V = len(self.graph)
        visited = [False] * (V)
        count = 0

        # Tính số thành phần liên thông bằng cách thực hiện DFS từ mỗi đỉnh chưa được duyệt
        for i in range(V):
            if len(self.graph[i]) > 0 and visited[i] == False:
                self.DFS(i, visited)
                count += 1

        return count

# Ví dụ
dt = Graph()
dt.themCanh(0, 1)
dt.themCanh(0, 2)
dt.themCanh(1, 2)
dt.themCanh(3, 4)
print(dt.SoThanhPhan())  # Output: 2
