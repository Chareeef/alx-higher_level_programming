#!/usr/bin/python3
'''Test The Square class using unittest'''
import unittest
import sys
import io
from models.square import Square
from models.rectangle import Rectangle
from models.base import Base


class TestSquareInstantiation(unittest.TestCase):
    '''
    This class gathers test cases to ensure that
    the Square class instantiation works conveniently
    '''

    def setUp(self):
        '''Method that runs before every test'''
        Base._Base__nb_objects = 0

    def test_type_square(self):
        '''Ensure that Square is a subclass of Base'''

        s1 = Square(5)
        self.assertTrue(isinstance(s1, Rectangle))
        self.assertTrue(isinstance(s1, Base))
        self.assertTrue(type(s1) is Square)
        self.assertTrue(issubclass(Square, Rectangle))
        self.assertTrue(issubclass(Square, Base))

    def test_wrong_argument(self):
        '''Test if a wrong arguments number is passed'''

        with self.assertRaises(TypeError):
            s1 = Square()

        with self.assertRaises(TypeError):
            s2 = Square(1, 2, 3, 4, 5)

    def test_correct_attributes(self):
        '''Test correct attributes for each instance'''

        s1 = Square(10, 7, 7, 6)
        s2 = Square(20)
        s3 = Square(25, 20, id=5)
        s4 = Square(3, y=6)

        s1_atrr = (s1.size, s1.x, s1.y, s1.id)
        s2_atrr = (s2.size, s2.x, s2.y, s2.id)
        s3_atrr = (s3.width, s3.height, s3.x, s3.y, s3.id)
        s4_atrr = (s4.width, s4.height, s4.x, s4.y, s4.id)

        self.assertEqual(s1_atrr, (10, 7, 7, 6))
        self.assertEqual(s2_atrr, (20, 0, 0, 1))
        self.assertEqual(s3_atrr, (25, 25, 20, 0, 5))
        self.assertEqual(s4_atrr, (3, 3, 0, 6, 2))

    def test_getters_and_setters(self):
        '''Test getters and setters for each attribute'''

        s1 = Square(10, 2, 1, 6)

        s1.width = 5
        s1.size = 9
        s1.x = 7
        s1.y = 3

        attrs = (s1.size, s1.width, s1.height, s1.x, s1.y, s1.id)

        self.assertEqual(attrs, (9, 9, 9, 7, 3, 6))

    def test_setters_exceptions(self):
        '''Test that setters raise the right exceptions'''

        with self.assertRaisesRegex(TypeError, 'width must be an integer'):
            s1 = Square('foo', 7, 3)

        with self.assertRaisesRegex(TypeError, 'width must be an integer'):
            s1 = Square(7)
            s1.size = True

        with self.assertRaisesRegex(TypeError, 'height must be an integer'):
            s1 = Square(7)
            s1.height = {8, 7, 6}

        with self.assertRaisesRegex(TypeError, 'width must be an integer'):
            s1 = Square(7)
            s1.width = (8, 7, 6)

        with self.assertRaisesRegex(TypeError, 'width must be an integer'):
            s1 = Square(7.7, 3)

        with self.assertRaisesRegex(TypeError, 'y must be an integer'):
            s1 = Square(4)
            s1.y = [7]

        with self.assertRaisesRegex(TypeError, 'x must be an integer'):
            s1 = Square(3, 'bar', 'Doe', 7)

        with self.assertRaisesRegex(TypeError, 'width must be an integer'):
            s1 = Square(float('inf'), 'bar', 'Doe', 7)

        with self.assertRaisesRegex(ValueError, 'width must be > 0'):
            s1 = Square(4)
            s1.size = 0

        with self.assertRaisesRegex(ValueError, 'width must be > 0'):
            s1 = Square(-4, -3)

        with self.assertRaisesRegex(ValueError, 'x must be >= 0'):
            s1 = Square(2, -3, 0)

        with self.assertRaisesRegex(ValueError, 'y must be >= 0'):
            s1 = Square(2, 5, 8)
            s1.y = -6


class TestSquareArea(unittest.TestCase):
    '''
    This class gathers test cases to ensure that
    the Square class area() method works conveniently
    '''

    def test_area(self):
        '''Test the Square's area() public method'''

        s1 = Square(9)
        s2 = Square(886)
        s3 = Square(1, 1, 8, 6)

        self.assertEqual(s1.area(), 81)
        self.assertEqual(s2.area(), 784996)
        self.assertEqual(s3.area(), 1)

    def test_wrong_argument(self):
        '''Test if a wrong arguments number is passed'''

        with self.assertRaises(TypeError):
            s1 = Square(8, 8)
            s1.area(9, 7)


class TestSquareDisplay(unittest.TestCase):
    '''
    This class gathers test cases to ensure that
    the Square is displayed conveniently
    '''

    def setUp(self):
        '''Redirect standard output to capture any function output'''
        self.stdout = io.StringIO()
        sys.stdout = self.stdout

    def tearDown(self):
        '''Restore the standard output'''
        sys.stdout = sys.__stdout__

    def test_display_5_no_xy(self):
        '''Test the Square's display() public method'''

        s = Square(5)

        s.display()

        printed = self.stdout.getvalue()
        expected = "#####\n" * 5

        self.assertEqual(printed, expected)

    def test_display_7_with_xy(self):
        '''Test the Square's display() public method'''

        s = Square(7, 1, 2)

        s.display()

        printed = self.stdout.getvalue()
        expected = ("\n" * 2) + (" #######\n" * 7)

        self.assertEqual(printed, expected)

    def test_display_4_with_xy(self):
        '''Test the Square's display() public method'''

        s = Square(4, 4, 1)

        s.display()

        printed = self.stdout.getvalue()
        expected = ('\n' * 1) + ("    ####\n" * 4)

        self.assertEqual(printed, expected)

    def test_display_3_with_xy(self):
        '''Test the Square's display() public method'''

        s = Square(3, y=8)

        s.display()

        printed = self.stdout.getvalue()
        expected = ("\n" * 8) + ("###\n" * 3)

        self.assertEqual(printed, expected)

    def test_display_1_no_xy(self):
        '''Test the Square's display() public method'''

        s = Square(1)

        s.display()

        printed = self.stdout.getvalue()
        expected = "#\n"

        self.assertEqual(printed, expected)

    def test_wrong_argument(self):
        '''Test if a wrong arguments number is passed'''

        with self.assertRaises(TypeError):
            s = Square(8, 8)
            s.display(9)


