print("\nMasukkan data album. Ketik 'q' kapan saja untuk berhenti.")

while True:
    artis = input("\nNama artis: ")
    if artis == "q":
        break

    judul = input("Judul album: ")
    if judul == "q":
        break

    album = buat_album(artis, judul)
    print(album)