print("Masukkan topping pizza yang kamu mau.")
print("Ketik 'quit' kalau sudah selesai.")

while True:
    topping = input("Topping: ")

    if topping == "quit":
        break

    print(f"Oke, {topping} akan kami tambahkan ke pizzamu.")

print("Pesanan pizza selesai. Terima kasih!")