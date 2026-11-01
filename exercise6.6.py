bahasa_favorit = { "zaki": "python", "adib": "c", "winur": "ruby", "seto": "python",}

daftar_peserta = ["zaki", "adib", "winur", "seto", ]

print("\n Jajak Pendapat")
for orang in daftar_peserta:
    if orang in bahasa_favorit.keys():
        print(f"Terima kasih {orang.title()}, kamu sudah mengisi jajak pendapat.")
    else:
        print(f"Halo {orang.title()}, yuk isi jajak pendapat bahasa pemrograman favoritmu!")
