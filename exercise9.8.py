class User:
    """Class induk: pengguna."""

    def __init__(self, first_name, last_name, age, city, email, occupation):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.city = city
        self.email = email
        self.occupation = occupation
        self.login_attempts = 0

    def describe_user(self):
        print(f"Nama       : {self.first_name} {self.last_name}")
        print(f"Umur       : {self.age} tahun")
        print(f"Kota       : {self.city}")
        print(f"Email      : {self.email}")
        print(f"Pekerjaan  : {self.occupation}")

    def greet_user(self):
        print(f"Halo, {self.first_name} {self.last_name}! Selamat datang kembali.")


class Privileges:
    """Class khusus untuk menyimpan dan menampilkan hak akses."""

    def __init__(self):
        self.privileges = ["can add post", "can delete post", "can ban user"]

    def show_privileges(self):
        """Menampilkan daftar hak akses."""
        print("Hak akses yang dimiliki:")
        for privilege in self.privileges:
            print(f"- {privilege}")


class Admin(User):
    """Class anak: administrator."""

    def __init__(self, first_name, last_name, age, city, email, occupation):
        super().__init__(first_name, last_name, age, city, email, occupation)
        # Objek Privileges disimpan sebagai atribut Admin
        self.privileges = Privileges()


# Membuat objek Admin baru
admin = Admin("Rina", "Wijaya", 28, "Semarang", "rina@email.com", "Administrator")

# Memanggil method lewat atribut privileges
admin.privileges.show_privileges()