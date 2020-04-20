import unittest
from user import User


class TestUser(unittest.TestCase):

    '''
    Test class that defines test cases for the user class behaviors.

    Args:
        unittest.TestCases: TestCase class that helps in creatng test cases

    '''

    def setUp(self):
        '''
        Set up method to run before each test case.
        '''
        self.new_user = User('Twitter', 'Joan', 'Nekoye','NekoyeJoan','12345')



    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''
        User.user_list = []


    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_user.platform,"Twitter")
        self.assertEqual(self.new_user.first_name,"Joan")
        self.assertEqual(self.new_user.last_name,"Nekoye")
        self.assertEqual(self.new_user.username,"NekoyeJoan")
        self.assertEqual(self.new_user.password,"12345")


    def test_save_user(self):
        '''
        test_save_user to test if the user object is saved into the user list
        '''
        self.new_user.save_user()
        self.assertEqual(len(User.user_list),1)


    def test_save_multiple_users(self):
        '''
        test_save_multiple_users to check if we can save multiple users/ accounts
        '''
        self.new_user.save_user()
        test_user = User('Instagram','Mark','Gitau','gitaugram','6789')
        test_user.save_user()
        self.assertEqual(len(User.user_list),2)

    def test_delete_user(self):
        '''
        test_delete_user to test if we can remove a user from the list
        '''
        self.new_user.save_user()
        test_user = User('Instagram','Mark','Gitau','gitaugram','6789')
        test_user.save_user()

        self.assertEqual(len(User.user_list),1)


    

if __name__ == '__main__':
    unittest.main(verbosity=2)