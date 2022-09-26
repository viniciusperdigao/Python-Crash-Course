# 5-11. Ordinal Numbers: Ordinal numbers indicate their position in a list, such
# as 1st or 2nd. Most ordinal numbers end in th, except 1, 2, and 3.

positions = []

# • Store the numbers 1 through 9 in a list.
for pos in range(1,10):
    positions.append(pos)

# • Loop through the list.
# • Use an if-elif-else chain inside the loop to print the proper ordinal ending
# for each number. Your output should read "1st 2nd 3rd 4th 5th 6th
# 7th 8th 9th", and each result should be on a separate line.

for position in positions:
    if position == 1:
        print(f'{position}st')
    elif position == 2:
        print(f'{position}nd') 
    elif position == 3:
        print(f'{position}rd')  
    else:
        print(f'{position}th')