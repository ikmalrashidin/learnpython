usernames = ['ADmin', 'ikmal', 'johan', 'armany', 'amin', 'firdaus']
current_users = ['admin', 'adam', 'azim', 'john', 'jess']

# Make a lowercase copy of all current users
current_users_lower = [user.lower() for user in current_users]

print (current_users_lower)

if usernames:
    for username in usernames:
        username_lower = username.lower()
        if username_lower in current_users_lower:
            print(f"Username '{username}' is already taken. Please choose another.")
        else:
            if username_lower == 'admin':
                print(f"Hello {username}, would you like to see a status report?")
            else:
                print(f"Hello {username}, thank you for logging in again!")
else:
    print("We need to find some users!")
