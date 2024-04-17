def Giao(a, b):
    # Sử dụng set để tìm các phần tử xuất hiện cả trong a và b
    unique_nums_a = set(a)
    unique_nums_b = set(b)
    result = sorted(unique_nums_a.intersection(unique_nums_b))
    return result

# Ví dụ
a = [1, 5, 3, 7, 9, 4, 2]
b = [9, 6, 2, 3, 8]
c = Giao(a, b)
print(c)  # Output: [2, 3, 9]
