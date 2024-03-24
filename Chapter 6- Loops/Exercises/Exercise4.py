# I changed sandwitches to burgers instead
# BUrGR
burgers = ["Big Mac", "Whopper", "Fish o Fillet", "ChickenBurg", "DoubleBeefer"] # burger list
finished_burgers = [] #empty list where i will append later

for burger in burgers: #a for loop that goes through the burgers list
    print(f"Here is your {burger} burger. Thanks for ordering!") #prints an f-string
    finished_burgers.append(burger) #then appends the burger to the other list

print("\nBurgers ordered:") #after all burger in burgers where listed... this will execute
for burger in finished_burgers:
    print("- " + burger)