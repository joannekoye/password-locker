#!/usr/bin/env python3.6

import random
from user import User
from credentials import Credentials

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


def del_user(ind):
    '''
    Function to delete a user
    '''
    Credentials.delete_user(ind)


def display_users():
    '''
    Function that returns all saved users
    '''
    return Credentials.display_users()


def find_credentials(platform, username):
    '''
    Function that finds user credentials
    '''
    return Credentials.find_credential(platform,username)
    

def find_credentials_index(platform, username):
    '''
    Function that finds user credentials index
    '''
    return Credentials.find_credential_index(platform,username)

def main():
    print('Hello! Welcome to Password Locker. What is your name?')
    name = input()

    print(f'Hi, {name}. What woul you like to do today?')
    print('\n')

    while True:
        print('Use the following short codes to tell us how to help you: ce - collect existing credentials, cn - create new account on a new platform and have credentials saved here, del - delete existing credentials, vw - view saved credentials, ex - exit the application')
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
            print("-"*14)
            print("Delete Account")
            print("-"*14)

            print('Kindly enter the name of the platform to be deleted:')
            del_platform = input()

            print('Kindly enter username of account to be deleted:')
            del_username = input()

            if del_username & del_platform :
                found_credentials = find_credentials(del_platform,del_username)
                found_credentials_index = find_credentials_index(del_platform, del_username)
                
                print(f'The following account is going to be permanetly deleted => {found_credentials.platform}:{found_credentials.username}')
                print('\n')

                del_user(found_credentials_index.ind)


            else:
                print("Credentials not available")

        
        elif short_code == 'vw':
            print("-"*16)
            print("View Credentials")
            print("-"*16)

            if display_users():
                print('\n')



            