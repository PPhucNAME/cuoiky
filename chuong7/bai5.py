from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def themCanh(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def BacDinh(self, v):
        return len(self.graph[v])

# Ví dụ
dt = Graph()
dt.themCanh(0, 1)
dt.themCanh(1, 2)
dt.themCanh(2, 3)
print(dt.BacDinh(1))  # Output: 2 (đỉnh 1 có 2 cạnh nối)
