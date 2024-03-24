# dictionaries about different pets
pet1 = {'animal': 'dog', 'owner': 'Jotaro'}
pet2 = {'animal': 'cat', 'owner': 'Josuke'}
pet3 = {'animal': 'cat', 'owner': 'Dio'}
pet4 = {'animal': 'fish', 'owner': 'Joseph'}

# storing it in a list
pets = [pet1, pet2, pet3, pet4]

# loops throught the lists and printing the info
for pet in pets:
    print(f"Animal: {pet['animal']}")
    print(f"Owner: {pet['owner']}\n")
