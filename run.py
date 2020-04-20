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


def display_credentials():
    '''
    Function that returns all saved users
    '''
    return Credentials.display_credentials()


def main():
    print('\n')
    print('Hello! Welcome to Password Locker. What is your name?')
    name = input()
    print('\n')
    print(f'Hi, {name}. What would you like to do today?')
    

    while True:
        print('\n')
        print('Use the following short codes to tell us how to help you: ce - collect existing credentials, cn - create new account on a new platform and have credentials saved here, vw - view saved credentials, del - delete existing credentials, ex - exit the application')
        print('\n')
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

            print('\n')
            print('-'*35)
            print('Password Generation for new account:')
            print('-'*35)
            

            print('\n')
            print('Use the following short codes to tell us if you would like to set your own password or if you would like a system generated password: own - your own password, sys - system generated password')
            print('\n')
            passcode = input().lower()

            if passcode == 'own':
                print('\n')
                print('Kindly enter your prefered password: (Your password is safe with us)')
                password = input()
                print('\n')
                print('Password stored successfully')
                print("Account setup complete")

            elif passcode == 'sys':
                    print('\n')
                    password = random.randint(34567,98756)
                    print('\n')
                    print("Password generation is SUCCESSFUL!")
                    print("Account setup complete")

            else:
                print('\n')
                print("I really didn't get that. Please use the short codes")
            

            save_user(create_user(platform, firstname, lastname, username, password))
            print('\n')

        elif short_code == 'del':
            print("-"*14)
            print("Delete Account")
            print("-"*14)

            print('Kindly enter the name of the platform to be deleted:')
            del_platform = input()

            print('Kindly enter username of account to be deleted:')
            del_username = input()

            if del_username and del_platform :
                found_credentials = Credentials.find_credential(del_platform,del_username)
                
                if found_credentials:
                    print('\n')
                    print(f'The following account is going to be permanetly deleted => {found_credentials.platform}:{found_credentials.username}')
                    print('\n')

                    del_user(found_credentials)

                else:
                    print('\n')
                    print("Credentials not available")
                    print('\n')

        
        elif short_code == 'vw':
            print("-"*16)
            print("View Credentials")
            print("-"*16)

            if display_credentials():
                print('\n')
                print("Here is a list of all your credentials:")
                print('\n')

                for user in display_credentials():
                    
                    print(f'{user.platform} account, Username: {user.username}, Password : {user.password}')
                    

            else:
                print('\n')
                print("You dont seem to have any credentials saved yet")
                print('\n')

        elif short_code == "ex":
            print('\n')
            print("GOODBYE!")
            print('\n')
            break

        else:
            print('\n')
            print("I really didn't get that. Please use the short codes")
            print('\n')
        

if __name__ == '__main__':
    main()
