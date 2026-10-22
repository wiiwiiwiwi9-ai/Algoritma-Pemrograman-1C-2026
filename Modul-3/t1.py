jumlah = 0
pendapatan = 0
total_jarak = 0
terjauh = 0

while True:
    jarak = float(input("Masukkan jarak (km), 0 untuk selesai: "))
    if jarak == 0:
        break
    if jarak < 0:
        print("Jarak tidak valid!")
        continue

    if jarak <= 5:
        tarif = 3000
    elif jarak <= 15:
        tarif = 3000 + (jarak - 5) * 1000
    else:
        tarif = 13000 + (jarak - 15) * 500

    jumlah = jumlah + 1


    if jumlah % 5 == 0:
        tarif = tarif / 2
        print("Diskon 50%")

    pendapatan = pendapatan + tarif
    total_jarak = total_jarak + jarak

    if jarak > terjauh:
        terjauh = jarak

    print("Tarif: Rp", tarif)


if jumlah > 0:
    rata_rata = total_jarak / jumlah
else:
    rata_rata = 0


print("Jumlah penumpang:", jumlah)
print("Total pendapatan: Rp", pendapatan)
print("Jarak terjauh:", terjauh, "km")
print("Rata-rata jarak:", rata_rata, "km")
