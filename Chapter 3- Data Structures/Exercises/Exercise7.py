# Store the locations in a list (not in alphabetical order)
im_going_here = ["Tokyo", "Kyoto", "Osaka", "Mount Fuji", "Hokkaido"]


# Prints original order
print("Original order:", im_going_here)

# Printted alphabetically using sorted()
print("Alphabetical order:", sorted(im_going_here))

# Printed to show its still original order
print("Original order:", im_going_here)

# Printed the list in reverse alphabetical order 
print("Reverse alphabetical order:", sorted(im_going_here, reverse=True))

# Original order print
print("Original order:", im_going_here)

# Reversing the original list using reverse()
im_going_here.reverse()

# prints the reverse order
print("Reversed order:", im_going_here)

# Reversing the reversed version resulting back on its original order
im_going_here.reverse()

# Prints the list to show it's back to its original order
print("Original order:", im_going_here)

# Changes the original list so it's stored in alphabetical order using sort()
im_going_here.sort()

# Prints the list to show its order has changed
print("Sorted in alphabetical order:", im_going_here)

# list is now in reverse alphabetical order using sort()
im_going_here.sort(reverse=True)

# Print the list to show its order has changed
print("Sorted in reverse alphabetical order:", im_going_here)
