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
            # Tìm số hạng có cùng số mũ với số hạng hiện tại
            prev = current
            temp = current.KeTiep
            while temp is not None:
                if temp.SoMu == current.SoMu:
                    current.HeSo += temp.HeSo
                    prev.KeTiep = temp.KeTiep
                prev = temp
                temp = temp.KeTiep
            current = current.KeTiep

        # Loại bỏ các số hạng có hệ số bằng 0
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

    def Xuat(self):
        current = self.Head
        while current is not None:
            print(f"{current.HeSo}x^{current.SoMu}", end="")
            if current.KeTiep is not None:
                print(" + ", end="")
            current = current.KeTiep
        print()


# Ví dụ sử dụng
dathuc = DaThuc()
dathuc.Them(3, 2)
dathuc.Them(4, 1)
dathuc.Them(5, 0)
dathuc.Them(-4, 1)
dathuc.RutGon()
dathuc.Xuat()  # Output: 3x^2 + 1x^1 + 5
