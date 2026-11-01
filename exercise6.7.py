orang_1 = {"nama_depan": "zaki","nama_belakang": "addib","umur": 20,"kota": "solo",}
orang_2 = {"nama_depan": "winur","nama_belakang": "seto","umur": 19,"kota": "Yogyakarta",}
orang_3 = {"nama_depan": "Andi","nama_belakang": "Pratama","umur": 21, "kota": "Surabaya",}

people = [orang_1, orang_2, orang_3]

print("6-7. Orang-orang:")
for orang in people:
    for kunci, nilai in orang.items():
        print(f"{kunci.replace('_', ' ').title()}: {nilai}")
    print()
