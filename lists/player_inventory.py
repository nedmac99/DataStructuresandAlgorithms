#Create a list to represent a player’s inventory. Practice adding, removing, and sorting items, counting duplicates, and checking if certain items exist
#Gym log of people entering and leaving the building and checking if they are still in the list/gym

player_inventory = []

sword = "sword"
shield = "shield"
knife = "knife"
key = "key"


sword_response = input("Found an sword, do you want to add sword to the inventory?(y/n)")

print(player_inventory)

if sword_response == "y":
    player_inventory.append(sword)
    print("sword was added")
    print(player_inventory)
else:
    print("Nothing was added")



if len(player_inventory) >= 1:
    removal = input("Do you want to remove the sword?(y/n)")
    if removal == "y":
        player_inventory.remove(sword)
        print(player_inventory)
    else:
        print("Didn't remove anything")

