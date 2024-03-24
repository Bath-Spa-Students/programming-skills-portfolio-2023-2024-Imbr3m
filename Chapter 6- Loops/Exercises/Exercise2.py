# I made a while loop where it loops infinetly
while True:

  age = int(input("Enter age: ")) #here the user will input their age

  if age < 3: # if it is false it will move on to the next one
    print("The ticket is free! Enjoy!")
  elif age <=12:
    print("The ticket is $10, Enjoy!")
  else:
    print("The ticket is $15, Enjoy!")

# then it loops all over again
