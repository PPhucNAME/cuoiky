import sys
import io
import os
import tkinter as tk
from tkinter import simpledialog, messagebox

# Thiết lập mã hóa UTF-8 cho sys.stdout để hỗ trợ tiếng Việt
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')

# Hàm nhập từ từ người dùng
def nhap_tu(s):
    while True:
        try:
            # Sử dụng simpledialog để hiển thị hộp thoại nhập từ
            tu = simpledialog.askstring("Nhập từ", "Nhập {}: ".format(s))
            # Nếu người dùng không nhập gì, trả về None
            if tu is None:
                return None
            # Kiểm tra xem từ có chứa ký tự không phải chữ cái không
            if all(item == ' ' or item.isalpha() for item in tu):
                return tu
            else:
                # Hiển thị thông báo lỗi nếu từ không hợp lệ
                messagebox.showerror("Lỗi", "Đây không phải là từ. Yêu cầu nhập lại.")
        except Exception as err:
            # Hiển thị thông báo lỗi nếu có lỗi xảy ra
            messagebox.showerror("Lỗi", str(err))

# Hàm nhập số nguyên từ người dùng
def nhap_so():
    while True:
        try:
            # Sử dụng simpledialog để hiển thị hộp thoại nhập số nguyên
            n = simpledialog.askinteger("Chọn chức năng", "Chọn chức năng cần thực hiện (1-4): ")
            # Nếu người dùng không nhập gì, trả về None
            if n is None:
                return None
            # Kiểm tra xem số nhập vào có nằm trong khoảng 0-4 không
            if not 0 <= n <= 4:
                # Hiển thị thông báo lỗi nếu số không hợp lệ
                messagebox.showerror("Lỗi", "Đây không phải là số nguyên dương 1-4. Yêu cầu nhập lại.")
            else:
                return n
        except Exception as err:
            # Hiển thị thông báo lỗi nếu có lỗi xảy ra
            messagebox.showerror("Lỗi", str(err))

# Hàm thêm từ vào từ điển
def them_tu(dic):
    # Nhập từ mới
    word = nhap_tu('từ mới')
    # Nếu người dùng không nhập gì, thoát hàm
    if word is None:
        return
    meanings = []
    while True:
        # Nhập loại từ
        type_word = nhap_tu('từ loại (danh từ, động từ, tính từ)')
        # Nếu người dùng không nhập gì, thoát hàm
        if type_word is None:
            return
        # Nhập nghĩa của từ
        meaning = nhap_tu('nghĩa')
        # Nếu người dùng không nhập gì, thoát hàm
        if meaning is None:
            return
        # Nhập ví dụ minh họa
        example = nhap_tu('ví dụ')
        # Nếu người dùng không nhập gì, thoát hàm
        if example is None:
            return
        # Thêm nghĩa mới vào meanings
        meanings.append([type_word, meaning, example])
        # Hỏi người dùng có muốn thêm nghĩa khác cho từ này không
        if messagebox.askyesno("Thêm nghĩa", "Thêm nghĩa khác cho từ này?"):
            continue
        else:
            break
    # Thêm từ mới và các nghĩa của nó vào từ điển
    dic.append([word, meanings])
    # Hiển thị thông báo thành công
    messagebox.showinfo("Thông báo", "Từ mới đã được thêm.")

# Hàm tìm từ trong từ điển
def tim_tu(dic):
    # Nhập từ cần tìm
    word = nhap_tu('từ cần tìm')
    # Nếu người dùng không nhập gì, thoát hàm
    if word is None:
        return
    found = False
    for item in dic:
        if item[0] == word:
            meaning_str = ''
            for mean in item[1]:
                meaning_str += '- [%s] %s: %s\n' % (mean[0], mean[1], mean[2])
            # Hiển thị thông tin về từ tìm được
            messagebox.showinfo("Tìm từ", 'Tìm thấy từ: {}\nNghĩa:\n{}'.format(word, meaning_str))
            found = True
            break
    if not found:
        # Hiển thị thông báo nếu không tìm thấy từ
        messagebox.showinfo("Tìm từ", 'Không tìm thấy từ {} trong từ điển'.format(word))

