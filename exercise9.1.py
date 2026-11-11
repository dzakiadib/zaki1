class Restaurant:
    """Class untuk merepresentasikan sebuah restoran."""

    def __init__(self, restaurant_name, cuisine_type):
        # __init__ otomatis dijalankan saat objek dibuat
        # Menyimpan data restoran sebagai atribut
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Menampilkan nama dan jenis masakan restoran."""
        print(f"Nama restoran: {self.restaurant_name}")
        print(f"Jenis masakan: {self.cuisine_type}")

    def open_restaurant(self):
        """Menampilkan pesan bahwa restoran sedang buka."""
        print(f"{self.restaurant_name} sedang buka. Silakan masuk!")


# Membuat satu objek (instance) dari class Restaurant
restaurant = Restaurant("Warung Sedap", "Indonesia")

# Mencetak dua atribut secara terpisah
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)

# Memanggil kedua method
restaurant.describe_restaurant()
restaurant.open_restaurant()