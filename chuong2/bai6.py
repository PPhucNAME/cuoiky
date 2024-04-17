class NumberArray:
    def __init__(self, arr):
        self.arr = arr

    def Tru(self, other):
        # Đảm bảo độ dài của mảng a và b bằng nhau bằng cách thêm số 0 vào đầu cho đến khi bằng nhau
        max_len = max(len(self.arr), len(other.arr))
        a = [0] * (max_len - len(self.arr)) + self.arr
        b = [0] * (max_len - len(other.arr)) + other.arr

        # Khởi tạo biến mượn để xử lý khi trừ các số
        muon = 0
        result = []

        # Thực hiện phép trừ từ phải sang trái
        for i in range(max_len - 1, -1, -1):
            subtract = a[i] - b[i] - muon
            if subtract < 0:  # Nếu kết quả của phép trừ là âm, mượn 1 từ hàng bên trái
                subtract += 10
                muon = 1
            else:
                muon = 0
            result.append(subtract)

        # Loại bỏ các số 0 không cần thiết ở đầu kết quả
        while result[0] == 0:
            result.pop(0)

        return NumberArray(result)

    def __str__(self):
        return str(self.arr)


# Ví dụ sử dụng
a = NumberArray([4, 5, 6])
b = NumberArray([1, 2, 3])
result = a.Tru(b)
print(result)  # Output: [3, 3]
