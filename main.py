import time, sys
Damage = 0
Sword = "Wooden Sword "
Armour = "Chainmail Armour "
Protection = 5
inventory = [(str(Sword) + "Damage: " + str(Damage)), (str(Armour) + "Protection: " + str(Protection))] 
commandList = [".inv", ".help", ".quit"]
def commands(action):

    if (action == ".inv"):

        for a in range (len(inventory)):

            print(inventory[a])

    if (action == ".help"):

        for b in range(len(commandList)):

            print(commandList[b])

    if (action == ".quit"):

        print("See ya later!")    
        sys.exit()
print("Welcome to the best RPG Ever! Before we begin, we need to start out with the basic necessities")
username = input("What would you like your username to be?")
print(f"Cool name {username}!")
print("Now we need to choose your role")
choice = input(f"Please choose either role: Hero or Prince")
print("Great!")
print(f"Now that we have the necessities out of they way. It is time to begin {username}")
if choice == "Hero" or choice == "hero":

    print("Zzzzzzz....")
    time.sleep(1)
    print("Zzzzzz....Ugh")
    time.sleep(0.5)
    print("You wake up with the worst headache for the first time in years. You quickly put on your gear and report to the king. If you would like to see your inventory, type .inv for your inventory or .help for a list of commands at a given prompt like this one!")
    time.sleep(3)
    action = input("What would you like to do")
    commands(action)