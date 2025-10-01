def input_data():
    # INPUT JUMLAH DATA
    while True:
        try:
            count = int(input("Masukkan jumlah data nilai yang akan di input: "))
            if count > 0:
                break
            else:
                print("Jumlah harus lebih dari 0")
        except ValueError:
            print("Masukkan angka yang valid!")

    data_list = []

    # INPUT NILAI
    for i in range(count):
        while True:
            try:
                nilai = float(input(f"Masukkan nilai mahasiswa ke-{i+1}: "))
                data_list.append(nilai)
                break
            except ValueError:
                print("Masukkan angka yang valid")

    # HITUNG RATA-RATA
    jumlah = sum(data_list)
    rata_rata = jumlah / len(data_list)

    # NILAI MIN & MAX
    min_nilai = min(data_list)
    max_nilai = max(data_list)

    # JUMLAH NILAI > 70
    counter = sum(1 for n in data_list if n > 70)

    # OUTPUT
    print("\nData nilai:", data_list)
    print("Jumlah data :", len(data_list))
    print("Rata-rata nilai mahasiswa :", rata_rata)
    print("Nilai terkecil mahasiswa :", min_nilai)
    print("Nilai terbesar mahasiswa :", max_nilai)
    print("Jumlah mahasiswa yang mendapat nilai lebih dari 70 :", counter)


# Jalankan program
input_data()
