# favorite_number_write.py
from pathlib import Path
import json

angka = int(input("Apa angka favoritmu? "))

path = Path("favorite_number.json")
path.write_text(json.dumps(angka))

print("Angka favoritmu sudah disimpan!")

# favorite_number_read.py
from pathlib import Path
import json

path = Path("favorite_number.json")
angka = json.loads(path.read_text())

print(f"I know your favorite number! It's {angka}.")

