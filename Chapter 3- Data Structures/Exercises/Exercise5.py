# people i would invite
invite_people = ['Dwayne Johnson', 'Jotaro', 'Jim']

# Using f strings to print the invite letters
print(f'Hey {invite_people[0]}, come by later at my hosue to eat dinner.')
print(f'{invite_people[1]}! Come quick we have spaghetti!')
print(f'Yo man, come by later at my house we having dinner. See you {invite_people[2]}!')

# guest cant make it to dinner
print('\n') #made some space to see easier
print(f'Oh no! {invite_people[0]} cant make it to dinner! I will call someone else then.')

# Modifying the list to change the guest.
invite_people[0] = 'Mario'

# Inviting them again but with the new guest
print('\n') #made some space to see easier
print(f'Hey {invite_people[0]}, come by later at my hosue to eat dinner.')
print(f'{invite_people[1]}! Come quick we have spaghetti!')
print(f'Yo man, come by later at my house we having dinner. See you {invite_people[2]}!')

