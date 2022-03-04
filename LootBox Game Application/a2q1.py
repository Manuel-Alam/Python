
valid_LootBox = False
valid_Amount = False
groundHog_Name = "Groundhog"
groundHog_Price = 1.00
squirrel_Name = "Squirrel"
squirrel_Price = 5.00
raven_Name = "Raven"
raven_Price = 10.00
selected_LootBox = ""
selected_LootBox_Price = 0

userName_Input = input("Welcome to the Carleton Loot Box Purchasing System. First, what's your player name?")

while (valid_LootBox is False):


        strlootBox_Input = input("Please select a loot box from the menu below:"
                              "\n\t1. [Common] {} (${})"
                              "\n\t2. [Rare] {} (${})"
                              "\n\t3. [Epic] {} (${})".format(groundHog_Name,groundHog_Price, squirrel_Name, squirrel_Price, raven_Name, raven_Price))

        if(strlootBox_Input.isdigit()):

            intlootBox_Input = int(strlootBox_Input)

            if (intlootBox_Input == 1 or intlootBox_Input == 2 or intlootBox_Input == 3):
                valid_LootBox = True

                if(intlootBox_Input == 1):
                    selected_LootBox = groundHog_Name
                    selected_LootBox_Price = groundHog_Price

                elif (intlootBox_Input == 2):
                    selected_LootBox = squirrel_Name
                    selected_LootBox_Price = squirrel_Price

                elif (intlootBox_Input == 3):
                    selected_LootBox = raven_Name
                    selected_LootBox_Price = raven_Price
            else:
                print("Error: That was not a valid selection.")
        else:
            print("Error: That was not a valid selection.")

while(valid_Amount is False):

    stramount_LootBox = input("How many {} (${}) would you like to purchase?".format(selected_LootBox, selected_LootBox_Price))

    if(stramount_LootBox.isdigit()):
        intamount_LootBox = int(stramount_LootBox)

        if(intamount_LootBox > 0):
            valid_Amount = True #this will end while loop for purchase amount.
        else:
            print("Please enter a valid amount of boxes.")
    else:
        print("Please enter a valid amount of boxes.")

total_Cost = intamount_LootBox*selected_LootBox_Price

print("Thanks, {}! Here is your receipt:"
      "\n-----------------------------"
      "\n{}x   {} (${})"
      "\n-----------------------------"
      "\nTotal Cost: ${:.2f}"
      "\nThank you! Good luck, gamer!".format(userName_Input, intamount_LootBox, selected_LootBox, selected_LootBox_Price, total_Cost))
