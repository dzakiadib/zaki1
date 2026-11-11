nama = input("Siapa nama kamu? ")

with open("guest.txt", "w") as file:
    file.write(nama)

print(f"Halo, {nama}! Namamu sudah dicatat di guest.txt")