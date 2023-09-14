#!/usr/bin/python3
'''Test The Rectangle class using unittest'''
import unittest
from models.rectangle import Rectangle
from models.base import Base


class TestRectangleInstantiation(unittest.TestCase):
    '''
    This class gathers test cases to ensure that
    the Rectangle class instantiation works conveniently
    '''

    def setUp(self):
        '''Method that runs before every test'''
        Base._Base__nb_objects = 0

    def test_type_rectangle(self):
        '''Ensure that Rectangle is a subclass of Base'''

        r1 = Rectangle(5, 8)
        self.assertTrue(isinstance(r1, Base))
        self.assertTrue(type(r1) is Rectangle)
        self.assertTrue(issubclass(Rectangle, Base))

    def test_correct_attributes(self):
        '''Test correct attributes for each instance'''

        r1 = Rectangle(10, 5, 2, 1)
        r2 = Rectangle(20, 30)
        r3 = Rectangle(25, 25, id=5)
        r4 = Rectangle(3, 6, y=6)

        r1_atrr = (r1.width, r1.height, r1.x, r1.y, r1.id)
        r2_atrr = (r2.width, r2.height, r2.x, r2.y, r2.id)
        r3_atrr = (r3.width, r3.height, r3.x, r3.y, r3.id)
        r4_atrr = (r4.width, r4.height, r4.x, r4.y, r4.id)

        self.assertEqual(r1_atrr, (10, 5, 2, 1, 1))
        self.assertEqual(r2_atrr, (20, 30, 0, 0, 2))
        self.assertEqual(r3_atrr, (25, 25, 0, 0, 5))
        self.assertEqual(r4_atrr, (3, 6, 0, 6, 3))
        
    def test_getters_and_setters(self):
        '''Test getters and setters for each attribute'''

        r1 = Rectangle(10, 5, 2, 1, 6)

        r1.width = 5.5
        r1.height = 9
        r1.x = 7
        r1.y = 3

        attrs = (r1.width, r1.height, r1.x, r1.y, r1.id)

        self.assertEqual(attrs, (5.5, 9, 7, 3, 6))

    def test_missing_argument(self):
        '''Test if a wrong arguments number is passed'''

        with self.assertRaises(TypeError):
            r1 = Rectangle(8)

        with self.assertRaises(TypeError):
            r2 = Rectangle(0, 1, 2, 3, 4, 5)
