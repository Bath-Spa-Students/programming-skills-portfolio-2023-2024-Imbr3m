#assigning variables 
usb_price = 6  # in pounds
total_budget = 50  # in pounds

# calculating the maximum number of USB sticks she can buy
num_usb_sticks = total_budget // usb_price

#calculating the total number of usbs - the budget
money_left = total_budget - (num_usb_sticks * usb_price)

# printing 
print("Number of USB sticks she can buy:", num_usb_sticks)
print("Pounds left after buying USB sticks:", money_left)
