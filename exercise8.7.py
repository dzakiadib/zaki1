def buat_album(artis, judul, jumlah_lagu=None):
    album = {"artis": artis.title(), "judul": judul.title()}
    if jumlah_lagu is not None:
        album["jumlah_lagu"] = jumlah_lagu
    return album

print(buat_album("tulus", "gajah"))
print(buat_album("sheila on 7", "kisah klasik untuk masa depan"))
print(buat_album("noah", "seperti seharusnya"))

# Dengan jumlah lagu
print(buat_album("tulus", "monokrom", jumlah_lagu=10))