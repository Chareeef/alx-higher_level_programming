#!/usr/bin/python3
'''
Module to test max_integer([..]) function using unittest
'''
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    '''
    class containing tests for the max_integer() function
    '''

    def test_full_lists(self):
        '''Testing different integers lists'''

        list_ints = [0, 6, -77, 0, 5]
        self.assertEqual(max_integer(list_ints), 6)

        list_ints = [555, -7000, 87, 1]
        self.assertEqual(max_integer(list_ints), 555)

    def test_empty_list(self):
        '''Testing empty list'''

        self.assertIsNone(max_integer())
        self.assertIsNone(max_integer([]))

    def test_not_only_integers(self):
        '''Testing lists that not only contain integers'''

        not_list_ints = ['string', True, (8, )]
        self.assertRaises(TypeError, max_integer, not_list_ints)

        not_list_ints = [77, 'string', 7, 3]
        self.assertRaises(TypeError, max_integer, not_list_ints)

    def test_with_tuples(self):
        '''Testing with tuples'''

        tuple_ints = (0, 6, -77, 0, 5)
        self.assertEqual(max_integer(tuple_ints), 6)

        tuple_ints = (555, -7000, 87, 1)
        self.assertEqual(max_integer(tuple_ints), 555)

        not_tuple_ints = ('string', True, (8, ))
        self.assertRaises(TypeError, max_integer, not_tuple_ints)

        not_tuple_ints = (77, 'string', 7, 3)
        self.assertRaises(TypeError, max_integer, not_tuple_ints)

        self.assertIsNone(max_integer(()))

    def test_with_sets(self):
        '''Testing with sets'''

        set_ints = {0, 6, -77, 0, 5}
        self.assertRaises(TypeError, max_integer, set_ints)

        set_ints = {555, -7000, 87, 1}
        self.assertRaises(TypeError, max_integer, set_ints)

        not_set_ints = {'string', True, (8, )}
        self.assertRaises(TypeError, max_integer, not_set_ints)

        not_set_ints = {77, 'string', 7, 3}
        self.assertRaises(TypeError, max_integer, not_set_ints)

        self.assertIsNone(max_integer({}))
