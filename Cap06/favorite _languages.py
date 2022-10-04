# # favorite_languages = {
# # 'jen': 'python',
# # 'sarah': 'c',
# # 'edward': 'ruby',
# # 'phil': 'oi',
# # 'phil': 'test',
# # }

# # print(favorite_languages['phil'])



# # alien_0 = {'color': 'green', 'speed': 'slow'}
# # point_value = alien_0.get('color')
# # print(point_value)


# favorite_languages = {
# 'jen': 'python',
# 'sarah': 'c',
# 'edward': 'ruby',
# 'phil': 'python',
# }
# # #RODA OS VALORES NO LOOP
# # for name in favorite_languages.values():
# #     print(name.title())

# # #RODA AS CHAVES NO LOOP
# # for name in favorite_languages.keys():
# #     print(name.title())

# # #RODA CHAVE E VALOR NO LOOP
# # for name, language in favorite_languages.items():
# #     print(f"{name.title()}'s favorite language is {language.title()}.")



# friends = ['phil', 'sarah']
# for name in favorite_languages.keys():
#     print(name.title())
#     if name in friends:
#         language = favorite_languages[name].title()
#         print(f"\t{name.title()}, I see you love {language}!")

# print("The following languages have been mentioned:")
# for language in sorted(favorite_languages.values()):
#     print(language.title())


favorite_languages = {
'jen': ['python', 'ruby'],
'sarah': ['c'],
'edward': ['ruby', 'go'],
'phil': ['python', 'haskell'],
}

for name, languages in favorite_languages.items():
    print(f"\n{name.title()}'s favorite languages are:")
    for language in languages:
        print(f"\t{language.title()}")

