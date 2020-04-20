class User:
    '''
    Class that generates new instances of user credentials 
    '''
    user_list = []

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

        
    

