print("Kalkulator penjumlahan. Ketik 'q' kapan saja untuk berhenti.")

while True:
    angka1 = input("\nAngka pertama: ")
    if angka1 == "q":
        break

    angka2 = input("Angka kedua: ")
    if angka2 == "q":
        break

    try:
        hasil = int(angka1) + int(angka2)
    except ValueError:
        print("Maaf, kamu harus memasukkan angka, bukan teks.")
    else:
        print(f"Hasil penjumlahan: {hasil}")