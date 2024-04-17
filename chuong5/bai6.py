class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1

class Cay:
    def __init__(self):
        self.root = None

    def ChieuCao(self, node):
        if node is None:
            return 0
        return node.height

    def ChieuCaoCay(self, node):
        if node is None:
            return 0
        return max(self.ChieuCaoCay(node.left), self.ChieuCaoCay(node.right)) + 1

    def KiemTraAVL(self, node):
        if node is None:
            return True
        
        balance_factor = self.ChieuCao(node.left) - self.ChieuCao(node.right)

        if abs(balance_factor) > 1:
            return False

        return self.KiemTraAVL(node.left) and self.KiemTraAVL(node.right)

# Ví dụ sử dụng:
# Tạo một cây nhị phân cân bằng (AVL)
cay = Cay()
cay.root = Node(10)
cay.root.left = Node(5)
cay.root.right = Node(15)
cay.root.left.left = Node(2)
cay.root.left.right = Node(7)
cay.root.right.right = Node(20)

print("Cây là cây AVL:", cay.KiemTraAVL(cay.root))
