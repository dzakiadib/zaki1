my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("Makanan favoritku adalah:")
for food in my_foods:
    print(food)

print("\nMakanan favorit temanku adalah:")
for food in friend_foods:
    print(food)