class MaTranVuông:
    def __init__(self, mang):
        self.mang = mang

    def TamGiacDuoi(self):
        # Kiểm tra từng phần tử ở trên đường chéo chính và phần tử phía trên đường chéo chính
        # Nếu có phần tử khác không, trả về False
        for i in range(len(self.mang)):
            for j in range(i + 1, len(self.mang)):
                if self.mang[i][j] != 0:
                    return False
        return True

    def __str__(self):
        result = ""
        for row in self.mang:
            result += " ".join(map(str, row)) + "\n"
        return result.strip()


# Ví dụ sử dụng
mang1 = MaTranVuông([[1, 0, 0], [2, 3, 0], [4, 5, 6]])
mang2 = MaTranVuông([[1, 2, 3], [0, 4, 5], [0, 0, 6]])

print("Mang 1:")
print(mang1)
print("Tam giac duoi:", mang1.TamGiacDuoi())  # Output: True

print("\nMang 2:")
print(mang2)
print("Tam giac duoi:", mang2.TamGiacDuoi())  # Output: False
