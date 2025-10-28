# Shopping List App

import os

FILENAME = "shopping_list.txt"

# Step 1: Load persisted shopping list if exists
shopping_list = []
if os.path.exists(FILENAME):
    with open(FILENAME, "r", encoding="utf-8") as f:
        shopping_list = [line.strip() for line in f.readlines() if line.strip()]

# Step 2: Define the main menu
def show_menu():
    print("\n--- Shopping List Menu ---")
    print("1. View shopping list")
    print("2. Add an item")
    print("3. Remove an item")
    print("4. Modify an item")
    print("5. Clear list")
    print("6. Save and Exit")

# Step 3: Main Program Loop
while True:
    show_menu()
    choice = input("Enter your choice (1-6): ")
    if choice == "1":
        print("\n--- Shopping List ---")
        if not shopping_list:
            print("Your shopping list is empty.")
        else:
            for index, item in enumerate(shopping_list):
                print(f"{index + 1}. {item}")
    elif choice == "2":
        item = input("Enter the item to add: ")
        shopping_list.append(item)
        print(f"{item} has been added to the shopping list.")
    elif choice == "3":
        item = input("Enter the item to remove: ")
        if item in shopping_list:
            shopping_list.remove(item)
            print(f"{item} has been removed from the shopping list.")
        else:
            print(f"{item} is not in the shopping list.")
    elif choice == "4":
        if not shopping_list:
            print("The shopping list is empty. Nothing to modify.")
            continue
        print("\n--- Shopping List ---")
        for index, item in enumerate(shopping_list):
            print(f"{index + 1}. {item}")
        try:
            pos = int(input("Which item do you want to modify? (Enter number): "))
            if 1 <= pos <= len(shopping_list):
                new_item = input(f"Enter the new value for '{shopping_list[pos-1]}': ")
                shopping_list[pos-1] = new_item
                print("Item updated.")
            else:
                print("Invalid position.")
        except ValueError:
            print("Enter a valid number.")
    elif choice == "5":
        shopping_list.clear()
        print("The shopping list has been cleared.")
    elif choice == "6":
        with open(FILENAME, "w", encoding="utf-8") as f:
            for item in shopping_list:
                f.write(item + "\n")
        print("List saved! Goodbye! Happy Shopping!")
        break
    else:
        print("Invalid choice. Please try again.")
