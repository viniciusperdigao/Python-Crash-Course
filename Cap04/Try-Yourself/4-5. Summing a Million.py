# 4-5. Summing a Million: Make a list of the numbers from one to one million,
# and then use min() and max() to make sure your list actually starts at one and
# ends at one million. Also, use the sum() function to see how quickly Python can
# add a million numbers.

lista = []

for numero in range (1,1_000_001):
    lista.append(numero)
print(f'Mínimo: {min(lista)}')
print(f'Máximo: {max(lista)}')
print(f'Soma da Lista: {sum(lista)}')


