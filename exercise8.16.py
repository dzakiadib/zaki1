def jelaskan_kota(kota, negara="Indonesia"):
    """Cetak kalimat sederhana tentang sebuah kota."""
    print(f"{kota.title()} ada di {negara.title()}.")
import kota
from kota import jelaskan_kota
from kota import jelaskan_kota as jk
import kota as k
from kota import *

kota.jelaskan_kota("semarang")
jelaskan_kota("yogyakarta")
jk("tokyo", "jepang")
k.jelaskan_kota("paris", "prancis")

jelaskan_kota("jakarta")