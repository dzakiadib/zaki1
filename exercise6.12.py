kota_lengkap = {
    "jakarta": {
        "negara": "Indonesia",
        "benua": "Asia",
        "populasi": 10600000,
        "fakta": "Dulu bernama Batavia pada masa kolonial.",
    },
    "tokyo": {
        "negara": "Jepang",
        "benua": "Asia",
        "populasi": 14000000,
        "fakta": "Dulu bernama Edo sebelum tahun 1868.",
    },
    "paris": {
        "negara": "Prancis",
        "benua": "Eropa",
        "populasi": 2100000,
        "fakta": "Menara Eiffel selesai dibangun pada tahun 1889.",
    },
}

print("Pengembangan Kota dan Informasi:")
for kota, info in kota_lengkap.items():
    populasi = f"{info['populasi']:,}".replace(",", ".")
    print(f"=== {kota.upper()} ===")
    print(f"Negara   : {info['negara']} ({info['benua']})")
    print(f"Populasi : sekitar {populasi} jiwa")
    print(f"Fakta    : {info['fakta']}")
    print()