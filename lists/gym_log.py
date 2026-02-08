#Gym log of people entering and leaving the building and checking if they are still on the list/in the gym
#Add sorting to make finding someone easier in larger lists
#Implement Queue sorting method. First in, First out

import sys

gym_log = []

def main():
    while True:
        selection = input("Enter selection: \n1.Add\n2.Remove\n3.View Log(Alphabetically)\n4.Exit\n")

        if selection == str(1):
            print()
            name = input("Name: ").title()
            add_person(name)
            print(f"\n{name} was added!\n")
        
        elif selection == str(2):
            print()
            name = input("\nName: \n").title()
            if name in gym_log:
                remove_name(f"{name}")
                print(f"\n{name} was removed!\n")
            else:
                print("\nName not found in log\n")
        
        elif selection == str(3):
            if not gym_log:
                print("\nNo one is in the log\n")
            else:    
                print(f"\n{sorted(gym_log)}\n")

        elif selection == str(4):
            sys.exit("\nThanks for using my log!\n")
        
        else:
            print("\nInvalid input\n")



def add_person(name):
    return gym_log.append(name)

def remove_name(name):
    return gym_log.remove(name)

def view_list():
    print(gym_log)

if __name__ == "__main__":
    main()