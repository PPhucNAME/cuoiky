from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def themCanh(self, u, v):
        self.graph[u].append(v)

    def DuongDi(self, v1, v2):
        # Khởi tạo tất cả các đỉnh là chưa được duyệt
        visited = set()

        # Sử dụng BFS để tìm đường đi từ v1 đến v2
        queue = [v1]
        while queue:
            node = queue.pop(0)
            if node == v2:
                return True
            if node not in visited:
                visited.add(node)
                queue.extend(self.graph[node])

        return False

# Ví dụ
dt = Graph()
dt.themCanh(0, 1)
dt.themCanh(0, 2)
dt.themCanh(1, 2)
dt.themCanh(2, 3)
print(dt.DuongDi(0, 3))  # Output: True
print(dt.DuongDi(1, 3))  # Output: True
print(dt.DuongDi(0, 4))  # Output: False
