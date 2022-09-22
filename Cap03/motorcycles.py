# # Trocando, Adicionando, e Removendo Elementos. 

# motorcycles = ['honda', 'yamaha', 'suzuki']
# print(motorcycles)

# #Trocando elemento da posição 0 
# motorcycles[0] = 'ducati'
# print(motorcycles)

# #Adicionar elemento a uma lista.

# motorcycles.append('ducati')
# print(motorcycles)

# #Removendo elementos de uma lista com DEL

# del motorcycles[0]
# print(motorcycles)

# #Removendo elementos de uma lista com o método pop()

motorcycles = ['honda', 'yamaha', 'suzuki']
first_owned = motorcycles.pop(0)
print(f"The first motorcycle I owned was a {first_owned.title()}.")
print(motorcycles)
first_owned = motorcycles.pop(0)
print(f"The first motorcycle I owned was a {first_owned.title()}.")
print(motorcycles)
first_owned = motorcycles.pop(0)
print(f"The first motorcycle I owned was a {first_owned.title()}.")
print(motorcycles)
first_owned = motorcycles.pop(0)


#Removendo um item da lista por valor.

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
motorcycles.remove('ducati')