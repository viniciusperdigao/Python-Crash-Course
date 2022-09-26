#  4-13. Buffet: A buffet-style restaurant offers only five basic foods. Think of five
#  simple foods, and store them in a tuple
comidas = ('arroz', 'feijao', 'macarrao', 'salada', 'farofa')
print(comidas)
# Use a for loop to print each food the restaurant offers.

for comida in comidas:
    print(comida)

# • Try to modify one of the items, and make sure that Python rejects the change.


# comidas[0] = 'acabate'

# The restaurant changes its menu, replacing two of the items with different
# foods. Add a line that rewrites the tuple, and then use a for loop to print
# each of the items on the revised menu.

comidas = ('abacate', 'feijoada', 'macarrao', 'salada', 'farofa')
print(comidas)
for comida in comidas:
    print(comida)