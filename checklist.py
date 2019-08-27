import sys
import os
import random

# USING TERMCOLOR MODULE FOR COLORED TEXT: https://pypi.org/project/termcolor/
from termcolor import colored

checklist = list()

# RANDOM COLOR SELECTOR
def color_selector():
    color_list = ['grey', 'red', 'green', 'yellow', 'blue', 'magenta', 'cyan']
    return random.choice(color_list)

# CREATE
def create(item):
    colored_item = colored(item, color_selector())
    checklist.append(colored_item)

# READ
def read(index):
    try:
        item = checklist[index]
        return item
    except IndexError:
        return("Index does not exist.")

# UPDATE
def update(index, item):
    try:
        checklist[index] = colored(item, color_selector())
        return("Item at index " + str(index) + " updated to " + item)
    except IndexError:
        return("Index does not exist.")

# DESTROY
def destroy(index):
    try:
        checklist.pop(index)
        return("Item at index " + str(index) + " removed.")
    except IndexError:
        return("Index does not exist.")

# MARK COMPLETED
def mark_completed(index):
    item = checklist[index]

    if item[0] != "√":
        checklist[index] = "√ " + checklist[index]
        return("Item marked as complete.")
    else:
        return("item is already marked as complete.")

# MARK UNCOMPLETED
def mark_uncompleted(index):
    item = checklist[index]
    
    if item[0] == "√":
        incompleted_item = item.replace("√ ","")
        checklist[index] = incompleted_item
        return("Item marked as incomplete.")
    else:
        return("Item is already marked as incomplete.")

# LIST ALL ITEMS
def list_all_items():
    index = 0
    for list_item in checklist:
        print("{} {}".format(index, list_item))
        index += 1

# SELECT
def select(function_code):
    # Create item
    if function_code == "a":
        input_item = user_input("Input item: ")
        create(input_item)

    # Read item
    elif function_code == "r":
        item_index = int(user_input("Index Number: "))

        # Remember that item_index must actually exist or our program will crash.
        print(read(item_index))

    # Print all items
    elif function_code == "l":
        list_all_items()

    # Update item
    elif function_code == "u":
        item_index = int(user_input("Index Number: "))
        update_item = user_input("Input item: ")
        print(update(item_index, update_item))

    # Destroy item
    elif function_code == "d":
        item_index = int(user_input("Index Number: "))
        print(destroy(item_index))
    
    # Mark Complete/Incomplete
    elif function_code == "m":
        complete_incomplete = user_input("Mark as Complete or Incomplete?(Enter C/I): ").lower()

        if complete_incomplete == "c":
            item_index = int(user_input("Index Number: "))
            print(mark_completed(item_index))
        
        elif complete_incomplete == "i":
            item_index = int(user_input("Index Number: "))
            print(mark_uncompleted(item_index))
        
        else:
            print("Invalid Option")

    elif function_code == "q":
        return False

    # Catch all
    else:
        print("Unknown Option")
    return True

# USER INPUT
def user_input(prompt):
    user_input = input(prompt)
    return user_input

# TESTING FUNCTIONS
def test():
    '''
    create("purple sox")
    create("red cloak")

    print(read(0))
    print(read(1))

    update(0, "purple socks")

    destroy(1)

    print(read(0))
    mark_completed(0)

    list_all_items()

    select("C")
    list_all_items()

    select("R")
    list_all_items()

    select("P")
    list_all_items()
    '''

# RUN TESTS
test()

running = True
while running:
    os.system("clear")
    selection = user_input(
        "Press A to Add to list, R to Read from list, L to Display list, U to Update item, D to Destroy item, M to Mark Complete/Incomplete, and Q to quit: ")
    selection_both_cases = selection.lower()
    running = select(selection_both_cases)
    input("Press Enter to Continue...")