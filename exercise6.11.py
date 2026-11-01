cities = {
    "jakarta": {
        "negara": "Indonesia",
        "populasi": 10600000,
        "fakta": "Dulu bernama Batavia pada masa kolonial.",},
    "tokyo": {
        "negara": "Jepang",
        "populasi": 14000000,
        "fakta": "Dulu bernama Edo sebelum tahun 1868.",},
    "paris": {
        "negara": "Prancis",
        "populasi": 2100000,
        "fakta": "Menara Eiffel selesai dibangun pada tahun 1889.",},
}

print(" Kota dan Informasi:")
for kota, info in cities.items():
    print(f"Kota: {kota.title()}")
    print(f"  Negara   : {info['negara']}")
    print(f"  Populasi : sekitar {info['populasi']}")
    print(f"  Fakta    : {info['fakta']}")
    print()