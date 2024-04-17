from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def themCanh(self, u, v):
        self.graph[u].append(v)

    def ChuaDinh(self, v):
        return v in self.graph

# Ví dụ
dt = Graph()
dt.themCanh(0, 1)
dt.themCanh(1, 2)
dt.themCanh(2, 3)
print(dt.ChuaDinh(2))  # Output: True
print(dt.ChuaDinh(4))  # Output: False

