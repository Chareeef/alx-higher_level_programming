#!/usr/bin/python3
'''Test The Rectangle class using unittest'''
import unittest
import sys
import io
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

    def test_wrong_argument(self):
        '''Test if a wrong arguments number is passed'''

        with self.assertRaises(TypeError):
            r1 = Rectangle(8)

        with self.assertRaises(TypeError):
            r2 = Rectangle(0, 1, 2, 3, 4, 5)

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

        r1.width = 5
        r1.height = 9
        r1.x = 7
        r1.y = 3

        attrs = (r1.width, r1.height, r1.x, r1.y, r1.id)

        self.assertEqual(attrs, (5, 9, 7, 3, 6))

    def test_setters_exceptions(self):
        '''Test that setters raise the right exceptions'''

        with self.assertRaisesRegex(TypeError, 'width must be an integer'):
            r = Rectangle('foo', 7, 3)

        with self.assertRaisesRegex(TypeError, 'width must be an integer'):
            r = Rectangle(4, 7)
            r.width = True

        with self.assertRaisesRegex(TypeError, 'height must be an integer'):
            r = Rectangle(9, 7.7, 3)

        with self.assertRaisesRegex(TypeError, 'y must be an integer'):
            r = Rectangle(4, 3)
            r.y = [7]

        with self.assertRaisesRegex(TypeError, 'x must be an integer'):
            r = Rectangle(4, 3, 'bar', 'Doe', 7)

        with self.assertRaisesRegex(TypeError, 'y must be an integer'):
            r = Rectangle(4, 3, 2, '1')

        with self.assertRaisesRegex(TypeError, 'width must be an integer'):
            r = Rectangle(float('inf'), 3, 'bar', 'Doe', 7)

        with self.assertRaisesRegex(ValueError, 'width must be > 0'):
            r = Rectangle(0, 2)

        with self.assertRaisesRegex(ValueError, 'height must be > 0'):
            r = Rectangle(4, 0)

        with self.assertRaisesRegex(ValueError, 'height must be > 0'):
            r = Rectangle(4, 3)
            r.height = 0

        with self.assertRaisesRegex(ValueError, 'width must be > 0'):
            r = Rectangle(-4, -3)

        with self.assertRaisesRegex(ValueError, 'x must be >= 0'):
            r = Rectangle(2, 2, -3, 0)

        with self.assertRaisesRegex(ValueError, 'y must be >= 0'):
            r = Rectangle(2, 2, 5, 8)
            r.y = -6


class TestRectangleArea(unittest.TestCase):
    '''
    This class gathers test cases to ensure that
    the Rectangle class area() method works conveniently
    '''

    def test_area(self):
        '''Test the Rectangle's area() public method'''

        r1 = Rectangle(2, 9)
        r2 = Rectangle(8886, 467)
        r3 = Rectangle(1, 1, 3, 8, 6)

        self.assertEqual(r1.area(), 18)
        self.assertEqual(r2.area(), 4149762)
        self.assertEqual(r3.area(), 1)

    def test_wrong_argument(self):
        '''Test if a wrong arguments number is passed'''

        with self.assertRaises(TypeError):
            r = Rectangle(8, 8)
            r.area(9, 7)


class TestRectangleDisplay(unittest.TestCase):
    '''
    This class gathers test cases to ensure that
    the Rectangle is displayed conveniently
    '''

    def setUp(self):
        '''Redirect standard output to capture any function output'''
        self.stdout = io.StringIO()
        sys.stdout = self.stdout

    def tearDown(self):
        '''Restore the standard output'''
        sys.stdout = sys.__stdout__

    def test_display_5_on_7_no_xy(self):
        '''Test the Rectangle's display() public method'''

        r = Rectangle(5, 7)

        r.display()

        printed = self.stdout.getvalue()
        expected = "#####\n" * 7

        self.assertEqual(printed, expected)

    def test_display_7_on_5_with_xy(self):
        '''Test the Rectangle's display() public method'''

        r = Rectangle(7, 5, 1, 2)

        r.display()

        printed = self.stdout.getvalue()
        expected = ("\n" * 2) + (" #######\n" * 5)

        self.assertEqual(printed, expected)

    def test_display_4_on_3_with_xy(self):
        '''Test the Rectangle's display() public method'''

        r = Rectangle(4, 3, 4)

        r.display()

        printed = self.stdout.getvalue()
        expected = "    ####\n" * 3

        self.assertEqual(printed, expected)

    def test_display_3_on_3_with_xy(self):
        '''Test the Rectangle's display() public method'''

        r = Rectangle(3, 3, y=8)

        r.display()

        printed = self.stdout.getvalue()
        expected = ("\n" * 8) + ("###\n" * 3)

        self.assertEqual(printed, expected)

    def test_display_1_on_1_no_xy(self):
        '''Test the Rectangle's display() public method'''

        r = Rectangle(1, 1)

        r.display()

        printed = self.stdout.getvalue()
        expected = "#\n"

        self.assertEqual(printed, expected)

    def test_wrong_argument(self):
        '''Test if a wrong arguments number is passed'''

        with self.assertRaises(TypeError):
            r = Rectangle(8, 8)
            r.display(9)


