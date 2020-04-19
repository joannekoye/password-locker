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
    print('Hello, Welcome to Password Locker')