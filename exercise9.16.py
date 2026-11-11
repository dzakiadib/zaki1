import random

print("Angka desimal acak:")
print(random.random())

print("\nAngka bulat acak:")
print(random.randint(1, 100))

fruits = ["Apel", "Mangga", "Pisang", "Pepaya"]
print("\nBuah yang dipilih secara acak:")
print(random.choice(fruits))
random.shuffle(fruits)
print("\nUrutan buah setelah diacak:")
print(fruits)
print("\n Dua buah yang dipilih:")
print(random.sample(fruits, 2))