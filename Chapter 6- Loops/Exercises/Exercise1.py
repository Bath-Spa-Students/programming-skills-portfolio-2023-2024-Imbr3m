# I made a while loop where it loops infinetly
while True:
  pizze_topping = input("Enter pizza topping: ") #here the user will input the toppings
  if pizze_topping == "quit": # if the user says quit it will run below else it will loop again
    print("OK sir! We will make your pizza with the toppings you requested!")
    break

