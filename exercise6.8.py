pets = [ {"jenis": "kucing", "pemilik": "Budi"},
    {"jenis": "anjing", "pemilik": "Sari"},
    {"jenis": "burung", "pemilik": "Andi"},
    {"jenis": "kelinci", "pemilik": "Dewi"},]

print("Hewan Peliharaan:")
for hewan in pets:
    for kunci, nilai in hewan.items():
        print(f"{kunci.title()}: {nilai.title()}")
    print()