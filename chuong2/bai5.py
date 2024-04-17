class NumberArray:
    def __init__(self, arr):
        self.arr = arr

    def Cong(self, other):
        # Đảm bảo độ dài của mảng a và b bằng nhau bằng cách thêm số 0 vào đầu cho đến khi bằng nhau
        max_len = max(len(self.arr), len(other.arr))
        a = [0] * (max_len - len(self.arr)) + self.arr
        b = [0] * (max_len - len(other.arr)) + other.arr

        # Khởi tạo biến c để lưu kết quả và biến tran để kiểm tra tràn số
        c = 0
        tran = False
        result = []

        # Thực hiện phép cộng từ phải sang trái
        for i in range(max_len - 1, -1, -1):
            total = a[i] + b[i] + c
            if total > 9:  # Kiểm tra tràn số
                tran = True
                result.append(-1)
                break
            else:
                result.append(total)
                c = 0 if total < 10 else 1

        # Nếu không có tràn số, đảo ngược kết quả và trả về
        if not tran:
            return NumberArray(result[::-1])
        else:
            return NumberArray(result)

    def __str__(self):
        return str(self.arr)


# Ví dụ sử dụng
a = NumberArray([1, 2, 3])
b = NumberArray([9, 9, 9])
result = a.Cong(b)
print(result)  # Output: [-1, -1, -1, -1]
