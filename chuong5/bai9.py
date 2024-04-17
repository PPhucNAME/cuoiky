class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Cay:
    def __init__(self):
        self.root = None

    def KiemTraCayCon(self, node1, node2):
        # Nếu cay2 là None, nó là cay con của mọi cây
        if node2 is None:
            return True
        # Nếu cay1 là None hoặc giá trị của hai nút không giống nhau, cay2 không thể là cay con của cay1
        if node1 is None or node1.data != node2.data:
            return False
        # Kiểm tra tiếp tục các cây con của cay1 và cay2
        return (self.KiemTraCayCon(node1.left, node2.left) and
                self.KiemTraCayCon(node1.right, node2.right))

    def CayCon(self, cay2):
        # Nếu cay2 là None, không có gì để kiểm tra, trả về False
        if cay2 is None:
            return False
        # Kiểm tra xem cay2 có phải là cây con của cay1 hay không
        return self.KiemTraCayCon(self.root, cay2.root)

# Ví dụ sử dụng:
# Tạo cây nhị phân 1
cay1 = Cay()
cay1.root = Node(1)
cay1.root.left = Node(2)
cay1.root.right = Node(3)
cay1.root.left.left = Node(4)
cay1.root.left.right = Node(5)

# Tạo cây nhị phân 2 là cây con của cây nhị phân 1
cay2 = Cay()
cay2.root = Node(2)
cay2.root.left = Node(4)
cay2.root.right = Node(5)

# Tạo cây nhị phân 3 không phải là cây con của cây nhị phân 1
cay3 = Cay()
cay3.root = Node(2)
cay3.root.left = Node(4)
cay3.root.right = Node(6)

print("Cây 2 là cây con của cây 1:", cay1.CayCon(cay2))
print("Cây 3 là cây con của cây 1:", cay1.CayCon(cay3))
