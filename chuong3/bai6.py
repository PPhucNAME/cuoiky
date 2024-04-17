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

    def Chep(self):
        result = DaThuc()
        if self.Head is None:
            return result

        current = self.Head
        while current is not None:
            result.Them(current.HeSo, current.SoMu)
            current = current.KeTiep

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
dathuc = DaThuc()
dathuc.Them(3, 2)
dathuc.Them(4, 1)
dathuc.Them(5, 0)

dathuc_copy = dathuc.Chep()
dathuc_copy.Xuat()  # Output: 3x^2 + 4x^1 + 5
