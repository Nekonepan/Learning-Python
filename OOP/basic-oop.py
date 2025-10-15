class Mobil:
  def __init__(self, merk, warna):
    self.merk = merk
    self.warna = warna

  def nyalakan(self):
      print(f"{self.merk} berwarna {self.warna} sedang dinyalakan !")

mobil1 = Mobil("Porsche", "Hitam")
mobil2 = Mobil("BMW", "Putih")

mobil1.nyalakan()
mobil2.nyalakan()