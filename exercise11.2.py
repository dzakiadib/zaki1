def get_city_country(city, country, population):
    """Mengembalikan 'City, Country - population xxx'."""
    return f"{city}, {country} - population {population}".title()


def get_city_country(city, country, population=""):
    """Mengembalikan 'City, Country', dengan populasi jika diberikan."""
    if population:
        hasil = f"{city}, {country} - population {population}"
    else:
        hasil = f"{city}, {country}"
    return hasil.title()


from city_functions import get_city_country


def test_city_country():
    """Apakah 'santiago' dan 'chile' menghasilkan 'Santiago, Chile'?"""
    hasil = get_city_country("santiago", "chile")
    assert hasil == "Santiago, Chile"


def test_city_country_population():
    """Apakah populasi ikut ditampilkan kalau diberikan?"""
    hasil = get_city_country("santiago", "chile", population=5000000)
    assert hasil == "Santiago, Chile - population 5000000"