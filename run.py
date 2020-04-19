#!/usr/bin/env python3.6

from user import User

def create_user(platform, fname, lname, uname, pword):
    '''
    Function to create a new user
    '''
    new_user = User(platform, fname, lname, uname, pword)
    return new_user


def save_user(user):
    '''
    Function to save user
    '''
    user.save_user()


def del_user(user):
    '''
    Function to delete a user
    '''
    user.delete_user()


def display_users():
    '''
    Function that returns all saved users
    '''
    return User.display_users()


def main():
    print('Hello! Welcome to Password Locker. What is your name?')
    name = input()

    print(f'Hi, {name}. What woul you like to do today?')
    print('\n')

    while True:
        print('Use the following short codes to tell us how to help you: ce - collect existing credentials, cn - create new account on a new platform and have credentials saved here, del - delete existing credentials, ex - exit the application')
        short_code = input().lower()

        if short_code == 'ce':
            print("-"*16)
            print("Existing Account")
            print("-"*16)

            print('Platform on which existing account is based: (e.g. Instagram, Twitter, etc.')
            platform = input()

            print ("First name registered on existing account:")
            firstname = input()

            print ("Last name registered on existing account:")
            lastname = input()

            print('Username registered on existing account:')
            username = input()

            print('Password registered on existing account: (Your password is safe with us')
            password = input()

            save_user(create_user(platform, firstname, lastname, username, password))
            print ('\n')
            print(f"New Credentials for {platform} ( {username} ), created")
            print ('\n')


        elif short_code == 'cn':
            print("-"*11)
            print("New Account")
            print("-"*11)

            print
