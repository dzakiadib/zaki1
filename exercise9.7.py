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

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


class Admin(User):
    """Class anak: administrator, adalah jenis khusus dari pengguna."""

    def __init__(self, first_name, last_name, age, city, email, occupation):
        super().__init__(first_name, last_name, age, city, email, occupation)
        # Daftar hak akses khusus admin
        self.privileges = ["can add post", "can delete post", "can ban user"]

    def show_privileges(self):
        """Menampilkan daftar hak akses admin."""
        print(f"Hak akses admin {self.first_name}:")
        for privilege in self.privileges:
            print(f"- {privilege}")


# Membuat objek Admin
admin = Admin("Rina", "Wijaya", 28, "Semarang", "rina@email.com", "Administrator")

admin.greet_user()       # method warisan dari User
admin.show_privileges()  # method milik Admin