angka_favorit = {
    "andi": [7, 21],
    "sari": [13],
    "dewi": [42, 3, 9],
    "rudi": [3, 8],
    "maya": [21, 5],}

print("Angka Favorit")
for nama, daftar_angka in angka_favorit.items():
    print(f"Angka favorit {nama.title()}:")
    for angka in daftar_angka:
        print(f"- {angka}")
    print()