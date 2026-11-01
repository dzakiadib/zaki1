pizzas = ['pepperoni', 'margherita', 'hawaiian', 'BBQ chicken']
friend_pizzas = pizzas[:]

pizzas.append('four cheese')
friend_pizzas.append('mushroom')

print("Pizza favoritku adalah:")
for pizza in pizzas:
    print(pizza)

print("\nPizza favorit temanku adalah:")
for pizza in friend_pizzas:
    print(pizza)