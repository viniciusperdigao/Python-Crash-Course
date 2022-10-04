# 6-7. People: Start with the program you wrote for Exercise 6-1 (page 99).


# Make two new dictionaries representing different people, and store all three dictionaries in a list called people. Loop through your list of people. As you loop through the list, print everything you know about each person.

pessoa_1 = {'first_name':'João', 'last_name':'Pedro', 'age':20, 'city':'Vitória'}

pessoa_2 = {'first_name':'Maria', 'last_name':'Eduarda', 'age':24, 'city':'Vitória'}

pessoa_3 = {'first_name':'Carlos', 'last_name':'Miguel', 'age':20, 'city':'Domingos Martins'}


people = [pessoa_1, pessoa_2, pessoa_3]


for person in people:
    name = f"{person['first_name'].title()} {person['last_name'].title()}"
    age = person['age']
    city = person['city'].title()
    
    print(f"{name}, of {city}, is {age} years old.")