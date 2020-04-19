from user import User

class Credentials:
    '''
    Class that stores and passes saved credentials
    '''
    new_user_list = User.user_list

    def delete_user(self):
        '''
        delete_user method deletes a user from the user_list
        '''

        Credentials.new_user_list.remove(self)

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
        for user in cls.new_user_list:
            if user.platform == platform & user.username == username:
                return user
                