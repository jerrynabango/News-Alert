import unittest
from flask import current_app
from app import create_app

class BasicsTestCase(unittest.TestCase):
    def setUp(self):
        
        '''
        Set up method that will run before every Test
        '''
        
        self.app = create_app('development')