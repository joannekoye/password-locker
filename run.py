#!/usr/bin/env python3.6

import random
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

            print('Platform on which existing account is based: (e.g. Instagram, Twitter, etc.)')
            platform = input()

            print ("First name registered on existing account:")
            firstname = input()

            print ("Last name registered on existing account:")
            lastname = input()

            print('Username registered on existing account:')
            username = input()

            print('Password registered on existing account: (Your password is safe with us)')
            password = input()

            save_user(create_user(platform, firstname, lastname, username, password))
            print ('\n')
            print(f"New Credentials for {platform} ( {username} ), created")
            print ('\n')


        elif short_code == 'cn':
            print("-"*11)
            print("New Account")
            print("-"*11)

            print('Platform on which new account will be based: (e.g. Instagram, Twitter, etc.) ')
            platform = input()

            print ("First name:")
            firstname = input()

            print ("Last name:")
            lastname = input()

            print('Prefered username:')
            username = input()

            print('Password Generation for new account:')
            print('_'*20)
            print('\n')

            while True:
                print('Use the following short codes to tell us if you would like to set your own password or if you would like a system generated password: own - your own password, sys - system generated password')
            
                passcode = input().lower()

                if passcode == 'own':
                    print('Kindly enter your prefered password: (Your password is safe with us)')
                    password = input()

                elif passcode == 'sys':
                    password = random.randint(34567,98756)

                else:
                    print("I really didn't get that. Please use the short codes")
            

            save_user(create_user(platform, firstname, lastname, username, password))


        elif short_code == 'del':

            