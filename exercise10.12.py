from pathlib import Path
import json

path = Path("favorite_number.json")

try:
    contents = path.read_text()
except FileNotFoundError:
    # Belum pernah disimpan: minta angka lalu simpan
    angka = int(input("Apa angka favoritmu? "))
    path.write_text(json.dumps(angka))
    print("Angka favoritmu sudah disimpan!")
else:
    # Sudah pernah disimpan: tampilkan
    angka = json.loads(contents)
    print(f"I know your favorite number! It's {angka}.")