class TestRectanglePrint(unittest.TestCase):
    '''
    This class gathers test cases to ensure that
    the Rectangle's __str__ method works well
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
        '''Test the Rectangle's __str__ magic method returned string'''

        r1 = Rectangle(5, 7, 3, 2)

        returned_string = r1.__str__()
        expected = "[Rectangle] (1) 3/2 - 5/7"

        self.assertEqual(returned_string, expected)

        r = Rectangle(5, 7, id=7)

        returned_string = r.__str__()
        expected = "[Rectangle] (7) 0/0 - 5/7"

        self.assertEqual(returned_string, expected)

        r1 = Rectangle(1, 1, 1)

        returned_string = r1.__str__()
        expected = "[Rectangle] (2) 1/0 - 1/1"

        self.assertEqual(returned_string, expected)

    def test_print_rectangle(self):
        '''Test printing the Rectangle'''

        r = Rectangle(7, 5, id=99)
        print(r)
        expected = "[Rectangle] (99) 0/0 - 7/5\n"

        rect = Rectangle(7, 5, 8, 3)
        print(rect)
        expected += "[Rectangle] (1) 8/3 - 7/5\n"

        r = Rectangle(9, 85, y=3)
        print(r)
        expected += "[Rectangle] (2) 0/3 - 9/85\n"

        printed = self.stdout.getvalue()

        self.assertEqual(printed, expected)


class TestRectangleUpdate(unittest.TestCase):
    '''
    This class gathers test cases to ensure that
    the Rectangle's update method works conveniently
    '''

    def setUp(self):
        '''Reset Base's number of objects to 0 before every test'''
        Base._Base__nb_objects = 0

    def test_update_all(self):
        '''Test for updating all attributes'''

        r1 = Rectangle(6, 6, 3, 8, 9)
        self.assertEqual(r1.__str__(), "[Rectangle] (9) 3/8 - 6/6")

        r1.update(7, 2, 3, 4, 5)
        self.assertEqual(r1.__str__(), "[Rectangle] (7) 4/5 - 2/3")

        r2 = Rectangle(5, 7, 3)
        self.assertEqual(r2.__str__(), "[Rectangle] (1) 3/0 - 5/7")

        r2.update(id=7, x=2, y=3, height=4, width=5)
        self.assertEqual(r2.__str__(), "[Rectangle] (7) 2/3 - 5/4")

    def test_update_some(self):
        '''Test for updating some attributes'''

        r1 = Rectangle(6, 6, 3, 8)
        self.assertEqual(r1.__str__(), "[Rectangle] (1) 3/8 - 6/6")

        r1.update(7)
        self.assertEqual(r1.__str__(), "[Rectangle] (7) 3/8 - 6/6")

        r1.update(y=9)
        self.assertEqual(r1.__str__(), "[Rectangle] (7) 3/9 - 6/6")

        r1.update(99, 4, 3)
        self.assertEqual(r1.__str__(), "[Rectangle] (99) 3/9 - 4/3")

        r1.update(id=8, width=8, x=0)
        self.assertEqual(r1.__str__(), "[Rectangle] (8) 0/9 - 8/3")

    def test_update_mixed(self):
        '''Test for updating with *args and **kwargs'''

        r1 = Rectangle(6, 6, 3, 8)
        self.assertEqual(r1.__str__(), "[Rectangle] (1) 3/8 - 6/6")

        r1.update(7, 1, height=9, x=0, y=0)
        self.assertEqual(r1.__str__(), "[Rectangle] (7) 3/8 - 1/6")

    def test_update_wrong(self):
        '''Test for updating with wrong arguments'''

        r1 = Rectangle(6, 6, 3, 8)
        self.assertEqual(r1.__str__(), "[Rectangle] (1) 3/8 - 6/6")

        with self.assertRaisesRegex(TypeError, 'x must be an integer'):
            r1.update(8, 4, 8, '7')

        with self.assertRaisesRegex(ValueError, 'width must be > 0'):
            r1.update(id=9, height=9, x=7, width=0)


class TestRectangleJSON(unittest.TestCase):
    '''
    This class gathers test cases to ensure that
    the Rectangle class handles JSON conversions conveniently
    '''

    def setUp(self):
        '''Method that runs before every test'''
        Base._Base__nb_objects = 0

    def test_to_dictionary(self):
        '''Test to_dictionary() method'''

        r1 = Rectangle(2, 4, 1, 1)
        d1 = r1.to_dictionary()
        expected = {'id': 1, 'width': 2, 'height': 4, 'x': 1, 'y': 1}

        self.assertEqual(d1, expected)
        self.assertEqual(type(d1), dict)

        r2 = Rectangle(5, 8, id=9)
        d2 = r2.to_dictionary()
        expected = {'id': 9, 'width': 5, 'height': 8, 'x': 0, 'y': 0}

        self.assertEqual(d2, expected)

        r2.update(**d1)
        d2 = r2.to_dictionary()

        self.assertEqual(d1, d2)
        self.assertNotEqual(r1, r2)
