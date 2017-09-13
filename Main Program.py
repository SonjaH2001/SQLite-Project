# Menu Option 1 program creates a database and a table.
# Menu Option 2 program adds a row of data to the database table.
# Menu Option 3 program updates a row in the database table.
# Menu Option 4 program deletes a row from the database table.
# Menu Option 5 program displays all the rows in the database table.
# Menu Option 6 program display a single row of data based on an input value.
# Create a database table of products with a unique key
# and 6 additional of product data columns.
# Use various data types and constraints such as Not Null, default values, etc.

import sqlite3  # import the library

sqlite_file = 'ThingsNStuff_db.sqlite'  # name of the sqlite database file
table_name1 = 'TNS_table1'  # name of the table to be created
new_field = 'TNS_1st_column'
field_type = 'INTEGER'
# id_column = 'first_field'  # name of the field to be created
# new_column_2 = '2nd_field'# name of the field to be created
# new_column_3 = '3rd_field'# name of the field to be created
# new_column_4 = '4th_field'# name of the field to be created
# new_column_5 = '5th_field'# name of the field to be created
# new_column_6 = '6th_field'# name of the field to be created
# field_type = 'TEXT' #column data type
# default_val = 'add content' #sets default value for new rows

def main():
    show_menu()  # call the function to display options to the user

def show_menu(): # provides the user with the options
    while True:
        print("Menu options:    ")
        print("1: CREATE a database and table")
        print("2: ADD a row of data to the table")
        print("3: UPDATE a row of data from the table")
        print("4: DELETE a row of data from the table")
        print("5: SHOW the data from entire table")
        print("6: DISPLAY a single row of data")
        print("7: DROP TABLE-->BE CAREFUL")
        print("9: QUIT program")
        print() #blank space
        user_input = input("Please enter the number of your selection: ")# gets the user choice
        #call the function for user's choice
        if user_input == "1":
            create_database()
        elif user_input == "2":
            add_row()
        elif user_input == "3":
            update_row()
        elif user_input == "4":
            delete_row()
        elif user_input == "5":
            show_all_rows()
        elif user_input == "6":
            show_single_row()
        elif user_input == "7":
            drop_table()
        elif user_input == "9":
            print()
            print("Thank you, goodbye")
            break  # ends the program
        else:
            print()#blank space
            print("please make a valid selection, jackass.")#prompts user for valid input
            print()#blank space
            # show_menu() nope. It loops back up to the top, did a while loop instead.

def drop_table():
    conn = sqlite3.connect(sqlite_file)
    c = conn.cursor()
    # c.execute('DROP TABLE {tn} )({nf} {ft})'\
    #           .format(tn=table_name1, nf=new_field, ft=field_type))
    c.execute('DROP TABLE {tn}' \
              .format(tn=table_name1))
    print("your database is gone. forever.")

def create_database():
    # print("--->creating the database")  # for testing

        # connecting to the database file
    conn = sqlite3.connect(sqlite_file)
    c = conn.cursor()
        #creating table with 1 column
    c.execute('CREATE TABLE IF NOT EXISTS {tn} ({nf} {ft})'\
              .format(tn=table_name1, nf=new_field, ft=field_type))
    print("successful database table") #test print
        #commit changes and close the DB file connection
    conn.commit()
    conn.close()

def add_row():
    print("----->adding a row")  # for testing

        # connecting to the database file
#     conn = sqlite3.connect(sqlite_file)
#     c = conn.cursor()
#         #add the new column
# #--->HOW TO add new_column_3, etc??????????????????
#     c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ft}"\
#               .format(tn=table_name1, cn=new_column_2, ft=field_type))
#         # commit changes and close the DB file connection
#     conn.commit()
#     conn.close()

def update_row():
    print("----->updating a row")# for testing

    # connecting to the database file
    # conn = sqlite3.connect(sqlite_file)
    # c = conn.cursor()
    # try: #inserts an ID w/specific val in a 3rd (new) column
    #     c.execute("INSERT INTO {tn} ({idf}, {cn}) VALUES (123456, 'test')".\
    #               format(tn=table_name1, idf=id_column, cn=new_column_3))
    # except sqlite3.IntegrityError:
    #     print("ERROR".format(id_column))
    #     #tries to insert an ID (if it doesn't exist yet) w/spec val into a new column
    # c.execute("INSERT OR IGNORE INTO {tn} ({idf}, {cn}) VALUES (123456, 'test')".\
    #     format(tn=table_name1, idf=id_column, cn=new_column_3))
    #     #updates the newly inserted or pre-esisting entry
    # c.execute("UPDATE {tn} SET {cn}= ('Hey you guys!') WHERE {idf}=(123456)".\
    #           format(tn=table_name1, cn=new_column_3, idf=id_column))
    # # commit changes and close the DB file connection
    # conn.commit()
    # conn.close()

def delete_row():
    print("----->delete a row")  # for testing

def show_all_rows():
    print("----->here is the entire table")# for testing

def show_single_row():
    print("----->here is the row you requested")# for testing



main()#calls the main program



