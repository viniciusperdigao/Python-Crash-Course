#Maneira correta de usar ' ou " dentro de uma string.
message = "One of Python's strengths is its diverse community."
print(message)


# Desta forma vai dar erro. 
# message = 'One of Python's strengths is its diverse community.'
# print(message)


# 2-3. Personal Message: Use a variable to represent a person’s name, and print
# a message to that person. Your message should be simple, such as, “Hello Eric,
# would you like to learn some Python today?”

nome_pessoa = 'PiNk'
print(f'Hello {nome_pessoa}, would you like to learn some Python today?')

# 2-4. Name Cases: Use a variable to represent a person’s name, and then print
# that person’s name in lowercase, uppercase, and title case.

a = nome_pessoa.title()
print(a)
b = nome_pessoa.lower()
print(b)
c = nome_pessoa.upper()
print(c)

print(nome_pessoa)

# 2-5. Famous Quote: Find a quote from a famous person you admire. Print the
# quote and the name of its author. Your output should look something like the
# following, including the quotation marks:

albert_msg = 'Albert Einstein once said, “A person who never made a mistake never tried anything new.”'
print(albert_msg)