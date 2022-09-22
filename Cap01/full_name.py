# Utilizando F-Strings
first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print(full_name)


first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print(f"Hello, {full_name.title()}!")

#Adicionando Linhas = \n e Tabs =\t
print("Languages:\n\tPython\n\tC\n\tJavaScript")

#Eliminar espaços em branco de uma string.
favorite_language = ' python '
favorite_language.rstrip() # Corta caracteres a direita 

favorite_language.lstrip() # Corta caracteres a esquerda

favorite_language.strip() # Corta caratcteres da esquerad e direita.

