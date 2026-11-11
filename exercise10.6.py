try:
    angka1 = int(input("Masukkan angka pertama: "))
    angka2 = int(input("Masukkan angka kedua: "))
except ValueError:
    print("Maaf, kamu harus memasukkan angka, bukan teks.")
else:
    print(f"Hasil penjumlahan: {angka1 + angka2}")