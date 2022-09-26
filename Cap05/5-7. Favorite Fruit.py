# 5-7. Favorite Fruit: Make a list of your favorite fruits, and then write a series of
# independent if statements that check for certain fruits in your list.


# • Make a list of your three favorite fruits and call it favorite_fruits.

favorite_fruits = ['banana','laranja','limão','pera','uva']
other_fruits = ['pera', 'banana', 'laranja','maçã','jabuticaba']
# • Write five if statements. Each should check whether a certain kind of fruit
# is in your list. If the fruit is in your list, the if block should print a statement,
# such as You really like bananas!

for fruit in other_fruits:
    if fruit in favorite_fruits:
        print(f'You really like {fruit}!')
    else:
        print(f"You really don't like {fruit}!")