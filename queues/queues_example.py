#Queue Example
#Implementing a basic queue where people can join and leave in a first-in, first-out manner
#Maybe alter it so it represents a spotify Queue. Maybe use deque for this?

import sys

queue = []

def main():
    while True:
        selection = input("Enter selection: \n1.Join Queue\n2.Leave Queue\n3.View Queue\n4.Exit\n")

        if selection == str(1):
            print()
            name = input("Name: ").title()
            join_queue(name)
            print(f"\n{name} joined the queue!\n")
        
        elif selection == str(2):
            print()
            if queue:
                name = leave_queue()
                print(f"\n{name} has left the queue!\n")
            else:
                print("\nThe queue is empty!\n")
        
        elif selection == str(3):
            if not queue:
                print("\nThe queue is empty!\n")
            else:    
                view_queue()

        elif selection == str(4):
            sys.exit("\nThanks for using the queue system!\n")
        
        else:
            print("\nInvalid input\n")


def join_queue(name):
    return queue.append(name)

def leave_queue():
    return queue.pop(0)

def view_queue():
    print(f"\nCurrent Queue: {queue}\n")

if __name__ == "__main__":
    main()
