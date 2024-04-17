class NumberArray:
    def __init__(self, arr):
        self.arr = arr

    def Nhan(self, other):
        # Đảm bảo độ dài của mảng a và b bằng nhau bằng cách thêm số 0 vào đầu cho đến khi bằng nhau
        max_len = len(self.arr) + len(other.arr)
        a = [0] * (max_len - len(self.arr)) + self.arr
        b = [0] * (max_len - len(other.arr)) + other.arr

        # Khởi tạo biến kết quả và biến tràn để kiểm tra tràn số
        result = [0] * max_len
        tran = False

        # Thực hiện phép nhân từ phải sang trái
        for i in range(len(b) - 1, -1, -1):
            carry = 0
            for j in range(len(a) - 1, -1, -1):
                temp = result[i + j + 1] + (a[j] * b[i]) + carry
                result[i + j + 1] = temp % 10
                carry = temp // 10

            # Kiểm tra tràn số
            if carry != 0:
                tran = True
                break

        # Nếu có tràn số, trả về mảng chứa -1, ngược lại trả về kết quả của phép nhân
        return result if tran else NumberArray(result)

    def __str__(self):
        return str(self.arr)


# Ví dụ sử dụng
a = NumberArray([1, 2, 3])
b = NumberArray([4, 5])
result = a.Nhan(b)
print(result)  # Output: [0, 0, 5, 7, 3, 5]
