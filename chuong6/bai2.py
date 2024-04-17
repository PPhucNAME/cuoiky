def Hieu(a, b):
    # Sử dụng set để tìm các phần tử chỉ xuất hiện trong a mà không xuất hiện trong b
    unique_nums_a = set(a)
    unique_nums_b = set(b)
    result = sorted(unique_nums_a - unique_nums_b)
    return result

# Ví dụ
a = [1, 5, 3, 7, 9, 4, 2]
b = [9, 6, 2, 3, 8]
c = Hieu(a, b)
print(c)  # Output: [1, 4, 5, 7]
