def Hop(a, b):
    # Sử dụng set để tìm các phần tử có trong a hoặc b
    unique_nums_a = set(a)
    unique_nums_b = set(b)
    result = sorted(unique_nums_a.union(unique_nums_b))
    return result

# Ví dụ
a = [1, 5, 3, 7, 9, 4, 2]
b = [9, 6, 2, 3, 8]
c = Hop(a, b)
print(c)  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]
