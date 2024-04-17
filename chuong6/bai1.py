def Duynhat(a):
    # Sử dụng set để loại bỏ các phần tử trùng lặp và sắp xếp lại theo thứ tự tăng dần
    unique_nums = sorted(set(a))
    return unique_nums

# Ví dụ
a = [1, 5, 3, 7, 5, 9, 7]
b = Duynhat(a)
print(b)  # Output: [1, 3, 5, 7, 9]
