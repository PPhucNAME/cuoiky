class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Cay:
    def __init__(self):
        self.root = None

    def KiemTraBST(self, node, min_val=float('-inf'), max_val=float('inf')):
        if node is None:
            return True
        
        # Kiểm tra giá trị của nút hiện tại có nằm trong khoảng min_val và max_val hay không
        if node.data <= min_val or node.data >= max_val:
            return False
        
        # Kiểm tra các cây con của nút hiện tại
        return (self.KiemTraBST(node.left, min_val, node.data) and
                self.KiemTraBST(node.right, node.data, max_val))

# Ví dụ sử dụng:
# Tạo một cây nhị phân
cay = Cay()
cay.root = Node(4)
cay.root.left = Node(2)
cay.root.right = Node(6)
cay.root.left.left = Node(1)
cay.root.left.right = Node(3)

print("Cây là cây BST:", cay.KiemTraBST(cay.root))
