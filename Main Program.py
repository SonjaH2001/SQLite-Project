# Menu Option 1 program creates a database and a table.
# Menu Option 2 program adds a row of data to the database table.
# Menu Option 3 program updates a row in the database table.
# Menu Option 4 program deletes a row from the database table.
# Menu Option 5 program displays all the rows in the database table.
# Menu Option 6 program display a single row of data based on an input value.
# Create a database table of products with a unique key + 6 more columns
# Use various data types and constraints such as Not Null, default values, etc.
#************Sonja Hayden 2950-90********************************

import sqlite3  # import the library

sqlite_file = 'ThingsNStuff_db.sqlite'  # name of the sqlite database file
table_name1 = 'WIDGETZ'  # name of the table to be created
new_field = 'ITEM_ID'               # Primary Key
new_field_2 = 'NAME'                # name of column
new_field_3 = 'SKU'                 # name of column
new_field_4 = 'PRICE'               # name of column
new_field_5 = 'DESCRIPTION'         # name of column
new_field_6 = 'On_HAND_Quantity'    # name of column
new_field_7 = 'ORDER_Quantity'      # name of column
field_type_int = 'INTEGER'          # name of column
field_type_txt = 'TEXT'             # name of column


def main():
    show_menu()  # call the function to display options to the user


def show_menu(): # provides the user with the options
    while True:
        print() # intentional blank line
        print("Menu options:    ")      # show user their options...
        print("1: CREATE a database and table")
        print("2: ADD a row of data to the table")
        print("3: UPDATE a row of data from the table")
        print("4: DELETE a row of data from the table")
        print("5: SHOW the data from entire table")
        print("6: DISPLAY a single row of data")
        # print("7: DROP TABLE-->BE CAREFUL")   hidden, for testing purposes only
        print("9: QUIT program")
        print()     # intentional blank line
        user_input = input("Please enter the number of your selection: ")   # gets the user choice
        # call the function, from user's choice
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
        elif user_input == "7": # for testing
            drop_table()
        elif user_input == "9":
            print()
            print("Thank you, goodbye")
            break  # ends the program
        else:
            print() # intentional blank line
            print("Please make a valid selection, jackass.") # prompts user for valid input
            print() # intentional blank line
            # show_menu() nope. It loops back up to the top, did a while loop instead.


def create_database():
    print("--->creating the database<---")  # for testing
    # connecting to the database file
    conn = sqlite3.connect(sqlite_file)
    c = conn.cursor()
    # cite http://www.sqlitetutorial.net/sqlite-create-table/
    # db = conn.execute('''CREATE TABLE COMPANY
    #     (ID INT PRIMARY KEY   NOT NULL,
    #     NAME    TEXT          NOT NULL,
    #     AGE     INT           NOT NULL,
    #     ADDRESS     VARCHAR(50),
    #     SALARY       REAL);''')
    # print(db) #test to see the DB object
    # worked but I don't understand it

        # creating table with columns, put in a variable to make debugging easier
    create_table_sql = (
        'CREATE TABLE If NOT EXISTS {tn} ('
        ' {nf} {ft} PRIMARY KEY AUTOINCREMENT ,'
        ' {nf2} {ft_T} NOT NULL , '
        ' {nf3} {ft_T} NOT NULL ,'
        ' {nf4} {ft} NOT NULL ,'
        ' {nf5} {ft_T} NOT NULL ,'
        ' {nf6} {ft} NOT NULL ,'
        ' {nf7} {ft} NOT NULL '
        ')  '
    ).format(tn=table_name1, nf=new_field, nf2=new_field_2, nf3=new_field_3, nf4=new_field_4, nf5=new_field_5, nf6=new_field_6, nf7=new_field_7, ft=field_type_int, ft_T=field_type_txt)

    c.execute(create_table_sql) #pass the variable instead of putting the code into execute statement
    # c.execute('CREATE TABLE IF NOT EXISTS {tn} ({nf} {ft} PRIMARY KEY,\
    #         {nf2} {ft_T}, {nf3} {ft}, {nf4} {ft_T}, {nf5} {ft}, {nf6} {ft}, {nf7} {ft})'\
        #commit changes and close the DB file connection
    conn.commit()
    conn.close()


