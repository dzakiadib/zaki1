
sandwich_orders = ["tuna", "ayam", "telur", "keju"]

finished_sandwiches = []

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print(f"Saya sudah membuat sandwich {sandwich} pesananmu.")
    finished_sandwiches.append(sandwich)  

print("\nSemua sandwich yang sudah dibuat:")
for sandwich in finished_sandwiches:
    print(f"- {sandwich}")