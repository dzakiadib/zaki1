tempat_favorit = {
    "budi": ["pantai", "gunung"],
    "sari": ["perpustakaan", "kafe", "taman kota"],
    "andi": ["lapangan futsal"],
}

print("Tempat Favorit")
for nama, tempat in tempat_favorit.items():
    print(f"Tempat favorit {nama.title()}:")
    for t in tempat:
        print(f"- {t.title()}")
    print()