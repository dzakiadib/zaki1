nama_file = "exercise10.2.txt"

with open(nama_file, "w") as file:
    file.write("In Python you can menyimpan data ke dalam variabel.\n")
    file.write("In Python you can membuat daftar (list) untuk menyimpan banyak nilai.\n")
    file.write("In Python you can mengulang perintah dengan perulangan for dan while.\n")
    file.write("In Python you can membuat fungsi agar kode bisa dipakai berulang kali.\n")
    file.write("In Python you can membaca dan menulis file.\n")

with open(nama_file) as file:
    for baris in file:
        baris_baru = baris.replace("Python", "C")
        print(baris_baru.rstrip())