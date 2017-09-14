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
new_field_2 = 'Column 2'
new_field_3 = 'Column 3'
new_field_4 = 'Column 4'
new_field_5 = 'Column 5'
new_field_6 = 'Column 6'
new_field_7 = 'Column 7'
field_type_int = 'INTEGER'
field_type_txt = 'TEXT'
# id_column = 'first_field'  # name of the field to be created
# new_column_2 = '2nd_field'# name of the field to be created
# new_column_3 = '3rd_field'# name of the field to be created
# new_column_4 = '4th_field'# name of the field to be created
# new_column_5 = '5th_field'# name of the field to be created
# new_column_6 = '6th_field'# name of the field to be created
# new_column_7 = '7th_field'# name of the field to be created
# field_type = 'TEXT' #column data type
# default_val = 'add content' #sets default value for new rows

def main():
    show_menu()  # call the function to display options to the user

def show_menu(): # provides the user with the options
    while True:
        print() #intentional blank line
        print("Menu options:    ")
        print("1: CREATE a database and table")
        print("2: ADD a row of data to the table")
        print("3: UPDATE a row of data from the table")
        print("4: DELETE a row of data from the table")
        print("5: SHOW the data from entire table")
        print("6: DISPLAY a single row of data")
        print("8: add a new COLUMN to the table")
        # print("7: DROP TABLE-->BE CAREFUL")
        print("9: QUIT program")
        print() #intentional blank line
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
        #     drop_table()
            view_column_names()
        elif user_input == "8":
            add_new_column()
        elif user_input == "9":
            print()
            print("Thank you, goodbye")
            break  # ends the program
        else:
            print()#intentional blank line
            print("please make a valid selection, jackass.")#prompts user for valid input
            print()#intentional blank line
            # show_menu() nope. It loops back up to the top, did a while loop instead.

def create_database():
    print("--->creating the database")  # for testing
        # connecting to the database file
    conn = sqlite3.connect(sqlite_file)
    c = conn.cursor()
        #creating table with 1 column and PK. cite: Mason
    c.execute('CREATE TABLE IF NOT EXISTS {tn} ({nf} {ft} PRIMARY KEY )'\
                  .format(tn=table_name1, nf=new_field, ft=field_type_int))
    print("Table: "+table_name1, "\t" "Columns: "+new_field, "\t" "Data type: "+field_type_int) #test print
        #commit changes and close the DB file connection
    conn.commit()
    conn.close()

def add_row():
    print("----->adding a row")  # for testing

        # connecting to the database file
#     conn = sqlite3.connect(sqlite_file)
#     c = conn.cursor()
#
# #         # commit changes and close the DB file connection
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

def add_new_column():
    #print("----->you have a new column!!")# for testing
    #connecting to db file
    conn = sqlite3.connect(sqlite_file)
    c = conn.cursor()
    #add new column
    c.execute(("ALTER TABLE {tn} ADD COLUMN '{nf}' {ft}" \
              .format(tn=table_name1, nf=new_field_2, ft=field_type_txt)))
    print(("success. new COLUMN added"))
    # #--->HOW TO add new_column_3, etc??????????????????

def view_column_names(): #for testing, might be useful in a query
    #from https://github.com/rasbt/python_reference/blob/master/tutorials/sqlite3_howto/code/get_columnnames.py
    conn = sqlite3.connect(sqlite_file)
    c = conn.cursor()
    c.execute('PRAGMA TABLE_INFO ({})'.format(table_name1))
    names = [tup[1] for tup in c.fetchall()]
    print(names)
    conn.close()

def drop_table(): #for testing
    conn = sqlite3.connect(sqlite_file)
    c = conn.cursor()
    # c.execute('DROP TABLE {tn} )({nf} {ft})'\
    #           .format(tn=table_name1, nf=new_field, ft=field_type))
    c.execute('DROP TABLE {tn}' \
              .format(tn=table_name1))
    print("your database is gone. forever.")
    conn.close()

main()#calls the main program



