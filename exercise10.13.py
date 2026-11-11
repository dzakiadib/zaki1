
from pathlib import Path
import json


def ambil_data_tersimpan(path):
    """Mengembalikan dictionary data user, atau None kalau belum ada."""
    if path.exists():
        return json.loads(path.read_text())
    return None


def ambil_data_baru(path):
    """Meminta data user, menyimpannya ke file, lalu mengembalikannya."""
    data_user = {
        "nama": input("Siapa namamu? "),
        "kota": input("Kamu tinggal di kota mana? "),
        "hobi": input("Apa hobimu? "),
    }
    path.write_text(json.dumps(data_user))
    return data_user


def tampilkan_ringkasan(data_user):
    print("\nIni yang aku ingat tentangmu:")
    print(f"- Nama : {data_user['nama']}")
    print(f"- Kota : {data_user['kota']}")
    print(f"- Hobi : {data_user['hobi']}")


path = Path("data_user.json")
data_user = ambil_data_tersimpan(path)

if data_user:
    print(f"Selamat datang kembali, {data_user['nama']}!")
else:
    data_user = ambil_data_baru(path)
    print(f"Datamu akan kuingat, {data_user['nama']}!")

tampilkan_ringkasan(data_user)