from array import*

valid_LootBox = False
valid_Amount = False
cart_Valid = False
groundHog_Name = "Groundhog"
groundHog_Price = 1.00
squirrel_Name = "Squirrel"
squirrel_Price = 5.00
raven_Name = "Raven"
raven_Price = 10.00
selected_LootBox = ""
selected_LootBox_Price = 0

amount_LootBox = 0
amount_GroundHog = 0
amount_Squirrel = 0
amount_Raven = 0
total_Cost = 0

boxAmount_List = array('i', [amount_GroundHog, amount_Squirrel, amount_Raven])
boxName_List = [groundHog_Name, squirrel_Name, raven_Name]
boxPrice_List = array("f", [groundHog_Price, squirrel_Price, raven_Price])

complete_Purchase = False

userName_Input = input("Welcome to the Carleton Loot Box Purchasing System. First, what's your player name?")

while(complete_Purchase is False):

    while (valid_LootBox is False):

            strlootBox_Input = input("Please select a loot box from the menu below:"
                                  "\n\t1. [Common] {} (${:.2f})"
                                  "\n\t2. [Rare] {} (${:.2f})"
                                  "\n\t3. [Epic] {} (${:.2f})"
                                  "\n\t4. Complete Purchase".format(groundHog_Name, groundHog_Price, squirrel_Name,
                                                                    squirrel_Price, raven_Name, raven_Price))

            if(strlootBox_Input.isdigit()):
                intlootBox_Input = int(strlootBox_Input)

                if(intlootBox_Input == 1 or intlootBox_Input == 2 or intlootBox_Input == 3):
                    valid_LootBox = True #this will stop the loop for lootbox selection.
                    valid_Amount = False #this will make sure the program doesnt continue after completing purchase.

                    if (intlootBox_Input == 1):
                        selected_LootBox = groundHog_Name
                        selected_LootBox_Price = groundHog_Price

                    elif (intlootBox_Input == 2):
                        selected_LootBox = squirrel_Name
                        selected_LootBox_Price = squirrel_Price

                    elif (intlootBox_Input == 3):
                        selected_LootBox = raven_Name
                        selected_LootBox_Price = raven_Price

                elif(intlootBox_Input == 4 and cart_Valid is False):
                    print("Your cart is empty! Please choose a loot box before you checkout!")

                elif(intlootBox_Input == 4 and cart_Valid is True):
                    complete_Purchase = True
                    valid_LootBox = True
                    total_Cost += amount_GroundHog*groundHog_Price + amount_Squirrel*squirrel_Price + amount_Raven*raven_Price
                    receipt = ""

                    for i in range(3):
                        if(boxAmount_List[i] > 0):
                            receipt+="\n {}x {} (${:.2f})".format(boxAmount_List[i], boxName_List[i], boxPrice_List[i])

                    print("Thanks, {}! Here is your receipt:"
                      "\n---------------------------------".format(userName_Input))

                    print(" "+str.strip(receipt)+
                      "\n---------------------------------"
                      "\nTotal Cost: ${:.2f}"
                      "\nGood luck {}!".format(total_Cost, userName_Input))
                else:
                    print("Error: That was not a valid selection.")
            else:
                print("Error: That was not a valid selection.")

    while (valid_Amount is False):

            stramount_LootBox = input("How many {} (${:.2f}) would you like to purchase?".format(selected_LootBox, selected_LootBox_Price))

            if(stramount_LootBox.isdigit()):

                intamount_LootBox = int(stramount_LootBox)

                if (intamount_LootBox > 0):
                    valid_Amount = True
                    cart_Valid = True
                    if(intlootBox_Input == 1):
                        amount_GroundHog += intamount_LootBox
                        boxAmount_List[0] = amount_GroundHog

                    elif(intlootBox_Input == 2):
                        amount_Squirrel += intamount_LootBox
                        boxAmount_List[1] = amount_Squirrel

                    elif(intlootBox_Input == 3):
                        amount_Raven += intamount_LootBox
                        boxAmount_List[2] = amount_Raven

                else:
                    print("Please enter a valid amount of boxes.")
            else:
                print("Please enter a valid amount of boxes.")

    valid_LootBox = False # this will cause the program to start from the menu again