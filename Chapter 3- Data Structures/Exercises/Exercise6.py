# Initial guest list
invite_people = ['Dwayne Johnson', 'Jotaro', 'Jim']

# Prints that I can only invite two people
print("Sorry, I can only invite two people for dinner.")

# Pop invite_people until only two names remain
#using while loop 
while len(invite_people) > 2:
    removed_guest = invite_people.pop()
    # used f strings so i can type it easier
    print(f"Sorry, {removed_guest}, your not invited! Bye!")

# Print messages to remaining invite_people in the list
for guest in invite_people:
    print(f"Hey {guest}, you are still invited!!!")

# removing the last two names
del invite_people[0]
# when it deletes, the [1] index becomes [0] so i deleted it twice
del invite_people[0]

# list is now empty
print("\nGuest list is now empty:", invite_people)
