import random

# defining the stat list
original_stats = ['strength', 'agility', 'fortitude', 'magic']

# player stats
p_stats = {'strength': 7, 'agility': 7, 'fortitude': 7, 'magic': 7}

# lists of monsters
monsters = ['goblin', 'orc', 'troll', 'slime', 'wolf']

# making the gold variable global so I can access it on multiple functions
global gold
gold = 100

# Fight function
def fight():
    global gold, p_stats
    
    while True:
        # used random.choice() to choose a monster from the monsters list
        monster = random.choice(monsters)
        # same thing here but choosing a random stat instead.
        fight_stat = random.choice(original_stats)
        
        # using random to make a monster attack between 1 to 25
        monster_attack = random.randint(1, 25)
        
        # printing the setting
        print(f'A wild {monster} appears!')
        print(f'The {monster} attacks you {monster_attack}pts with {fight_stat}!') #using f string because its easier
        
        # whatever the fight stat is, it will get the player stat value of that specific stat
        player_stat = p_stats[fight_stat]
        
        # chcks to see if your stat is higher than the monster's attack
        if player_stat >= monster_attack:
            print(f"You defeated the {monster}!")
            # the player will recieve gold between 15 to 25
            gold_reward = random.randint(15, 25)
            # adds the reward to your main gold which is global
            gold += gold_reward
            print(f'You earn +{gold_reward} gold!')
            
            # a feature I thought of, there is a 20% chance that you level up if you win the battle
            if random.random() < 0.2:
                print("Congratulations! You've leveled up!")
                # increases all player stats by 1
                for stat in p_stats:
                    p_stats[stat] += 1
                print("All your stats have increased by 1.")
                
            break
        else:
            #when you lose, this will print
            print(f"The {monster} defeated you!")
            break

