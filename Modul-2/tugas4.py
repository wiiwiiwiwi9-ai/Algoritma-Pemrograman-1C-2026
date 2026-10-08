pin = int(input("masukkan PIN 3 digit: "))
jam = int(input("masukkan jam kedatangan (0-23): "))

digit1 = pin // 100
digit2 = (pin // 10) % 10
digit3 = pin % 10

if pin % 5 == 0:
    if jam < 12:
        akses_pintu = "garasi pagi terbuka"
    else:
        akses_pintu = "garasi malam terbuka, lampu dinyalakan"
elif pin % 2 == 0:
    if digit1 + digit3 == digit2:
        akses_pintu = "garasi VIP terbuka khusus bos"
    else:
        akses_pintu = "kode genap ditolak, alarm berbunyi"
else:
    akses_pintu = "akses ditolak"

status_cctv = "mode malam merekam" if jam > 18 else "mode siang standby"

print("digit pertama:", digit1)
print("digit kedua:", digit2)
print("digit ketiga:", digit3)
print("status akses:", akses_pintu)
print("status CCTV:", status_cctv)