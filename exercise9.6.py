class Restaurant:
    """Class induk: restoran."""

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"Nama restoran: {self.restaurant_name}")
        print(f"Jenis masakan: {self.cuisine_type}")

    def open_restaurant(self):
        print(f"{self.restaurant_name} sedang buka. Silakan masuk!")


class IceCreamStand(Restaurant):
    """Class anak: kios es krim, adalah jenis khusus dari restoran."""

    def __init__(self, restaurant_name, cuisine_type, flavors):
        # super() memanggil __init__ milik class induk (Restaurant)
        super().__init__(restaurant_name, cuisine_type)
        # Atribut khusus milik IceCreamStand
        self.flavors = flavors

    def display_flavors(self):
        """Menampilkan daftar rasa es krim."""
        print(f"Rasa es krim di {self.restaurant_name}:")
        for flavor in self.flavors:
            print(f"- {flavor}")


# Membuat objek IceCreamStand
stand = IceCreamStand("Es Krim Ceria", "Es krim", ["Vanila", "Cokelat", "Stroberi", "Matcha"])

stand.describe_restaurant()   # method warisan dari Restaurant
stand.display_flavors()       # method milik IceCreamStand