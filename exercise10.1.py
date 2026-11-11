nama_file = "exercise10.1.txt"

# Membuat file berisi ringkasan, tiap baris diawali "In Python you can"
with open(nama_file, "w") as file:
    file.write("In Python you can menyimpan data ke dalam variabel.\n")
    file.write("In Python you can membuat daftar (list) untuk menyimpan banyak nilai.\n")
    file.write("In Python you can mengulang perintah dengan perulangan for dan while.\n")
    file.write("In Python you can membuat fungsi agar kode bisa dipakai berulang kali.\n")
    file.write("In Python you can membaca dan menulis file.\n")

# Cara 1: membaca seluruh isi file sekaligus
print("=== Cara 1: Membaca seluruh file ===")
with open(nama_file) as file:
    isi = file.read()
print(isi)

# Cara 2: menyimpan baris-baris ke dalam list, lalu looping tiap baris
print("=== Cara 2: Looping per baris ===")
with open(nama_file) as file:
    daftar_baris = file.readlines()

for baris in daftar_baris:
    print(baris.rstrip())