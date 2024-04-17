class Mang:
    def __init__(self, matrix):
        self.matrix = matrix
    
    def DoiXung(self):
        # Kiểm tra nếu ma trận không phải là ma trận vuông
        if len(self.matrix) != len(self.matrix[0]):
            return False
        
        n = len(self.matrix)
        # Duyệt qua từng phần tử của ma trận và kiểm tra tính đối xứng
        for i in range(n):
            for j in range(n):
                # Kiểm tra nếu phần tử tại vị trí (i, j) khác phần tử tại vị trí (j, i)
                if self.matrix[i][j] != self.matrix[j][i]:
                    return False
        # Nếu không có phần tử nào không đối xứng, trả về True
        return True

# Sử dụng
matrix1 = [[1, 2, 3],
           [2, 4, 5],
           [3, 5, 6]]

matrix2 = [[1, 2, 3],
           [2, 4, 2],
           [3, 2, 7]]

mang1 = Mang(matrix1)
mang2 = Mang(matrix2)

print(mang1.DoiXung())  # Output: False
print(mang2.DoiXung())  # Output: True
