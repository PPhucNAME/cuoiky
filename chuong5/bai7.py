class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Cay:
    def __init__(self):
        self.root = None

    def Chep(self, node):
        if node is None:
            return None
        new_node = Node(node.data)
        new_node.left = self.Chep(node.left)
        new_node.right = self.Chep(node.right)
        return new_node

# Ví dụ sử dụng:
# Tạo một cây nhị phân
cay = Cay()
cay.root = Node(1)
cay.root.left = Node(2)
cay.root.right = Node(3)
cay.root.left.left = Node(4)
cay.root.left.right = Node(5)

# Sao chép cây
cay_sao_chep = Cay()
cay_sao_chep.root = cay.Chep(cay.root)

# In ra cây sao chép để kiểm tra
def in_cay(node):
    if node:
        print(node.data)
        in_cay(node.left)
        in_cay(node.right)

print("Cây gốc:")
in_cay(cay.root)

print("\nCây sao chép:")
in_cay(cay_sao_chep.root)
