kode_rahasi = int(input("masukkan kode digit : "))
digit1 = kode_rahasi// 100
digit2 = (kode_rahasi// 10) % 10
digit3 = kode_rahasi % 10

print("digit pertama:", digit1)
print("digit kedua:", digit2)
print("digit ketiga:", digit3)

pelacak_awal = digit1 * digit3
print("nilai pelacak awal:", pelacak_awal)

if digit2 % 2 == 1:
    pelacak_tahap1 = pelacak_awal + 25
else:
    pelacak_tahap1 = pelacak_awal - digit2
print("setelah tahap pertama:", pelacak_tahap1)

if pelacak_tahap1 % 3 == 0:
    pelacak_tahap2 = pelacak_tahap1 // 3
else:
    pelacak_tahap2= pelacak_tahap1 * 2
print("setelah tahap kedua (nilai akhir):", pelacak_tahap2)


if pelacak_tahap2 > 50:
    print("status password kategori A")
elif pelacak_tahap2> 20:
    print("status password kategori B")
else:
    print("status password ditolak")

if pelacak_tahap2 % 2 == 0:
    print("siklus genap")
else:
    print("siklus ganjil")