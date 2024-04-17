from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def themCanh(self, u, v):
        self.graph[u].append(v)

    def SoCungRa(self, v):
        return len(self.graph[v])

# Ví dụ
dt = Graph()
dt.themCanh(0, 1)
dt.themCanh(0, 2)
dt.themCanh(1, 2)
dt.themCanh(2, 3)
print(dt.SoCungRa(2))  # Output: 1 (có một cung đi ra từ đỉnh 2)
