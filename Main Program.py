# Menu Option 1 program creates a database and a table.
# Menu Option 2 program adds a row of data to the database table.
# Menu Option 3 program updates a row in the database table.
# Menu Option 4 program deletes a row from the database table.
# Menu Option 5 program displays all the rows in the database table.
# Menu Option 6 program display a single row of data based on an input value.
# Create a database table of products with a unique key
# and 6 additional of product data columns.
# Use various data types and constraints such as Not Null, default values, etc.

#testing github

import sqlite3  # import the library

sqlite_file = 'Products_db.sqlite'  # name of the sqlite database file
table_name1 = 'Produce_table1'  # name of the table to be created
new_field = 'Lettuce'  # name of the field to be created


def main():
    show_menu()  # call the function to display options to the user
    # main()


def create_database():
    print("--->creating the database")  # for testing


def add_row():
    print("----->adding a row")  # for testing


def delete_row():
    print("----->delete a row")  # for testing


def show_menu():
    while True:
        print("Menu options:    ")
        print("1: create database and table")
        print("2: add a row of data to the table")
        print("3: delete a row of data from the table")
        print("9: QUIT program")
        user_input = input("Please enter the number of your selection: ")
        if user_input == "1":
            create_database()
        elif user_input == "2":
            add_row()
        elif user_input == "3":
            delete_row()
        elif user_input == "9":
            print()
            print("Thank you, goodbye")
            break  # ends the program
        else:
            print()
            print("please make a valid selection, jackass.")
            print()
            # show_menu() nope. It loops back up to the top, did while loop instead.


main()



