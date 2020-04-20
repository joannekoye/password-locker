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
