# 4-7. Threes: Make a list of the multiples of 3 from 3 to 30. Use a for loop to
# print the numbers in your list.

from audioop import mul


lista = []

for numero in range(3,31):
    if numero % 3 == 0:
        lista.append(numero)

print(lista)



