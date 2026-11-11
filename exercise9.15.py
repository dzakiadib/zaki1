from random import sample

lottery_pool = [
    1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
    "A", "B", "C", "D", "E"
]
my_ticket = [7, 2, "A", "D"]
attempts = 0

print("LOTTERY ANALYSIS")
print("Tiket saya:", my_ticket)

while True:
    winning_ticket = sample(lottery_pool, 4)

    attempts += 1

    if set(winning_ticket) == set(my_ticket):
        print("\nSelamat! Tiket kamu menang!")
        print("Hasil undian:", winning_ticket)
        print("Jumlah percobaan:", attempts)
        break