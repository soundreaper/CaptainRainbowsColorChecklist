checklist = list()

# CREATE
def create(item):
    checklist.append(item)

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
        checklist[index] = item
    except IndexError:
        return("Index does not exist.")

# DESTROY
def destroy(index):
    try:
        checklist.pop(index)
    except IndexError:
        return("Index does not exist.")

# MARK COMPLETED
def mark_completed(index):
    checklist[index] = "√" + checklist[index]

# LIST ALL ITEMS
def list_all_items():
    index = 0
    for list_item in checklist:
        print("{} {}".format(index, list_item))
        index += 1

# SELECT
def select(function_code):
    # Create item
    if function_code == "C":
        input_item = user_input("Input item: ")
        create(input_item)

    # Read item
    elif function_code == "R":
        item_index = int(user_input("Index Number?: "))

        # Remember that item_index must actually exist or our program will crash.
        read(item_index)

    # Print all items
    elif function_code == "P":
        list_all_items()

    # Catch all
    else:
        print("Unknown Option")

# USER INPUT
def user_input(prompt):
    user_input = input(prompt)
    return user_input

# TESTING FUNCTIONS
def test():
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

# RUN TESTS
test()