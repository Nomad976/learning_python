usernames = ['admin', 'eric', 'tom', 'nomad', 'demon']

for username in usernames:
    if username == 'admin':
        print("Hello admin, would you like to see a status report?")
    else:
        print("Hello " + username + ", thank you for logging in again.")

usernames.clear()
if not usernames:
    print("We need to find some users!")
