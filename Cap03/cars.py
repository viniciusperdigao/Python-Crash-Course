#Coloca a lista em ordem alfabética A-Z. Não poderemos mais inverter para ordem original.

cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)

# Inverto em ordem alfabética Z - A.
cars.sort(reverse=True)
print(cars)

# Sorteio os itens de uma lista mantendo a posição original dos itens.
print("Here is the original list:")
print(cars)
print("\nHere is the sorted list:")
print(sorted(cars))
print("\nHere is the original list again:")
print(cars)

#Inverter a ordem de uma lista, alterando a posição dos elementos.
cars.reverse()
print(cars)

#Achar o comprimento de unma lista

print(len(cars))
