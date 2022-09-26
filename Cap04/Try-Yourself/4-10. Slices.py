# 4-10. Slices: Using one of the programs you wrote in this chapter, add several
# lines to the end of the program that do the following:



animals = ['gato', 'cachorro', 'cavalo', 'papagaio', 'calopsita','mamute']


for animal in animals:
    print(f'O {animal} é o melhor PET!')
print('Any of these animals would make a great pet!')



# • Print the message The first three items in the list are:. Then use a slice to
# print the first three items from that program’s list.

print(f'The first three items in the list are: {animals[0:3]}')

# • Print the message Three items from the middle of the list are:. Use a slice to
# print three items from the middle of the list.

print(f'Three items from the middle of the list are: {animals[int((len(animals)/2)-1):int((len(animals)/2)+2)]}')

# • Print the message The last three items in the list are:. Use a slice to print the
# last three items in the list.

print(f'The last three items in the list are: {animals[-3:]}')