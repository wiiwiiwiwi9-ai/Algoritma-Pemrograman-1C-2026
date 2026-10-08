suhu = int(input("masukkan suhu reaktor (celcius): "))
tekanan = int(input("masukkan tekanan gas (bar): "))

if suhu > 1000:
    if tekanan > 50:
        pesan = "MELTDOWN! SEGERA EVAKUASI!"
    else:
        pesan = "bahaya suhu: segera turunkan daya!"
elif suhu > 500:
    if tekanan > 30:
        pesan = "tekanan tidak stabil"
    else:
        pesan = "operasi reaktor normal"
else:
    pesan = "reaktor belum cukup panas"

status_pompa = "pompa maksimal" if suhu > 800 else "pompa normal"

print("suhu:", suhu, "celcius")
print("tekanan:", tekanan, "bar")
print("status reaktor:", pesan)
print("status pompa:", status_pompa)



