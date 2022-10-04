# 6-6. Polling: Use the code in favorite_languages.py (page 97).

# • Make a list of people who should take the favorite languages poll. Include some names that are already in the dictionary and some that are not.

favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
'phil': 'test',
}

pessoas = ['jen', 'sarah','barbara','joaquim']

# • Loop through the list of people who should take the poll. If they have already taken the poll, print a message thanking them for responding.

for pessoa in pessoas:
    print(f'\n{pessoa}')

    if pessoa in favorite_languages:
        print(f'{favorite_languages[pessoa]}')
    else:
        print(f'{pessoa}, você deve escolher alguma linguagem de programação.')

# If they have not yet taken the poll, print a message inviting them to take
# the poll.