def add_row():
    print("----->adding a row<-----")  # for testing
        # connecting to the database file
    conn = sqlite3.connect(sqlite_file)
    c = conn.cursor()

    try: # help from Mason and http://www.sqlitetutorial.net/  Can't use "?" I guess.
        c.execute('INSERT INTO WIDGETZ ("NAME", "SKU", "PRICE", "DESCRIPTION", "On_HAND_Quantity", "ORDER_Quantity") VALUES ("name", "sku", "int", "desc", "int", "int")')
        # c.execute("INSERT INTO table_name1 (new_field, new_field_2, new_field_3, new_field_4, new_field_5, new_field_6, new_field_7)\
        #     VALUES (123456, 'test 2', 'test 3', 'test 4', 'test 5', 'test 6', 'test 7')")
            # format(tn=table_name, idf=id_column, cn=column_name))
        # c.execute("INSERT INTO {tn} ({idf}, {cn, }) VALUES (123456, 'test 2', 'test 3', 'test 4', 'test 5', 'test 6', 'test 7')".\
        #           format(tn=table_name, idf=id_column, cn=column_name))
    except sqlite3.IntegrityError:
        print('ERROR: ID already exists in PRIMARY KEY column {}'.format())

         # commit changes and close the DB file connection
    conn.commit()
    conn.close()


def update_row():
    print("----->updating a row<-----") # for testing
    # connecting to the database file
    conn = sqlite3.connect(sqlite_file)
    c = conn.cursor()

    row_query_update = int(input("Enter the Item Id number for the row to update: "))
    if row_query_update > 0:
        # print("data type working")#testing
        fetch_row_sql = "SELECT * FROM " + table_name1 + " WHERE Item_id = " + str(row_query_update)
        c.execute(fetch_row_sql)  # put in a variable to make debugging easier
        for row in c:  # c= cursor Value
            print("ID number: ", row[0])  # Displays rows by position
            print("Item Name: ", row[1])
            print("Item SKU: ", row[2])
            print("Item Description: ", row[3])
            print("Item Price: ", row[4])
            print("Quantity On-hand: ", row[5])
            print("Quantity Ordered: ", row[6])

    new_info = input("Whats the new name/ testing: ")

    change_row_info = "UPDATE " + table_name1 + " SET " + new_field_2 + new_info + " WHERE " + new_field == row_query_update
    print(change_row_info)

    #
    # else:
    #     print("Please enter a valid id number: ")
    # c.execute('UPDATE WIDGETZ SET NAME = "Smith", SKU = 666, PRICE = 99,DESCRIPTION = "Squeezy", On_HAND_Quantity = 0, ORDER_Quantity = 8862 WHERE ITEM_ID = 2')

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
    conn.commit()
    conn.close()


def delete_row():
    print("----->deleting a row<-----")  # for testing
    # Connecting to the database file
    conn = sqlite3.connect(sqlite_file)
    c = conn.cursor()
    # deletes this row, TODO have user search for a row to delete
    c.execute('DELETE FROM WIDGETZ WHERE ITEM_ID = 2')

    # commit changes and close the DB file connection
    conn.commit()
    conn.close()


def show_all_rows():
    print("----->here is the " + table_name1 +  " table<-----")# for testing
    # Connecting to the database file
    conn = sqlite3.connect(sqlite_file)
    c = conn.cursor()

    #  NEED to add row headers!!!!!!!!!!
    table_query = input("Enter the name of the requested table to view: (HINT!! type WIDGETZ) " )
    if table_query == table_name1:
        fetch_allRows_sql = "SELECT * FROM " + table_name1
        c.execute(fetch_allRows_sql)  ##put in a variable to make debugging easier
        for row in c:  # c= cursor Value
            print("ID number: ", row[0])
            print("Item Name: ", row[1])
            print("Item SKU: ", row[2])
            print("Item Description: ", row[3])
            print("Item Price: ", row[4])
            print("Quantity On-hand: ", row[5])
            print("Quantity Ordered: ", row[6])
            print() # intentional blank line
        print("YAY, it works")  # for testing.  and motivation.
    else:
        print("Oh so sad. Not working")
    # close the DB file connection
    conn.close()


def show_single_row():
    print("----->here is the row you requested<-----")  # for testing
    # connecting to the database file
    conn = sqlite3.connect(sqlite_file)
    c = conn.cursor()

    row_query = int(input("Enter the Item Id number: (hint, start at 1) "))
    if row_query > 0:
        # print("data type working")#testing
        fetch_row_sql = "SELECT * FROM " + table_name1 + " WHERE Item_id = " + str(row_query)
        c.execute(fetch_row_sql) # put in a variable to make debugging easier
        for row in c: # c= cursor Value
            print("ID number: ", row[0])        # Displays rows by position
            print("Item Name: ", row[1])
            print("Item SKU: ", row[2])
            print("Item Description: ", row[3])
            print("Item Price: ", row[4])
            print("Quantity On-hand: ", row[5])
            print("Quantity Ordered: ", row[6])
            print() # intentional blank line
        print("YAY, it works") # for testing.  and motivation.
    # close the DB file connection
    conn.close()


def drop_table(): # for testing
    conn = sqlite3.connect(sqlite_file)
    c = conn.cursor()
    # drops the table, #!TO DO get user input, also lots of "are you sure" warnings
    c.execute('DROP TABLE ' + table_name1)
    print("Table " + table_name1 + " is gone. forever.")
    conn.commit()
    conn.close()

main() # calls the main program



