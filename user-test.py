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


if __name__ == '__main__':
    unittest.main()