# I changed sandwitches to burgers instead
# BUrGR
burgers = ["Big Mac", "Whopper", "Fish o Fillet", "ChickenBurg", "DoubleBeefer"] # burger list
finished_burgers = [] #empty list where i will append later

# Print a message about running out of ChikenBurg
print("So so sorry! we've run out of ChickenBurg!")

# Remove all occurrences of 'pastrami' from sandwich_orders
while 'ChickenBurg' in burgers:
    burgers.remove('ChickenBurg')

for burger in burgers: #a for loop that goes through the burgers list
    print(f"Here is your {burger} burger. Thanks for ordering!") #prints an f-string
    finished_burgers.append(burger) #then appends the burger to the other list

print("\nBurgers ordered:") #after all burger in burgers where listed... this will execute
for burger in finished_burgers:
    print("- " + burger)