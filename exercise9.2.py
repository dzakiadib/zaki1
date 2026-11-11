class Restaurant:
    """Class untuk merepresentasikan sebuah restoran."""

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"Nama restoran: {self.restaurant_name}")
        print(f"Jenis masakan: {self.cuisine_type}")

    def open_restaurant(self):
        print(f"{self.restaurant_name} sedang buka. Silakan masuk!")


# Membuat tiga objek restoran yang berbeda
restaurant_1 = Restaurant("Warung Sedap", "Indonesia")
restaurant_2 = Restaurant("Sakura Sushi", "Jepang")
restaurant_3 = Restaurant("Pizza Roma", "Italia")

# Memanggil describe_restaurant() untuk masing-masing objek
restaurant_1.describe_restaurant()
print()  # baris kosong agar output rapi
restaurant_2.describe_restaurant()
print()
restaurant_3.describe_restaurant()