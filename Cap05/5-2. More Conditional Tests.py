# 5-2. More Conditional Tests: You don’t have to limit the number of tests you
# create to ten. If you want to try more comparisons, write more tests and add
# them to conditional_tests.py. Have at least one True and one False result for
# each of the following:

# • Tests for equality and inequality with strings
msg_1 = 'Olá Mundo'
msg_2 = 'Ola mundo'
print(msg_1 == msg_2)

# • Tests using the lower() method
print(msg_1.lower == msg_2.lower)

# • Numerical tests involving equality and inequality, greater than and
# less than, greater than or equal to, and less than or equal to
n1 = 10
n2 = 20
print( n1 == n2)
print( n1 != n2)
print( n1 >= n2)
print( n1 <= n2)

# • Tests using the 'and' keyword and the 'or' keyword
print( n1 == n2 and n1 != n2)
print( n1 != n2 or n1 == n2)
print( n1 >= n2 and n1 <= n2)
print( n1 <= n2 or n1 >= n2)

# • Test whether an item is in a list
frutas = ['abacate','morango','ameixa','laranja','uva']

print('abacate' in frutas)
print('morango' in frutas)
print('ameixa' in frutas)
print('Laranja' in frutas)
print('Uva' in frutas)
# • Test whether an item is not in a list

if 'maçã' not in frutas:
    print('não tem maçã')

if 'banana' not in frutas:
    print('não tem banana')

if 'melancia' not in frutas:
    print('não tem melancia')