# 4-11. My Pizzas, Your Pizzas: Start with your program from Exercise 4-1
# (page 56). Make a copy of the list of pizzas, and call it friend_pizzas.
# Then, do the following:


pizzas = ['calabresa', '4 queijos', 'portuguesa','moda da casa']

friend_pizzas = pizzas[:]

## • Add a new pizza to the original list.

pizzas.append('marguerita')

# • Add a different pizza to the list friend_pizzas.
friend_pizzas.append('baiana')


# • Prove that you have two separate lists. Print the message My favorite
# pizzas are:, and then use a for loop to print the first list. Print the message
# My friend’s favorite pizzas are:, and then use a for loop to print the second
# list. Make sure each new pizza is stored in the appropriate list.
for pizza in pizzas:
    print(f'EMy favorite pizzas are {pizza.title()}')

for friend_pizza in friend_pizzas:
    print(f'My friend’s favorite pizzas are {friend_pizza.title()}')
