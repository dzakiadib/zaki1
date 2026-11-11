from random import sample

# Membuat daftar angka dan huruf
lottery_pool = [
    1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
    "A", "B", "C", "D", "E"
]
winning_ticket = sample(lottery_pool, 4)

print("HASIL LOTRE")
print("Angka dan huruf yang terpilih:")

for item in winning_ticket:
    print(item)

print("\nTiket yang cocok dengan 4 pilihan ini")
print("berhak mendapatkan hadiah!")