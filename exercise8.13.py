def buat_profil(nama_depan, nama_belakang, **info_pengguna):
    "Membuat dictionary berisi semua yang kita ketahui tentang pengguna."
    info_pengguna["nama_depan"] = nama_depan
    info_pengguna["nama_belakang"] = nama_belakang
    return info_pengguna

profil_saya = buat_profil("zaki", "adib", kota="Semarang", jurusan="Teknik Industri", hobi="membaca",)
print("\nProfil saya:")
print(profil_saya)
