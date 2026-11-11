class User:
    """Class untuk merepresentasikan profil seorang pengguna."""

    def __init__(self, first_name, last_name, age, city, email, occupation):
        # Atribut wajib: first_name dan last_name
        # Atribut tambahan yang umum ada di profil pengguna
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.city = city
        self.email = email
        self.occupation = occupation

    def describe_user(self):
        """Menampilkan ringkasan informasi pengguna."""
        print(f"Nama       : {self.first_name} {self.last_name}")
        print(f"Umur       : {self.age} tahun")
        print(f"Kota       : {self.city}")
        print(f"Email      : {self.email}")
        print(f"Pekerjaan  : {self.occupation}")

    def greet_user(self):
        """Menampilkan sapaan yang dipersonalisasi."""
        print(f"Halo, {self.first_name} {self.last_name}! Selamat datang kembali.")


# Membuat beberapa objek pengguna yang berbeda
user_1 = User("Budi", "Santoso", 20, "Semarang", "budi@email.com", "Mahasiswa")
user_2 = User("Siti", "Rahayu", 25, "Jakarta", "siti@email.com", "Desainer")
user_3 = User("Andi", "Pratama", 30, "Surabaya", "andi@email.com", "Insinyur")

# Memanggil kedua method untuk setiap pengguna
user_1.describe_user()
user_1.greet_user()
print()

user_2.describe_user()
user_2.greet_user()
print()

user_3.describe_user()
user_3.greet_user()