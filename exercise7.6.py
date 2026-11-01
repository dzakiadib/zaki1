
print("--- Cara 1: kondisi di while ---")
topping = ""
while topping != "quit":
    topping = input("Topping (ketik 'quit' untuk selesai): ")
    if topping != "quit":
        print(f"Oke, {topping} akan kami tambahkan.")

print("\n--- Cara 2: variabel aktif ---")
aktif = True
while aktif:
    topping = input("Topping (ketik 'quit' untuk selesai): ")
    if topping == "quit":
        aktif = False   
    else:
        print(f"Oke, {topping} akan kami tambahkan.")

# Cara 3: pakai break
print("\n--- Cara 3: pakai break ---")
while True:
    topping = input("Topping (ketik 'quit' untuk selesai): ")
    if topping == "quit":
        break           
    print(f"Oke, {topping} akan kami tambahkan.")