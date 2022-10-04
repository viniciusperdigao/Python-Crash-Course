# 6-5. Rivers: Make a dictionary containing three major rivers and the country

# each river runs through. One key-value pair might be 'nile': 'egypt'.
rios = {'Nilo':'Egito','Amazonas':'Brasil','Yangtze':'China'}

# • Use a loop to print a sentence about each river, such as The Nile runs
# through Egypt.

for rio, pais in rios.items():
    print(f'O rio {rio} pertence ao {pais}')

# • Use a loop to print the name of each river included in the dictionary.
for rio in rios.keys():
    print(rio)

# • Use a loop to print the name of each country included in the dictionary.
for pais in rios.values():
    print(pais)