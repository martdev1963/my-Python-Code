import os
import random

shopping_list = ["apples"]


def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def help():
    clear()
    print("What should we pick up at the store? ")
    print("""
ENTER 'DONE' to stop adding items.
ENTER 'HELP' for this help.
ENTER 'SHOW' to see your current list.
""")


def add_to_list(item):
    show_list()
    if len(shopping_list):
        position = input("Where   should I add {}?\n"
                         "Press ENTER to add to the end of the list\n"
                         "> ".format(item))
    else:
        position = 0

    try:
        position = abs(int(position))
    except ValueError:
        position = None
    if position is not None:
        shopping_list.insert(position - 1, item)
    else:
        shopping_list.append(new_item)

    show_list()


def show_list():
    clear()

    print("Here's your list:")

    index = 1
    for item in shopping_list:
        print("{}. {}".format(index, item))
        index += 1

        print("-" * 10)


help()

while True:
    new_item = input("> ")

    if new_item.upper() == 'DONE' or new_item.upper() == 'QUIT':
        break
    elif new_item == 'HELP':
        show_help()
        continue
    elif new_item == 'SHOW':
        show_list()
        continue
    else:
        add_to_list(new_item)

show_list()




