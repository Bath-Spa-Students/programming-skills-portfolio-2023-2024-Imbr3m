#I made it so the user can input their age freely
age = int(input("How old are you? "))

# multiple if and elif statments 
if age < 2: # if less than 2 this will run
    print("You baby.")
elif age < 4: # if the previous is false then it will move on to the next one
    print("You are a toddler.")
elif age < 13: # if the previous is false then it will move on to the next one
    print("You're just a kid!")
elif age < 20: # if the previous is false then it will move on to the next one
    print("Ur now a teenager.")
elif age < 65: # if the previous is false then it will move on to the next one
    print("You is an adult.")
else: 
    print("You are very elder.") # if all the if and elif statement are false. else will run
