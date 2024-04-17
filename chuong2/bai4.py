class MaTran:
    def __init__(self, matrix):
        self.matrix = matrix
    
    def NhomHang(self):
        # Kiểm tra nếu ma trận không phải là ma trận vuông
        if len(self.matrix) != len(self.matrix[0]):
            print("Ma trận không phải là ma trận vuông.")
            return
        
        n = len(self.matrix)
        # Tạo một từ điển để lưu trữ nhóm chỉ mục hàng của các hàng giống nhau
        nhom_hang = {}
        # Duyệt qua từng hàng của ma trận
        for i in range(n):
            # Tạo một chuỗi từ chỉ mục hàng hiện tại
            index_str = str(i)
            # Nếu chuỗi này chưa xuất hiện trong từ điển, tạo một nhóm mới
            if index_str not in nhom_hang:
                nhom_hang[index_str] = [i]
            else:
                # Nếu chuỗi đã tồn tại, thêm chỉ mục hàng vào nhóm tương ứng
                nhom_hang[index_str].append(i)
        # In ra các nhóm chỉ mục hàng của các hàng giống nhau
        for key, value in nhom_hang.items():
            print("Nhóm", key, ":", value)

# Test
matrix1 = [[1, 2, 3],
           [4, 5, 6],
           [1, 2, 3],
           [7, 8, 9],
           [4, 5, 6]]

matran1 = MaTran(matrix1)
matran1.NhomHang()