# Hàm xóa từ khỏi từ điển
def xoa_tu(dic):
    # Nhập từ cần xóa
    word = nhap_tu('từ cần xóa')
    # Nếu người dùng không nhập gì, thoát hàm
    if word is None:
        return
    found = False
    for item in dic:
        if item[0] == word:
            # Xác nhận việc xóa từ
            confirm = messagebox.askyesno("Xóa từ", "Từ cần xóa: {}\nBạn có chắc chắn muốn xóa không?".format(item[0]))
            if confirm:
                # Xóa từ khỏi từ điển
                dic.remove(item)
                # Hiển thị thông báo xóa thành công
                messagebox.showinfo("Thông báo", "Từ đã được xóa.")
            found = True
            break
    if not found:
        # Hiển thị thông báo nếu không tìm thấy từ cần xóa
        messagebox.showinfo("Thông báo", 'Không tìm thấy từ {} cần xóa'.format(word))

# Hàm xem tất cả các từ trong từ điển
def xem_tat_ca(dic):
    if len(dic) == 0:
        # Hiển thị thông báo nếu từ điển rỗng
        messagebox.showinfo("Tất cả từ", "Hiện tại từ điển của bạn không có từ nào. Bạn cần nhập thêm từ mới.")
    else:
        word_meaning_str = ''
        for item in dic:
            meaning_str = ''
            for mean in item[1]:
                meaning_str += '- [%s] %s - ví dụ: %s\n' % (mean[0], mean[1], mean[2])
            word_meaning_str += 'Từ: {}\nNghĩa:\n{}\n\n'.format(item[0], meaning_str)
        # Hiển thị tất cả các từ trong từ điển
        messagebox.showinfo("Tất cả từ", word_meaning_str)

# Hàm hiển thị menu chương trình
def menu():
    # Hiển thị menu chức năng của chương trình
    messagebox.showinfo("Chương trình tạo từ điển", "\n1.- Thêm từ\n2.- Tìm từ\n3.- Xóa từ\n4.- Xem tất cả\n")

# Hàm lưu từ điển xuống file
def luu_tu_dien(file_name, dic):
    with open(file_name, 'w', encoding='utf-8') as file:
        for item in dic:
            file.write(item[0] + ',')
            for mean in item[1]:
                file.write(','.join(mean) + '|')
            file.write('\n')

# Hàm tải từ điển từ file
def tai_tu_dien(file_name):
    if not os.path.exists(file_name):
        return []
    with open(file_name, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        dic = []
        for line in lines:
            parts = line.strip().split(',')
            word = parts[0]
            meanings = []
            for mean in parts[1].split('|'):
                mean_parts = mean.split(',')
                if len(mean_parts) == 3:
                    meanings.append(mean_parts)
            dic.append([word, meanings])
        return dic

# Hàm chính của chương trình
def main():
    # Tên file chứa từ điển
    file_name = "mãsinhviên_mang.txt"
    # Tải từ điển từ file
    dic = tai_tu_dien(file_name)
    while True:
        # Hiển thị menu chức năng
        menu()
        # Nhập lựa chọn từ người dùng
        choice = nhap_so()
        # Nếu người dùng không nhập gì, kết thúc chương trình
        if choice is None:
            messagebox.showinfo("Thông báo", "Chương trình tạo từ điển kết thúc")
            # Lưu từ điển vào file
            luu_tu_dien(file_name, dic)
            break
        elif choice == 1:
            them_tu(dic)
        elif choice == 2:
            tim_tu(dic)
        elif choice == 3:
            xoa_tu(dic)
        elif choice == 4:
            xem_tat_ca(dic)

if __name__ == "__main__":
    main()
