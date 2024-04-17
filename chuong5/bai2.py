class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Cay:
    def __init__(self):
        self.root = None

    def ChieuCao(self, node):
        if node is None:
            return -1
        else:
            left_height = self.ChieuCao(node.left)
            right_height = self.ChieuCao(node.right)
            return 1 + max(left_height, right_height)

# Ví dụ sử dụng:
# Tạo một cây nhị phân
cay = Cay()
cay.root = Node(1)
cay.root.left = Node(2)
cay.root.right = Node(3)
cay.root.left.left = Node(4)
cay.root.left.right = Node(5)

print("Chiều cao của cây:", cay.ChieuCao(cay.root))
