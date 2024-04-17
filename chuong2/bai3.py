class MaTran:
    def __init__(self, matrix):
        self.matrix = matrix
    
    def TrungHang(self):
        # Kiểm tra nếu ma trận không phải là ma trận vuông
        if len(self.matrix) != len(self.matrix[0]):
            return False
        
        n = len(self.matrix)
        # Duyệt qua từng hàng của ma trận
        for i in range(n):
            # Duyệt qua từng hàng còn lại sau hàng i
            for j in range(i + 1, n):
                # Kiểm tra xem hàng i có giống với hàng j hay không
                if self.matrix[i] == self.matrix[j]:
                    return True
        # Nếu không tìm thấy hai hàng giống nhau, trả về False
        return False

# Test
matrix1 = [[1, 2, 3],
           [4, 5, 6],
           [1, 2, 3]]

matrix2 = [[7, 8, 9],
           [4, 5, 6],
           [7, 8, 9]]

matran1 = MaTran(matrix1)
matran2 = MaTran(matrix2)

print(matran1.TrungHang())  # Output: True
print(matran2.TrungHang())  # Output: False
