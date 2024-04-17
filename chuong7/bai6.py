from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def themCanh(self, u, v):
        self.graph[u].append(v)

    def SoCungVao(self, v):
        count = 0
        for node in self.graph:
            for neighbor in self.graph[node]:
                if neighbor == v:
                    count += 1
        return count

# Ví dụ
dt = Graph()
dt.themCanh(0, 1)
dt.themCanh(1, 2)
dt.themCanh(2, 3)
dt.themCanh(3, 0)
print(dt.SoCungVao(0))  # Output: 1 (chỉ có cung (3, 0) đi vào đỉnh 0)
