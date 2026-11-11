class Car:
    """Class untuk mobil secara umum."""

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Mengembalikan nama mobil yang rapi."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        print(f"Mobil ini sudah menempuh {self.odometer_reading} km.")


class Battery:
    """Class untuk baterai mobil listrik."""

    def __init__(self, battery_size=40):
        # Ukuran baterai default adalah 40 kWh
        self.battery_size = battery_size

    def describe_battery(self):
        print(f"Mobil ini punya baterai {self.battery_size}-kWh.")

    def get_range(self):
        """Menampilkan jarak tempuh sesuai ukuran baterai."""
        if self.battery_size == 40:
            range_km = 150
        elif self.battery_size == 65:
            range_km = 225
        else:
            range_km = 0   # ukuran lain tidak ada datanya

        print(f"Mobil ini bisa menempuh sekitar {range_km} km dengan sekali isi penuh.")

    def upgrade_battery(self):
        """Mengubah kapasitas baterai menjadi 65 jika belum 65."""
        if self.battery_size != 65:
            self.battery_size = 65
            print("Baterai berhasil di-upgrade ke 65-kWh.")
        else:
            print("Baterai sudah berkapasitas 65-kWh.")


class ElectricCar(Car):
    """Class untuk mobil listrik, mewarisi dari Car."""

    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        # Baterai disimpan sebagai objek Battery
        self.battery = Battery()


# Membuat mobil listrik dengan baterai default
my_tesla = ElectricCar("tesla", "model s", 2026)
print(my_tesla.get_descriptive_name())

# Pemanggilan get_range() pertama (baterai default 40 kWh)
my_tesla.battery.get_range()

# Upgrade baterai, lalu panggil get_range() lagi
my_tesla.battery.upgrade_battery()
my_tesla.battery.get_range()