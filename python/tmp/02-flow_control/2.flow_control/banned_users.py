
banned_users = ['andrew', 'carolina', 'david','freddy']
user = 'rafael'

if user not in banned_users:
    print('{}, you can post a response if you wish.'.format(user.title()))
else:
    print('{}, are banned you dumb ass.'.format(user.title()))

