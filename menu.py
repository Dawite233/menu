"""
A menu - you need to add the database and fill in the functions. 
"""
import sqlite3


db = 'Record_name.sqlite'

def main():
    menu_text = """
    1. Display all records
    2. Search by name
    3. Add new record
    4. Edit existing record
    5. Delete record 
    6. Quit
    """

    while True:
        print(menu_text)
        choice = input('Enter your choice: ')
        if choice == '1':
            display_all_records()
        elif choice == '2':
            search_by_name()
        elif choice == '3':
            add_new_record()
        elif choice == '4':
            edit_existing_record()
        elif choice == '5':
            delete_record()
        elif choice == '6':
            break
        else:
            print('Not a valid selection, please try again')


def display_all_records():
    print('todo display all records')
    #with sqlite3.connect('Record_name.sqlite') as conn:
    conn = sqlite3.connect(db)
    products = conn.execute('SELECT * FROM records')
    print('The entired products')

    for row_products in products:
        print(row_products[1])

    conn.close()
        


def search_by_name():
    print('todo ask user for a name, and print the matching record if found. What should the program do if the name is not found?')


def add_new_record():
    print
    ('todo add new record. What if user wants to add a record that already exists?')
    new_name = input('Enter Record holder name?')
    new_country = input('Enter record holder country name')
    new_number_catchs = int(input('Enter record holder number od catches'))
    
    with sqlite3.connect(db) as conn:
        conn.execute(f'INSERT INTO records VALUES (?, ?, ?)', (new_name, new_country, new_number_catchs))
        conn.execute(f'INSERT INTO records VALUES (?, ?, ?)', (new_name, new_country, new_number_catchs))
        conn.execute(f'INSERT INTO records VALUES (?, ?, ?)', (new_name, new_country, new_number_catchs))

    conn.close()


def edit_existing_record():
    print('todo edit existing record. What if user wants to edit record that does not exist?') 
    Editing_new_namenew_name = ' wool hat'
    Editing_new_country = 'Africa'
    Editing_new_number_catchs = 1000

    with sqlite3.connect(db) as conn:
        conn.execute('UPDATE products SET name = ? WHERE id = ? ', (update_product, update_id ))
   
    conn.close()


def delete_record():
    print('todo delete existing record. What if user wants to delete record that does not exist?') 
    with sqlite3.connect(db) as conn:
     conn.execute('DELETE from RECORDS WHERE name = ?', (new_name, new_country, new_number_catchs))
    
    conn.close() 


if __name__ == '__main__':
    main()