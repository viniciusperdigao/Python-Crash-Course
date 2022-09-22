bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)

#Print de um elemento de uma lista em determinada posição.
print(bicycles[0])

#Pode-se Utilizar métodos de string para converter o item de uma lista.
print(bicycles[0].capitalize())
print(bicycles[0].upper())

#Retorna sempre o último elemento da lista.
print(bicycles[-1])


message = f"I would like to own a {bicycles[2].upper()}."
print(message)