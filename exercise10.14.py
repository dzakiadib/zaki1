
from pathlib import Path
import json


def get_stored_username(path):
    """Mengambil username tersimpan, atau None kalau belum ada."""
    if path.exists():
        return json.loads(path.read_text())
    return None


def get_new_username(path):
    """Meminta username baru dan menyimpannya."""
    username = input("Siapa namamu? ")
    path.write_text(json.dumps(username))
    return username


def greet_user():
    """Menyapa user, setelah memastikan username-nya benar."""
    path = Path("username.json")
    username = get_stored_username(path)

    if username:
        jawaban = input(f"Apakah kamu {username}? (y/n) ")
        if jawaban.lower() == "y":
            print(f"Selamat datang kembali, {username}!")
        else:
            username = get_new_username(path)
            print(f"Kami akan mengingatmu, {username}!")
    else:
        username = get_new_username(path)
        print(f"Kami akan mengingatmu saat kamu kembali, {username}!")


greet_user()