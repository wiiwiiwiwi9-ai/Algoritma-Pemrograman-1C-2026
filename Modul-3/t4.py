
jumlah_penuh = 0

for i in range(1, 11):
    print("Mahasiswa ke-", i)

    nama = input("Nama mahasiswa: ")
    ipk = float(input("IPK: "))

    if ipk < 3.00:
        print("Tidak memenuhi syarat.")
        continue

    penghasilan = int(input("Penghasilan orang tua: "))

    if penghasilan <= 3000000:
        print(nama, "mendapat beasiswa penuh")
        jumlah_penuh = jumlah_penuh + 1

    elif penghasilan <= 5000000:
        print(nama, "mendapat beasiswa sebagian")

    else:
        print(nama, "tidak mendapat beasiswa")

    if jumlah_penuh == 3:
        print("Kuota beasiswa penuh sudah habis.")
        break

print("\nJumlah penerima beasiswa penuh:", jumlah_penuh)
