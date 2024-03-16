# Create a dictionary of three rivers and the country each river runs through
rivers = {
    'nile': 'egypt',
    'amazon': 'brazil',
    'yangtze': 'china'
}

# Print a sentence about each river
for river, country in rivers.items():
    print(f"The {river} runs through {country}.")

# Print the name of each river using .keys()
print("\nList of rivers:")
for river in rivers.keys():
    print(river)

# Print the name of each country using .values()
print("\nList of countries:")
for country in rivers.values():
    print(country)
