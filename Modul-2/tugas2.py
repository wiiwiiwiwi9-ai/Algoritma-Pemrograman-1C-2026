total = int(input("masukkan total belanja: "))

if total % 100000 == 0:
    diskon = 100
elif total % 500000 == 0:
    diskon = 50
elif total % 10000 == 0:
    diskon = 20
elif total >= 200000:
    diskon = 10
else:
    diskon = 0

potongan_diskon = total * diskon / 100
bayar = total - potongan_diskon

poin = "poin bertambah" if bayar > 0 else "tidak ada poin"

print("total belanja awal:", total)
print("diskon:", diskon, "%")
print("total yang harus dibayar:", bayar)
print("Status poin:", poin)