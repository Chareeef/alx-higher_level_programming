#!/usr/bin/python3
'''Test The Base class using unittest'''
import unittest
import json
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBaseInstantiation(unittest.TestCase):
    '''
    This class gathers test cases to ensure that
    the Base class instantiation works conveniently
    '''

    def setUp(self):
        '''Method that runs before every test'''
        Base._Base__nb_objects = 0

    def test_monitor_id(self):
        '''Test correct id for each instance'''

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


class TestBaseJSON(unittest.TestCase):
    '''
    This class gathers test cases to ensure that
    the Base class handles JSON operation conveniently
    '''

    def setUp(self):
        '''Method that runs before every test'''
        Base._Base__nb_objects = 0

    def test_to_json_string(self):
        '''Test to_json_string() static method'''

        r = Rectangle(4, 3, id=5)
        s = Square(9, 2, 2)

        d1 = r.to_dictionary()
        d2 = s.to_dictionary()

        # With one dictionary:

        json_str_1 = Base.to_json_string([d1])
        self.assertIs(type(json_str_1), str)

        expected_str_1 = '[{"id": 5, "width": 4, "height": 3, "x": 0, "y": 0}]'

        # We compare .loads() results because we don't know the keys order
        self.assertEqual(json.loads(json_str_1), json.loads(expected_str_1))

        # With two dictionary:

        json_str_2 = Base.to_json_string([d1, d2])

        expected_str_2 = '[{"id": 5, "width": 4, "height": 3, "x": 0, "y": 0},'
        expected_str_2 += ' {"id": 1, "size": 9, "x": 2, "y" : 2}]'

        self.assertEqual(json.loads(json_str_2), json.loads(expected_str_2))

        # Edge cases:

        json_str_None = Base.to_json_string(None)
        json_str_empty = Base.to_json_string([])

        self.assertEqual(json_str_None, '[]')
        self.assertEqual(json_str_empty, '[]')

        with self.assertRaises(TypeError):
            wrong_json_str = Base.to_json_string()

        with self.assertRaises(TypeError):
            wrong_json_str = Base.to_json_string([{'id': 8}], [{'x': 7}])
