def buat_profil(nama_depan, nama_belakang, **info_pengguna):
    """Buat dictionary berisi semua yang diketahui tentang pengguna."""
    info_pengguna["nama_depan"] = nama_depan
    info_pengguna["nama_belakang"] = nama_belakang
    return info_pengguna


def buat_album(artis, judul, jumlah_lagu=None):
    """Buat dictionary yang menggambarkan sebuah album musik."""
    album = {"artis": artis.title(), "judul": judul.title()}
    if jumlah_lagu is not None:
        album["jumlah_lagu"] = jumlah_lagu
    return album


def kirim_pesan(belum_terkirim, terkirim):
    """Cetak setiap pesan, lalu pindahkan ke daftar pesan terkirim."""
    while belum_terkirim:
        pesan = belum_terkirim.pop()
        print(f"Mengirim pesan: {pesan}")
        terkirim.append(pesan)


profil_saya = buat_profil("Budi", "Santoso", kota="Semarang", hobi="membaca")
print(profil_saya)

album = buat_album("tulus", "gajah", jumlah_lagu=10)
print(album)

belum_terkirim = ["Halo!", "Nanti malam belajar bareng, ya."]
terkirim = []
kirim_pesan(belum_terkirim, terkirim)