print("Ketik 'quit' untuk berhenti.")

while True:
    umur = input("Berapa umurmu? ")

    if umur == "quit":
        break

    umur = int(umur)

    if umur < 3:
        print("Tiketmu gratis.")
    elif umur <= 12:
        print("Harga tiketmu $10.")
    else:
        print("Harga tiketmu $15.")