class Node:
    def __init__(self, heso, somu):
        self.HeSo = heso
        self.SoMu = somu
        self.KeTiep = None

class DaThuc:
    def __init__(self):
        self.Head = None

    def Them(self, heso, somu):
        if self.Head is None:
            self.Head = Node(heso, somu)
        else:
            current = self.Head
            while current.KeTiep is not None:
                current = current.KeTiep
            current.KeTiep = Node(heso, somu)

    def RutGon(self):
        if self.Head is None:
            return
        
        current = self.Head
        while current is not None:
            prev = current
            temp = current.KeTiep
            while temp is not None:
                if temp.SoMu == current.SoMu:
                    current.HeSo += temp.HeSo
                    prev.KeTiep = temp.KeTiep
                prev = temp
                temp = temp.KeTiep
            current = current.KeTiep

        current = self.Head
        while current is not None and current.HeSo == 0:
            self.Head = current.KeTiep
            current = self.Head
        while current is not None:
            temp = current.KeTiep
            if temp is not None and temp.HeSo == 0:
                current.KeTiep = temp.KeTiep
            else:
                current = current.KeTiep

    def Cong(self, dathuc2):
        result = DaThuc()

        # Thêm từng số hạng của dathuc1 vào kết quả
        current = self.Head
        while current is not None:
            result.Them(current.HeSo, current.SoMu)
            current = current.KeTiep

        # Thêm từng số hạng của dathuc2 vào kết quả
        current = dathuc2.Head
        while current is not None:
            result.Them(current.HeSo, current.SoMu)
            current = current.KeTiep

        # Rút gọn kết quả
        result.RutGon()

        return result

    def Xuat(self):
        current = self.Head
        while current is not None:
            print(f"{current.HeSo}x^{current.SoMu}", end="")
            if current.KeTiep is not None:
                print(" + ", end="")
            current = current.KeTiep
        print()


# Ví dụ sử dụng
dathuc1 = DaThuc()
dathuc1.Them(3, 2)
dathuc1.Them(4, 1)
dathuc1.Them(5, 0)

dathuc2 = DaThuc()
dathuc2.Them(1, 2)
dathuc2.Them(-4, 1)
dathuc2.Them(3, 0)

ketqua = dathuc1.Cong(dathuc2)
ketqua.Xuat()  # Output: 4x^2 + 5x^1 + 8
