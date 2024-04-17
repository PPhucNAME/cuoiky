import sys
import io
import os

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')

def Nhap_tu(s):
    while True:
        try:
            tu = input('Nhập %s: ' % s)
            if all(item == ' ' or item.isalpha() for item in tu):
                return tu
            else:
                print('Đây không phải là từ. Yêu cầu nhập lại.')
        except Exception as err:
            print(err)

def Nhapso():
    while True:
        try:
            n = int(input('Chọn chức năng cần thực hiện (0-4): '))
        except Exception as err:
            print(err)
        else:
            if not 0 <= n <= 4:
                print('Đây không phải là số nguyên dương 0-4. Yêu cầu nhập lại.')
            else:
                return n

def them_tu(dic):
    print('\t1.- Thêm từ')
    word = Nhap_tu('từ mới')
    meanings = []
    while True:
        type_word = Nhap_tu('từ loại (danh từ, động từ, tính từ)')
        meaning = Nhap_tu('nghĩa')
        example = Nhap_tu('ví dụ')
        meanings.append([type_word, meaning, example])
        if input('Thêm nghĩa khác cho từ này? (C/K): ').strip().upper() != 'C':
            break
    dic.append([word, meanings])
    print('Từ mới đã được thêm.')

def Tim_tu(dic):
    print('\t2.- Tìm từ')
    word = Nhap_tu('từ cần tìm')
    found = False
    for item in dic:
        if item[0] == word:
            print('Tìm thấy từ: %s' % word)
            print('Nghĩa:')
            for mean in item[1]:
                print('- [%s] %s: %s' % (mean[0], mean[1], mean[2]))
            found = True
            break
    if not found:
        print('Không tìm thấy từ %s trong từ điển' % word)

def xoa_tu(dic):
    print('\t3.- Xóa từ:')
    word = Nhap_tu('từ cần xóa')
    found = False
    for item in dic:
        if item[0] == word:
            print('Từ cần xóa: %s' % item[0])
            dic.remove(item)
            found = True
            print('Từ đã được xóa.')
            break
    if not found:
        print('Không tìm thấy từ %s cần xóa' % word)

def xem_tat_ca(dic):
    print('\t4.- Xem tất cả')
    if len(dic) == 0:
        print('Hiện tại từ điển của bạn không có từ nào. Bạn cần nhập thêm từ mới.')
    else:
        print('Từ điển của bạn:')
        for item in dic:
            print('Từ: %s' % item[0])
            print('Nghĩa:')
            for mean in item[1]:
                print('- [%s] %s - ví dụ: %s' % (mean[0], mean[1], mean[2]))
            print()

def menu():
    print('-' * 40)
    print('CHƯƠNG TRÌNH TẠO TỪ ĐIỂN'.center(40, '*'))
    print('-' * 40)
    print('\t1.- Thêm từ')
    print('\t2.- Tìm từ')
    print('\t3.- Xóa từ')
    print('\t4.- Xem tất cả')
    print('\t0.- Nhấn 0 để kết thúc chương trình')

def luu_tu_dien(file_name, dic):
    with open(file_name, 'w', encoding='utf-8') as file:
        for item in dic:
            file.write(item[0] + ',')
            for mean in item[1]:
                file.write(','.join(mean) + '|')
            file.write('\n')

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

def main():
    file_name = "mãsinhviên_mang.txt"
    dic = tai_tu_dien(file_name)
    while True:
        menu()
        choice = Nhapso()
        if choice == 0:
            print('Chương trình tạo từ điển kết thúc')
            luu_tu_dien(file_name, dic)
            break
        elif choice == 1:
            them_tu(dic)
        elif choice == 2:
            Tim_tu(dic)
        elif choice == 3:
            xoa_tu(dic)
        elif choice == 4:
            xem_tat_ca(dic)

if __name__ == "__main__":
    main()
