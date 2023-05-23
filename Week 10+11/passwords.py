import pickle
import sys
import time
# import pwnedpasswords
'''
Author: David Thomsen
Class: CSI-160
Assignment: Password Manager and Cipher
'''


# The password list - We start with it populated for testing purposes
entries = {'yahoo': {'username': 'johndoe', 'password': 'cus#u%S tu', 'url': 'https://www.yahoo.com'},
           'google': {'username': 'johndoe', 'password': '`q$$( #tABCD^ %fu#*W  t', 'url': 'https://www.google.com'}}

# The password file name to store the data to

password_file_name = "PasswordFile.pickle"

# The encryption key for the caesar cypher


def make_key():
    encryption_key = int(input("please enter an encryption key:"))
    return encryption_key


encryption_key = make_key()


menu_text = """
What would you like to do:
1. Open password file
2. Add an entry
3. Lookup an entry
4. Save password file
5. Quit program
6. Print dictionary for testing
7. Delete an entry
8. Edit an entry
9. View Key
10. Change Key
Please enter a number (1-10)"""


def password_encrypt(unencrypted_message, key):

    result_string = ''
    min_limit = 32
    max_limit = 126

    for character in unencrypted_message:
        value = ord(character) - min_limit + key
        value = value % (max_limit - min_limit + 1)
        value = value + min_limit
        result_string = result_string + chr(value)
    return result_string


def password_decrypt(encrypted_message, key):

    return password_encrypt(encrypted_message, -key)


def load_password_file():

    global entries, encryption_key
    entries, encryption_key = pickle.load(open(password_file_name, "rb"))
    time.sleep(2)


def save_password_file():

    pickle.dump((entries, encryption_key), open(password_file_name, "wb"))
    time.sleep(2)


def add_entry():

    david = {'username': '','password': '', 'url': ''}

    dtitle = input("Enter a title: ")

    duser = input("Enter a username: ")

    dpass = input("Enter a password: ")

    durl = input("Enter a url: ")

    david['username'] = duser

    david['password'] = dpass

    david['url'] = durl

    password_encrypt(david['password'], encryption_key)

    entries[dtitle] = david


def print_entry():

    print("Which entry do you want to lookup?")

    for key in entries:
        print(key)
    entry = input('Entry name: ')

    print('Username: ' + entries[entry]['username'])
    password_decrypt(entries[entry]['password'], encryption_key)
    print('Password: ' + entries[entry]['password'])
    print('Url: ' + entries[entry]['url'])
    input("Press enter when done")

def delete_entry():

    for key in entries:
        print(key)

    delselect = input('Select Password to delete: ')

    if delselect in entries:
        entries.pop(delselect)
        print("Deleted successfully")
        time.sleep(2)

    for key in entries:
        print(key)


def edit_entry():

    for key in entries:
        print(key)

    editsel = input("Enter a entry to be edited")

    if editsel in entries:
        uchange = input("Enter a new username: ")

        upass = input("Enter a new password: ")

        newurl = input("Enter a new url: ")


        entries[editsel]['username'] = uchange

        entries[editsel]['password'] = upass

        password_encrypt(entries[editsel]['password'], encryption_key)

        entries[editsel]['url'] = newurl


def end_program():
    sys.exit()


def print_dictionary():
    print(entries)
    time.sleep(2)


def view_key():
    print(encryption_key)
    time.sleep(1)


def edit_key():
    make_key()
    print("Key Changed")
    time.sleep(1)


menu_dict = {
         '1': load_password_file,
         '2': add_entry,
         '3': print_entry,
         '4': save_password_file,
         '5': end_program,
         '6': print_dictionary,
         '7': delete_entry,
         '8': edit_entry,
         '9': view_key,
         '10': edit_key
    }


while True:
    user_choice = input(menu_text)
    if user_choice in menu_dict and menu_dict[user_choice]:
        menu_dict[user_choice]()
    else:
        print('Not valid entry')
        time.sleep(2)
