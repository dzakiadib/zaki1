from random import randint

class Die:
    def __init__(self, sides=6):
        self.sides = sides
    def roll_die(self):
        return randint(1, self.sides)
    
die_6 = Die()
print("Dadu 6 sisi:")
for roll in range(10):
    print(die_6.roll_die())
    
die_10 = Die(10)
print("\nDadu 10 sisi:")
for roll in range(10):
    print(die_10.roll_die())
    
die_20 = Die(20)
print("\nDADU 20 SISI:")
for roll in range(10):
    print(die_20.roll_die())