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

    def LienThong(self):
        # Khởi tạo tất cả các đỉnh là chưa được duyệt
        V = len(self.graph)
        visited = [False] * (V)

        # Tìm một đỉnh không được duyệt và thực hiện DFS từ đó
        for i in range(V):
            if len(self.graph[i]) > 0:
                self.DFS(i, visited)
                break

        # Nếu có đỉnh nào không được duyệt, đồ thị không liên thông
        for i in range(V):
            if len(self.graph[i]) > 0 and visited[i] == False:
                return False

        # Nếu tất cả các đỉnh đều được duyệt, đồ thị liên thông
        return True

# Ví dụ
dt = Graph()
dt.themCanh(0, 1)
dt.themCanh(0, 2)
dt.themCanh(1, 2)
dt.themCanh(2, 3)
print(dt.LienThong())  # Output: True

dt2 = Graph()
dt2.themCanh(0, 1)
dt2.themCanh(0, 2)
dt2.themCanh(3, 4)
print(dt2.LienThong())  # Output: False
