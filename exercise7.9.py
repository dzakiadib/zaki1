
sandwich_orders = ["pastrami", "tuna", "pastrami", "ayam", "telur", "pastrami"]
finished_sandwiches = []

print("Maaf, pastrami sudah habis.")

while "pastrami" in sandwich_orders:
    sandwich_orders.remove("pastrami")  

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print(f"Saya sudah membuat sandwich {sandwich} pesananmu.")
    finished_sandwiches.append(sandwich)

print("\nSemua sandwich yang sudah dibuat:")
for sandwich in finished_sandwiches:
    print(f"- {sandwich}")