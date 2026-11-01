def buat_mobil(pabrikan, model, **info_tambahan):
    mobil = {"pabrikan": pabrikan, "model": model}
    for kunci, nilai in info_tambahan.items():
        mobil[kunci] = nilai
    return mobil

mobil = buat_mobil("subaru", "outback", warna="biru", paket_towing=True)
print("\nData mobil:")
print(mobil)