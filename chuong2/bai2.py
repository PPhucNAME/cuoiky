class MaTran:
    def __init__(self, matrix):
        self.matrix = matrix
    
    def TamGiacTren(self):
        # Kiểm tra nếu ma trận không phải là ma trận vuông
        if len(self.matrix) != len(self.matrix[0]):
            return False
        
        n = len(self.matrix)
        # Duyệt qua từng hàng của ma trận
        for i in range(n):
            # Duyệt qua từng cột của hàng i
            for j in range(n):
                # Kiểm tra nếu phần tử không nằm trên đường chéo chính và có giá trị khác 0
                if i > j and self.matrix[i][j] != 0:
                    return False
        # Nếu không có phần tử nào không nằm dưới đường chéo chính khác 0, thì ma trận là tam giác trên
        return True

# Test
matrix1 = [[1, 2, 3, 3],
           [0, 4, 5, 4],
           [0, 0, 6, 5],
           [0, 0, 0, 5]]

matrix2 = [[1, 2, 3],
           [4, 5, 6],
           [7, 8, 9]]

matran1 = MaTran(matrix1)
matran2 = MaTran(matrix2)

print(matran1.TamGiacTren())  # Output: True
print(matran2.TamGiacTren())  # Output: False
