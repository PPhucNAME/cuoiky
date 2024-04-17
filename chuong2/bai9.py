class MaTranVuông:
    def __init__(self, mang):
        self.mang = mang

    def TrungCot(self):
        # Duyệt qua từng cột của ma trận
        for j in range(len(self.mang[0])):
            # Khởi tạo một set để lưu trữ giá trị của cột hiện tại
            col_set = set()
            for i in range(len(self.mang)):
                col_set.add(self.mang[i][j])

            # Nếu kích thước của set không bằng kích thước của hàng, có nghĩa là có ít nhất hai phần tử giống nhau trong cột
            if len(col_set) != len(self.mang):
                return True

        # Nếu không tìm thấy cột nào có hai phần tử giống nhau, trả về False
        return False

    def __str__(self):
        result = ""
        for row in self.mang:
            result += " ".join(map(str, row)) + "\n"
        return result.strip()


# Ví dụ sử dụng
mang1 = MaTranVuông([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
mang2 = MaTranVuông([[1, 2, 3], [4, 5, 6], [7, 5, 9]])

print("Mang 1:")
print(mang1)
print("Trung cot:", mang1.TrungCot())  # Output: False

print("\nMang 2:")
print(mang2)
print("Trung cot:", mang2.TrungCot())  # Output: True
