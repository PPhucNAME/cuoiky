class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Cay:
    def __init__(self):
        self.root = None

    def SoNut(self, node):
        if node is None:
            return 0
        else:
            return 1 + self.SoNut(node.left) + self.SoNut(node.right)

# Ví dụ sử dụng:
# Tạo một cây nhị phân
cay = Cay()
cay.root = Node(1)
cay.root.left = Node(2)
cay.root.right = Node(3)
cay.root.left.left = Node(4)
cay.root.left.right = Node(5)

print("Số nút của cây:", cay.SoNut(cay.root))
