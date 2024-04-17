from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def themCanh(self, u, v):
        self.graph[u].append(v)

    def isCyclicUtil(self, v, visited, recStack):
        visited[v] = True
        recStack[v] = True

        for neighbor in self.graph[v]:
            if visited[neighbor] == False:
                if self.isCyclicUtil(neighbor, visited, recStack) == True:
                    return True
            elif recStack[neighbor] == True:
                return True

        recStack[v] = False
        return False

    def ChuTrinh(self):
        V = len(self.graph)
        visited = [False] * V
        recStack = [False] * V

        for node in range(V):
            if visited[node] == False:
                if self.isCyclicUtil(node, visited, recStack) == True:
                    return True

        return False

# Ví dụ
dt = Graph()
dt.themCanh(0, 1)
dt.themCanh(1, 2)
dt.themCanh(2, 0)
print(dt.ChuTrinh())  # Output: True

dt2 = Graph()
dt2.themCanh(0, 1)
dt2.themCanh(1, 2)
dt2.themCanh(2, 3)
print(dt2.ChuTrinh())  # Output: False
