jarak_pergi = 100
jarak_pulang = 100
konsumsi_bbm = 40
sisa_bbm = 1.5
harga_bbm = 10

jarak_tempuh_pp = jarak_pergi + jarak_pulang

total_kebutuhan_bbm = jarak_tempuh_pp / konsumsi_bbm

bbm_yang_sudah_dibayar = total_kebutuhan_bbm - sisa_bbm

total_biaya = bbm_yang_sudah_dibayar * harga_bbm

print("Total jarak perjalanan =", jarak_tempuh_pp, "km")
print("Total kebutuhan BBM =", total_kebutuhan_bbm, "liter")
print("BBM yang harus dibeli =", bbm_yang_sudah_dibayar, "liter")
print("Total biaya BBM = Rp", total_biaya)