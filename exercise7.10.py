
hasil_polling = {}

polling_aktif = True

while polling_aktif:
    nama = input("\nSiapa namamu? ")
    tempat = input("Jika kamu bisa mengunjungi satu tempat di dunia, ke mana kamu akan pergi? ")


    hasil_polling[nama] = tempat
    lagi = input("Apakah ada orang lain yang mau menjawab? (ya/tidak) ")
    if lagi == "tidak":
        polling_aktif = False

print("\n Hasil Polling Liburan Impian ")
for nama, tempat in hasil_polling.items():
    print(f"{nama} ingin pergi ke {tempat}.")