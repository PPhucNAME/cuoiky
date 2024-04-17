class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Cay:
    def __init__(self):
        self.root = None

    def SoSanh(self, node1, node2):
        if node1 is None and node2 is None:
            return True
        if node1 is not None and node2 is not None:
            return (node1.data == node2.data and
                    self.SoSanh(node1.left, node2.left) and
                    self.SoSanh(node1.right, node2.right))
        return False

# Ví dụ sử dụng:
# Tạo cây nhị phân 1
cay1 = Cay()
cay1.root = Node(1)
cay1.root.left = Node(2)
cay1.root.right = Node(3)
cay1.root.left.left = Node(4)
cay1.root.left.right = Node(5)

# Tạo cây nhị phân 2 giống hệt cây nhị phân 1
cay2 = Cay()
cay2.root = Node(1)
cay2.root.left = Node(2)
cay2.root.right = Node(3)
cay2.root.left.left = Node(4)
cay2.root.left.right = Node(5)

# Tạo cây nhị phân 3 khác cây nhị phân 1
cay3 = Cay()
cay3.root = Node(1)
cay3.root.left = Node(2)
cay3.root.right = Node(3)
cay3.root.left.left = Node(4)
cay3.root.left.right = Node(6)

print("Cây 1 và cây 2 giống hệt:", cay1.SoSanh(cay1.root, cay2.root))
print("Cây 1 và cây 3 giống hệt:", cay1.SoSanh(cay1.root, cay3.root))
