daftar_nama = []

print("Ketik 'q' kapan saja untuk berhenti.")

while True:
    nama = input("Siapa nama kamu? ")
    if nama == "q":
        break
    daftar_nama.append(nama)
    print(f"Halo, {nama}! Namamu akan dicatat di buku tamu.")

with open("guest_book.txt", "w") as file:
    for nama in daftar_nama:
        file.write(nama + "\n")

print("Semua nama sudah ditulis ke guest_book.txt")