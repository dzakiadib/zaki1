def hitung_kata(nama_file, kata):
    """Menghitung kemunculan kata di dalam file teks."""
    try:
        with open(nama_file, encoding="utf-8") as file:
            isi = file.read()
    except FileNotFoundError:
        print(f"Maaf, file {nama_file} tidak ditemukan.")
    else:
        jumlah = isi.lower().count(kata)
        print(f"Kata '{kata}' muncul sekitar {jumlah} kali di {nama_file}.")


daftar_buku = ["alice.txt", "moby_dick.txt", "pride_and_prejudice.txt"]

for buku in daftar_buku:
    hitung_kata(buku, "the")      
    hitung_kata(buku, "the ")     
    print()