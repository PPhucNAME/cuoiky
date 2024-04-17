class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Cay:
    def __init__(self):
        self.root = None

    def SoNutLa(self, node):
        if node is None:
            return 0
        elif node.left is None and node.right is None:
            return 1
        else:
            return self.SoNutLa(node.left) + self.SoNutLa(node.right)

# Ví dụ sử dụng:
# Tạo một cây nhị phân
cay = Cay()
cay.root = Node(1)
cay.root.left = Node(2)
cay.root.right = Node(3)
cay.root.left.left = Node(4)
cay.root.left.right = Node(5)

print("Số nút lá của cây:", cay.SoNutLa(cay.root))
