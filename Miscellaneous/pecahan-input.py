import math

class Pecahan:
    def __init__(self, pembilang, penyebut):
        if penyebut == 0:
            raise ValueError("Penyebut tidak boleh 0!")
        self.pembilang = pembilang
        self.penyebut = penyebut
        self.sederhanakan()

    def get_pembilang(self):
        return self.pembilang

    def get_penyebut(self):
        return self.penyebut

    def tambah(self, p):
        pembilang_baru = (self.pembilang * p.penyebut) + (p.pembilang * self.penyebut)
        penyebut_baru = self.penyebut * p.penyebut
        return Pecahan(pembilang_baru, penyebut_baru)

    def kurang(self, p):
        pembilang_baru = (self.pembilang * p.penyebut) - (p.pembilang * self.penyebut)
        penyebut_baru = self.penyebut * p.penyebut
        return Pecahan(pembilang_baru, penyebut_baru)

    def kali(self, p):
        pembilang_baru = self.pembilang * p.pembilang
        penyebut_baru = self.penyebut * p.penyebut
        return Pecahan(pembilang_baru, penyebut_baru)

    def bagi(self, p):
        if p.pembilang == 0:
            raise ValueError("Tidak bisa membagi dengan pecahan yang pembilangnya 0!")
        pembilang_baru = self.pembilang * p.penyebut
        penyebut_baru = self.penyebut * p.pembilang
        return Pecahan(pembilang_baru, penyebut_baru)

    def sederhanakan(self):
        fpb = math.gcd(self.pembilang, self.penyebut)
        self.pembilang //= fpb
        self.penyebut //= fpb

    def __str__(self):
        return f"{self.pembilang}/{self.penyebut}"


# ==== Bagian utama (main) ====
if __name__ == "__main__":
    print("=== Program Operasi Pecahan ===")

    try:
        # Input pecahan pertama
        a = int(input("Masukkan pembilang pecahan pertama: "))
        b = int(input("Masukkan penyebut pecahan pertama: "))
        p1 = Pecahan(a, b)

        # Input pecahan kedua
        c = int(input("Masukkan pembilang pecahan kedua: "))
        d = int(input("Masukkan penyebut pecahan kedua: "))
        p2 = Pecahan(c, d)

        print("\n=== Hasil Operasi ===")
        print(f"P1 = {p1}")
        print(f"P2 = {p2}")
        print(f"{p1} + {p2} = {p1.tambah(p2)}")
        print(f"{p1} - {p2} = {p1.kurang(p2)}")
        print(f"{p1} * {p2} = {p1.kali(p2)}")
        print(f"{p1} / {p2} = {p1.bagi(p2)}")

    except ValueError as e:
        print("Terjadi kesalahan:", e)