# buy function to buy potions
def buy():
    global gold, p_stats
    
    # displaying the available potions with some art that took me 20min
    print('Welcome to the potion vending machine.')
    print(f'You have {gold} gold.')
    print('\nAvailable potions:')
    #i used multi line string to draw the art much easier
    # these are potion bottles by the way
    print('''
     _/\_       _/\_         _/\_        _/\_
    |    |     |    |       |    |      |    |
   |      |   |      |     |      |    |      |
    \____/     \____/       \____/      \____/

 1)Strength    2)Agility  3)Fortitude  4)Magic
     Potion    Potion     Potion       Potion
     25 gold   22.25 g    21.50 g      20 gold

     _/\_       _/\_         _/\_        _/\_        __/\__
    |    |     |    |       |    |      |    |      ||    ||
   /|    |\   /|    |\     /|    |\    /|    |\    //|    |\\
   |      |   |      |     |      |    |      |    ||      ||
    \____/     \____/       \____/      \____/     ||\____/||

 5)Greater    6)Greater  7)Greater     8)Greater    9)Level Up
   Strenght     Agility    Fortittude    Magic        Potion
   Potion       Potion     Potion        Potion       100 gold
   50 gold      44.5 g     43 g          40 gold
''')
    #if user types 0 it will exit
    print('0) Exit')

    # the choices

    # made it a while loop so it wont continue until the user answwers the question
    while True:
        choice = input('\nEnter the number of the potion you want to buy (or enter "0" to exit): ')

        if choice == '1':
            cost = 25
            potion_name = 'Strength Potion'
            stat_to_increase = 'strength'
        elif choice == '2':
            cost = 22.25
            potion_name = 'Agility Potion'
            stat_to_increase = 'agility'
        elif choice == '3':
            cost = 21.50
            potion_name = 'Fortitude Potion'
            stat_to_increase = 'fortitude'
        elif choice == '4':
            cost = 20
            potion_name = 'Magic Potion'
            stat_to_increase = 'magic'
        elif choice == '5':
            cost = 50
            potion_name = 'Greater Strength Potion'
            stat_to_increase = 'strength'
        elif choice == '6':
            cost = 44.5
            potion_name = 'Greater Agility Potion'
            stat_to_increase = 'agility'
        elif choice == '7':
            cost = 43
            potion_name = 'Greater Fortitude Potion'
            stat_to_increase = 'fortitude'
        elif choice == '8':
            cost = 40
            potion_name = 'Greater Magic Potion'
            stat_to_increase = 'magic'
        elif choice == '9':
            cost = 100
            potion_name = 'Level Up Potion'
        elif choice == '0':
            print('Exiting potion vending machine...\n')
            break # if 0 is chosen then this while loop is stopped and goes back to main()
        else:
            print('\nInvalid choice. Please enter a number between 0 and 9.')
            continue # similar to break but this make the if loop again

        print(f'The {potion_name} costs {cost} gold.')

        # the payment part of buy()
        while True:
            # the user will enter the amount they want to pay.
            payment_str = input('Enter the amount you want to pay: ')
            try:
                # using try and except blocks to convert the input to a float.
                payment = float(payment_str)
            except ValueError:
                # will display error message if you put characters which are not numbers because its converting it to float.
                print('Invalid input. Please enter a valid number.')
                continue  # similar to break but this makes it loop again

            if payment < cost:
                #if the user types the payment and is less than cost this will print   
                print('\nInsufficient payment. Please enter a higher amount.')
            elif gold < cost:
                #if the user did type the payment correctly but dont have enough gold this will print
                print('\nInsufficient payment. You do not have enough gold.')
                # then it takes you back to main
                main()
            else:
                #if all goes well it breaks and moves on
                break

        #this part manages if the user gave too much money so it gives change
                # the potions do different effects I had to seperate them        
        if payment == cost:
            #this will run if the payment is exactly the cost
            if choice == '9':
                gold -= cost #deducts gold from cost
                print(f'\nYou bought a {potion_name}. Enjoy!\n')
                for stat in p_stats: #potion 9 levels up all stats
                    p_stats[stat] += 1
                print("Congratulations! You've leveled up!")
                print("All your stats have increased by 1.")
                break 
            else:
                print(f'\nYou bought a {potion_name}. Enjoy!\n')
                gold -= cost
                if choice in ['5', '6', '7', '8']:
                    print(f"{stat_to_increase} +3!\n")
                    p_stats[stat_to_increase] += 3 #these greater potions increase 1 stat by 3
                else:
                    # if the potion is not the above then its probably a normal potion
                    print(f"{stat_to_increase} +1!\n")
                    p_stats[stat_to_increase] += 1  # increases stat by 1
                    
        else:
            #this will then run if player has given more payment than the cost which will result in change
            change = payment - cost 
            print(f'\nYou bought a {potion_name}. Your change is {change:.2f} gold. Enjoy!\n')# .2f means rounding it to 2 decimal points
            if choice not in ['9', '0']:
                gold -= cost
                if choice in ['5', '6', '7', '8']:
                    print(f"{stat_to_increase} +3!\n")
                    p_stats[stat_to_increase] += 3
                else:
                    print(f"{stat_to_increase} +1!\n")
                    p_stats[stat_to_increase] += 1  # Increase the corresponding stat

    print(f'You now have {gold} gold.') #prints how much gold you have left
    

#MAIN
def main():

    while True: #repeats while true
        screen = input('''
        Do you want to...
    (S)tat check
    (F)ight a monster
    (B)uy a potion
    (H)elp
    (Q)uit\n\n''').strip().upper()  # makes the input uppercase in case user types in lowercase and with space
        
        if screen == 'F':
            fight()
        elif screen == 'B':
            buy()  
        elif screen == 'S':
            print(p_stats)
        elif screen == 'H': # a help option to know if you dont know what you are doing
            print('''\nHelp:
- Stat Check (S): Allows you to view your current stats.
- Fight a Monster (F): Engage in a battle with a randomly selected monster.
- Buy a Potion (B): Purchase a potion to increase your stats.
- Quit (Q): Exit the game.\n''')
        elif screen == 'Q': # a quit option for extra featurea
            break
        else:
            # if the user type a different option from the following this will print.
            print('Invalid option. Try again') 

#i forgot what this does. my past teacher just told me to put it if im doing defining main() functions
if __name__ == "__main__":
    main()
