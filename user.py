class User:
    '''
    Class that generates new instances of user credentials 
    '''
    users = []

    def __init__(self, first_name,last_name,username, password):
        '''
        __init__ method helps us define object properties.

        Args:
            first_name: New User first name.
            last_name: New user last name.
            username: New user desired username.
            password: New user password.
        '''
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.password = password