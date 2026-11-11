nama_file = ["cats.txt", "dogs.txt"]

for nama in nama_file:
    try:
        with open(nama) as file:
            isi = file.read()
    except FileNotFoundError:
        pass
    else:
        print(f"Isi {nama}:")
        print(isi)