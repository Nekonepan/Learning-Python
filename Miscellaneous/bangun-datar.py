import math

# ==================== BANGUN DATAR ====================
class PersegiPanjang:
    def __init__(self, panjang, lebar):
        self.panjang = panjang
        self.lebar = lebar

    def hitung_luas(self):
        return self.panjang * self.lebar

    def hitung_keliling(self):
        return 2 * (self.panjang + self.lebar)


class Lingkaran:
    def __init__(self, r):
        self.r = r

    def hitung_luas(self):
        return math.pi * self.r ** 2

    def hitung_keliling(self):
        return 2 * math.pi * self.r


class BujurSangkar:
    def __init__(self, sisi):
        self.sisi = sisi

    def hitung_luas(self):
        return self.sisi ** 2

    def hitung_keliling(self):
        return 4 * self.sisi


class BelahKetupat:
    def __init__(self, d1, d2, sisi):
        self.d1 = d1
        self.d2 = d2
        self.sisi = sisi

    def hitung_luas(self):
        return (self.d1 * self.d2) / 2

    def hitung_keliling(self):
        return 4 * self.sisi


class Segitiga:
    def __init__(self, alas, tinggi, s1, s2, s3):
        self.alas = alas
        self.tinggi = tinggi
        self.s1 = s1
        self.s2 = s2
        self.s3 = s3

    def hitung_luas(self):
        return 0.5 * self.alas * self.tinggi

    def hitung_keliling(self):
        return self.s1 + self.s2 + self.s3


# ==================== BANGUN RUANG ====================
class Kubus:
    def __init__(self, sisi):
        self.sisi = sisi

    def hitung_volume(self):
        return self.sisi ** 3

    def hitung_luas_permukaan(self):
        return 6 * self.sisi ** 2


class Balok:
    def __init__(self, p, l, t):
        self.p = p
        self.l = l
        self.t = t

    def hitung_volume(self):
        return self.p * self.l * self.t

    def hitung_luas_permukaan(self):
        return 2 * (self.p*self.l + self.p*self.t + self.l*self.t)


class Kerucut:
    def __init__(self, r, t, s):
        self.r = r
        self.t = t
        self.s = s

    def hitung_volume(self):
        return (1/3) * math.pi * self.r ** 2 * self.t

    def hitung_luas_permukaan(self):
        return math.pi * self.r * (self.r + self.s)


class Bola:
    def __init__(self, r):
        self.r = r

    def hitung_volume(self):
        return (4/3) * math.pi * self.r ** 3

    def hitung_luas_permukaan(self):
        return 4 * math.pi * self.r ** 2


class Silinder:
    def __init__(self, r, t):
        self.r = r
        self.t = t

    def hitung_volume(self):
        return math.pi * self.r ** 2 * self.t

    def hitung_luas_permukaan(self):
        return 2 * math.pi * self.r * (self.r + self.t)


# ==================== TESTER ====================
if __name__ == "__main__":
    persegi_panjang = [PersegiPanjang(5,3), PersegiPanjang(7,2), PersegiPanjang(10,4)]
    lingkaran = [Lingkaran(4), Lingkaran(7), Lingkaran(10)]
    bujur_sangkar = [BujurSangkar(5), BujurSangkar(8), BujurSangkar(12)]
    belah_ketupat = [BelahKetupat(6,8,5), BelahKetupat(10,12,8), BelahKetupat(14,16,10)]
    segitiga = [Segitiga(4,6,3,4,5), Segitiga(5,8,6,5,7), Segitiga(10,12,7,9,11)]

    kubus = [Kubus(3), Kubus(5), Kubus(7)]
    balok = [Balok(5,3,4), Balok(7,2,6), Balok(10,4,8)]
    kerucut = [Kerucut(3,5,6), Kerucut(5,7,8), Kerucut(7,10,12)]
    bola = [Bola(4), Bola(6), Bola(8)]
    silinder = [Silinder(3,7), Silinder(5,10), Silinder(7,12)]

    print("=== BANGUN DATAR ===")
    for i,p in enumerate(persegi_panjang):
        print(f"Persegi Panjang {i+1} -> Luas: {p.hitung_luas():.2f}, Keliling: {p.hitung_keliling():.2f}")
    for i,l in enumerate(lingkaran):
        print(f"Lingkaran {i+1} -> Luas: {l.hitung_luas():.2f}, Keliling: {l.hitung_keliling():.2f}")
    for i,b in enumerate(bujur_sangkar):
        print(f"Bujur Sangkar {i+1} -> Luas: {b.hitung_luas():.2f}, Keliling: {b.hitung_keliling():.2f}")
    for i,bk in enumerate(belah_ketupat):
        print(f"Belah Ketupat {i+1} -> Luas: {bk.hitung_luas():.2f}, Keliling: {bk.hitung_keliling():.2f}")
    for i,s in enumerate(segitiga):
        print(f"Segitiga {i+1} -> Luas: {s.hitung_luas():.2f}, Keliling: {s.hitung_keliling():.2f}")

    print("\n=== BANGUN RUANG ===")
    for i,k in enumerate(kubus):
        print(f"Kubus {i+1} -> Volume: {k.hitung_volume():.2f}, Luas Permukaan: {k.hitung_luas_permukaan():.2f}")
    for i,b in enumerate(balok):
        print(f"Balok {i+1} -> Volume: {b.hitung_volume():.2f}, Luas Permukaan: {b.hitung_luas_permukaan():.2f}")
    for i,k in enumerate(kerucut):
        print(f"Kerucut {i+1} -> Volume: {k.hitung_volume():.2f}, Luas Permukaan: {k.hitung_luas_permukaan():.2f}")
    for i,b in enumerate(bola):
        print(f"Bola {i+1} -> Volume: {b.hitung_volume():.2f}, Luas Permukaan: {b.hitung_luas_permukaan():.2f}")
    for i,s in enumerate(silinder):
        print(f"Silinder {i+1} -> Volume: {s.hitung_volume():.2f}, Luas Permukaan: {s.hitung_luas_permukaan():.2f}")