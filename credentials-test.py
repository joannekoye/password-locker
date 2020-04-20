import unittest
from credentials import Credentials


class TestCredentials(unittest.TestCase):

    '''
    Test class that defines test cases for the credentials class behaviors.

    Args:
        unittest.TestCases: TestCase class that helps in creatng test cases

    '''

    def setUp(self):
        '''
        Set up method to run before each test case.
        '''
        self.new_user = Credentials('Twitter', 'Joan', 'Nekoye','NekoyeJoan','12345')



    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''
        Credentials.new_user_list = []


    def test_display_all_credentials(self):
        '''
        method that returns a list of all users saved
        '''

        self.assertEqual(Credentials.display_credentials(), Credentials.new_user_list)


if __name__ == '__main__':
    unittest.main(verbosity=2)