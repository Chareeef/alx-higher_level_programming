#!/usr/bin/python3
'''Test The Base class using unittest'''
import unittest
from models.base import Base


class TestBaseInstantiation(unittest.TestCase):
    '''
    This class gathers test cases to ensure that
    the Base class instantiation works conveniently
    '''

    def setUp(self):
        '''Method that runs before every test'''
        Base._Base__nb_objects = 0

    def test_monitor_id(self):
        '''Test correct id for eavh instance'''

        # Without passing an id
        b1 = Base()
        self.assertEqual(b1.id, 1)

        b2 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)

        # By passing an id
        b3 = Base(9)
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 9)

        # Again without passing an id
        b4 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 9)
        self.assertEqual(b4.id, 3)

    def test_missing_argument(self):
        '''Test if a wrong arguments number is passed'''

        with self.assertRaises(TypeError):
            b = Base(9, 5)