class TestSquarePrint(unittest.TestCase):
    '''
    This class gathers test cases to ensure that
    the Square's __str__ method works well
    '''

    def setUp(self):
        '''Redirect standard output to capture any function output'''
        Base._Base__nb_objects = 0
        self.stdout = io.StringIO()
        sys.stdout = self.stdout

    def tearDown(self):
        '''Restore the standard output'''
        sys.stdout = sys.__stdout__

    def test_str_return(self):
        '''Test the Square's __str__ magic method returned string'''

        s1 = Square(5, 3, 2)

        returned_string = s1.__str__()
        expected = "[Square] (1) 3/2 - 5"

        self.assertEqual(returned_string, expected)

        s1 = Square(7, id=7)

        returned_string = s1.__str__()
        expected = "[Square] (7) 0/0 - 7"

        self.assertEqual(returned_string, expected)

        s1 = Square(1, 1, 1)

        returned_string = s1.__str__()
        expected = "[Square] (2) 1/1 - 1"

        self.assertEqual(returned_string, expected)

    def test_print_square(self):
        '''Test printing the Square'''

        s1 = Square(7, 5, id=99)
        print(s1)
        expected = "[Square] (99) 5/0 - 7\n"

        s2 = Square(4, 8, 3)
        print(s2)
        expected += "[Square] (1) 8/3 - 4\n"

        s1 = Square(88, y=3)
        print(s1)
        expected += "[Square] (2) 0/3 - 88\n"

        printed = self.stdout.getvalue()

        self.assertEqual(printed, expected)


class TestSquareUpdate(unittest.TestCase):
    '''
    This class gathers test cases to ensure that
    the Square's update method works conveniently
    '''

    def setUp(self):
        '''Reset Base's number of objects to 0 before every test'''
        Base._Base__nb_objects = 0

    def test_update_all(self):
        '''Test for updating all attributes'''

        s1 = Square(6, 3, 8, 9)
        self.assertEqual(s1.__str__(), "[Square] (9) 3/8 - 6")

        s1.update(7, 2, 4, 5)
        self.assertEqual(s1.__str__(), "[Square] (7) 4/5 - 2")

        s2 = Square(5, 7, 3)
        self.assertEqual(s2.__str__(), "[Square] (1) 7/3 - 5")

        s2.update(id=7, x=2, y=3, size=3)
        self.assertEqual(s2.__str__(), "[Square] (7) 2/3 - 3")

    def test_update_some(self):
        '''Test for updating some attributes'''

        s1 = Square(6, 3, 8)
        self.assertEqual(s1.__str__(), "[Square] (1) 3/8 - 6")

        s1.update(7)
        self.assertEqual(s1.__str__(), "[Square] (7) 3/8 - 6")

        s1.update(y=9)
        self.assertEqual(s1.__str__(), "[Square] (7) 3/9 - 6")

        s1.update(99, 4, 3)
        self.assertEqual(s1.__str__(), "[Square] (99) 3/9 - 4")

        s1.update(id=8, size=8, x=0)
        self.assertEqual(s1.__str__(), "[Square] (8) 0/9 - 8")

    def test_update_mixed(self):
        '''Test for updating with *args and **kwargs'''

        s1 = Square(2, 3, 8)
        self.assertEqual(s1.__str__(), "[Square] (1) 3/8 - 2")

        s1.update(7, 1, size=9, x=0, y=0)
        self.assertEqual(s1.__str__(), "[Square] (7) 3/8 - 1")

    def test_update_wrong(self):
        '''Test for updating with wrong arguments'''

        s1 = Square(6, 3, 8)
        self.assertEqual(s1.__str__(), "[Square] (1) 3/8 - 6")

        with self.assertRaisesRegex(TypeError, 'x must be an integer'):
            s1.update(8, 4, '7')

        with self.assertRaisesRegex(ValueError, 'width must be > 0'):
            s1.update(id=9, x=7, size=0)


class TestSquareJSON(unittest.TestCase):
    '''
    This class gathers test cases to ensure that
    the Square class handles JSON conversions conveniently
    '''

    def setUp(self):
        '''Method that runs before every test'''
        Base._Base__nb_objects = 0

    def test_to_dictionary(self):
        '''Test to_dictionary() method'''

        s1 = Square(4, 3, 2)
        d1 = s1.to_dictionary()
        expected = {'id': 1, 'size': 4, 'x': 3, 'y': 2}

        self.assertEqual(d1, expected)
        self.assertEqual(type(d1), dict)

        s2 = Square(5, 8, id=77)
        d2 = s2.to_dictionary()
        expected = {'id': 77, 'size': 5, 'x': 8, 'y': 0}

        self.assertEqual(d2, expected)

        s2.update(**d1)
        d2 = s2.to_dictionary()

        self.assertEqual(d1, d2)
        self.assertNotEqual(s1, s2)
