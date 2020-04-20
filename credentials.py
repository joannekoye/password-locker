from user import User

class Credentials:
    '''
    Class that stores and passes saved credentials
    '''
    new_user_list = User.user_list


    def __init__(self, platform, first_name,last_name,username, password):
        '''
        __init__ method helps us define object properties.

        Args:
            first_name: New User first name.
            last_name: New user last name.
            username: New user desired username.
            password: New user password.
        '''

        self.platform = platform
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.password = password
    
    
    def save_user(self):
        '''
        save_user method saves user objects into user_list
        '''

        User.user_list.append(self)


    @classmethod
    def delete_user(cls,credential):
        '''
        delete_user method deletes a user from the user_list
        '''

        Credentials.new_user_list.remove(credential)


    @classmethod
    def display_credentials(cls):
        '''
        method that returns the user list
        '''
        return cls.new_user_list


    @classmethod
    def find_credential(cls,platform, username):
        '''
        Method that takes in a platform & username and returns user credentials that match that platform and username.

        Args:
            platform : platform to search for
            username : username to search for
        Returns :
            User credentials of person that matches the platfofrm and username.
        '''
        if len(cls.new_user_list)> 0:
            for credential in cls.new_user_list:
                if credential.platform == platform and credential.username == username:
                    return credential 
        else:
            return None



    