nama_file = ["cats.txt", "dogs.txt"]

for nama in nama_file:
    try:
        with open(nama) as file:
            isi = file.read()
    except FileNotFoundError:
        print(f"Maaf, file {nama} tidak ditemukan.")
    else:
        print(f"Isi {nama}:")
        print(isi)