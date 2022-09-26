# 5-9. No Users: Add an if test to hello_admin.py to make sure the list of users is
# not empty.

# • If the list is empty, print the message We need to find some users!
# • Remove all of the usernames from your list, and make sure the correct
# message is printed.

users = []
# users = ['admin', 'brabo', 'vinicius','Jaden']

# • If the username is 'admin', print a special greeting, such as Hello admin,
# would you like to see a status report?

if users ==[]:
    print('We need to find some users!')
else:
    for user in users:
        if user == 'admin':
            print('Hello admin, would you like to see a status report?')
    # • Otherwise, print a generic greeting, such as Hello Jaden, thank you for
    # logging in again.
        else:
            print(f'Hello {user}, thank you for logging in again.')
