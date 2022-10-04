user_0 = {
'username': 'efermi',
'first': 'enrico',
'last': 'fermi',
}

favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
}

# for key, value in user_0.items():
#     print(f"\nKey: {key}")
#     print(f"Value: {value}")


# for name in favorite_languages.keys():
#     print(name.title())

# for name in sorted(favorite_languages.keys()):
#     print(f"{name.title()}, thank you for taking the poll.")

#Rodar em um dicionário de valores únicos.
print("The following languages have been mentioned:")
for language in set(favorite_languages.values()):
    print(language.title())
