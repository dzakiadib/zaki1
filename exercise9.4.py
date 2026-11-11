class Restaurant:
    """Class untuk merepresentasikan sebuah restoran."""

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        # Atribut baru dengan nilai default 0
        # (tidak perlu dikirim lewat parameter saat membuat objek)
        self.number_served = 0

    def describe_restaurant(self):
        print(f"Nama restoran: {self.restaurant_name}")
        print(f"Jenis masakan: {self.cuisine_type}")

    def open_restaurant(self):
        print(f"{self.restaurant_name} sedang buka. Silakan masuk!")

    def set_number_served(self, number):
        """Mengatur jumlah pelanggan yang sudah dilayani."""
        self.number_served = number

    def increment_number_served(self, increment):
        """Menambah jumlah pelanggan yang sudah dilayani."""
        self.number_served += increment


# Membuat objek restaurant
restaurant = Restaurant("Warung Sedap", "Indonesia")

# 1. Mencetak nilai awal (default 0)
print(f"Pelanggan dilayani: {restaurant.number_served}")

# 2. Mengubah nilai langsung lewat atribut, lalu cetak lagi
restaurant.number_served = 10
print(f"Pelanggan dilayani: {restaurant.number_served}")

# 3. Mengubah nilai lewat method set_number_served()
restaurant.set_number_served(25)
print(f"Pelanggan dilayani: {restaurant.number_served}")

# 4. Menambah nilai lewat method increment_number_served()
#    (misalnya 40 pelanggan datang dalam satu hari)
restaurant.increment_number_served(40)
print(f"Pelanggan dilayani: {restaurant.number_served}")