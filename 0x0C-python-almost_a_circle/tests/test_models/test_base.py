#!/usr/bin/python3
'''Test The Base class using unittest'''
import unittest
import json
import os
import glob
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
    the Base class handles JSON operations conveniently
    '''

    def setUp(self):
        '''Method that runs before every test'''
        Base._Base__nb_objects = 0

    def test_to_json_string_normal(self):
        '''test to_json_string() static method in normal cases'''

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

    def test_to_json_string_edge(self):
        '''Test to_json_string() static method in edge cases'''

        json_str_None = Base.to_json_string(None)
        json_str_empty = Base.to_json_string([])
        json_str_empty_dict = Base.to_json_string([{}])

        self.assertEqual(json_str_None, '[]')
        self.assertEqual(json_str_empty, '[]')
        self.assertEqual(json_str_empty_dict, '[{}]')

        with self.assertRaises(TypeError):
            wrong_json_str = Base.to_json_string()

        with self.assertRaises(TypeError):
            wrong_json_str = Base.to_json_string([{'id': 8}], [{'x': 7}])

    def test_from_json_string_normal(self):
        '''test from_json_string() static method in normal cases'''

        list_str_1 = '[{"id": 5, "width": 4, "height": 3, "x": 0, "y": 0}]'
        list_1 = Base.from_json_string(list_str_1)
        self.assertIs(type(list_1), list)

        expected_list_1 = [{'id': 5, 'width': 4, 'height': 3, 'x': 0, 'y': 0}]

        self.assertEqual(list_1, expected_list_1)

        list_str_2 = '[{"id": 5, "width": 4, "height": 3, "x": 0, "y": 0},'
        list_str_2 += ' {"id": 1, "size": 9, "x": 2, "y" : 2}]'
        list_2 = Base.from_json_string(list_str_2)

        expected_list_2 = [{'id': 5, 'width': 4, 'height': 3, 'x': 0, 'y': 0}]
        expected_list_2.append({'id': 1, 'size': 9, 'x': 2, 'y': 2})

        self.assertEqual(list_2, expected_list_2)

    def test_from_json_string_edge(self):
        '''Test from_json_string() static method in edge cases'''

        json_list_None = Base.from_json_string(None)
        json_list_empty_string = Base.from_json_string('')
        json_list_empty_list = Base.from_json_string('[]')
        json_list_empty_dict = Base.from_json_string('[{}]')

        self.assertEqual(json_list_None, [])
        self.assertEqual(json_list_empty_string, [])
        self.assertEqual(json_list_empty_list, [])
        self.assertEqual(json_list_empty_dict, [{}])

        with self.assertRaises(TypeError):
            wrong_json_list = Base.from_json_string()

        with self.assertRaises(TypeError):
            wrong_json_list = Base.from_json_string('[{"y": 8}]', '[{"x": 7}]')

        with self.assertRaises(json.decoder.JSONDecodeError):
            wrong_json_list = Base.from_json_string('[{"id": 8}], [{"x": 7}]')

    def test_save_to_file_normal(self):
        '''Test save_to_file() class method in normal cases'''

        r = Rectangle(4, 3, id=5)
        s1 = Square(4, 2, 2)
        s2 = Square(8, id=3)

        # Rectangle case:

        Rectangle.save_to_file([r])
        expected_str_1 = '[{"id": 5, "width": 4, "height": 3, "x": 0, "y": 0}]'

        with open('Rectangle.json', 'r', encoding='utf-8') as f:
            file_content = f.read()
            self.assertEqual(json.loads(file_content),
                             json.loads(expected_str_1))

        # Square case:

        Square.save_to_file([s1, s2])
        expected_str_2 = '[{"id": 1, "size": 4, "x": 2, "y" : 2}, '
        expected_str_2 += '{"id": 3, "size": 8, "x": 0, "y" : 0}]'

        with open('Square.json', 'r', encoding='utf-8') as f:
            file_content = f.read()
            self.assertEqual(json.loads(file_content),
                             json.loads(expected_str_2))

        # Base case:

        Base.save_to_file([s2, r, s1])
        expected_str_3 = '[{"id": 3, "size": 8, "x": 0, "y" : 0}, '
        expected_str_3 += '{"id": 5, "width": 4, "height": 3, "x": 0, "y": 0},'
        expected_str_3 += ' {"id": 1, "size": 4, "x": 2, "y" : 2}]'

        with open('Base.json', 'r', encoding='utf-8') as f:
            file_content = f.read()
            self.assertEqual(json.loads(file_content),
                             json.loads(expected_str_3))

    def test_save_to_file_edge(self):
        '''Test save_to_file() class method in edge cases'''

        r = Rectangle(4, 3, id=5)
        s1 = Square(4, 2, 2)
        s2 = Square(8, id=3)

        d_r = r.to_dictionary()
        d_s1 = s1.to_dictionary()
        d_s2 = s2.to_dictionary()

        # Passing None:

        Rectangle.save_to_file(None)

        with open('Rectangle.json', 'r', encoding='utf-8') as f:
            self.assertEqual(f.read(), '[]')

        Square.save_to_file(None)

        with open('Square.json', 'r', encoding='utf-8') as f:
            self.assertEqual(f.read(), '[]')

        # Passing an empty list:

        Rectangle.save_to_file([])

        with open('Rectangle.json', 'r', encoding='utf-8') as f:
            self.assertEqual(f.read(), '[]')

        Square.save_to_file([])

        with open('Square.json', 'r', encoding='utf-8') as f:
            self.assertEqual(f.read(), '[]')

        # Square in Rectangle.json which already exists:

        Rectangle.save_to_file([s1, s2])

        with open('Rectangle.json', 'r', encoding='utf-8') as f:
            self.assertEqual(f.read(), json.dumps([d_s1, d_s2]))

        # Passing wrong arguments number:

        with self.assertRaises(TypeError):
            Square.save_to_file('98', 'Street')

    def test_create_normal(self):
        '''Test create() class method in normal cases'''

        r1 = Rectangle(4, 6, 5, 2)
        s1 = Square(3)

        d_r = r1.to_dictionary()
        d_s = s1.to_dictionary()

        r2 = Rectangle.create(**d_r)
        s2 = Square.create(**d_s)

        self.assertIs(type(r2), Rectangle)
        self.assertEqual(r1.to_dictionary(), r2.to_dictionary())
        self.assertNotEqual(r1, r2)
        self.assertIsNot(r1, r2)

        self.assertIs(type(s2), Square)
        self.assertEqual(s1.to_dictionary(), s2.to_dictionary())
        self.assertNotEqual(s1, s2)
        self.assertIsNot(s1, s2)

    def test_create_edge(self):
        '''Test create() class method in edge cases'''

        r1 = Rectangle(4, 6, 5, 2)
        s1 = Square(3)

        d_r = r1.to_dictionary()
        d_s = s1.to_dictionary()

        with self.assertRaises(TypeError):
            r = Rectangle.create(d_s, d_r)

        with self.assertRaises(TypeError):
            r = Rectangle.create(d_r)

    def test_load_from_file_normal(self):
        '''Test load_from_file() class method in normal cases'''

        r1 = Rectangle(2, 1, 1, 2)
        r2 = Rectangle(3, 1)
        s1 = Square(4, 6, 3)
        s2 = Square(1, 1, 3, 6)

        # For Rectangle:

        input_rects = [r1, r2]
        Rectangle.save_to_file(input_rects)

        output_rects = Rectangle.load_from_file()

        rect_pairs = zip(input_rects, output_rects)

        for in_rect, out_rect in rect_pairs:
            self.assertIsNot(in_rect, out_rect)
            self.assertNotEqual(in_rect, out_rect)
            self.assertEqual(in_rect.to_dictionary(), out_rect.to_dictionary())
            self.assertEqual(in_rect.__dict__, out_rect.__dict__)

        # For Square:

        input_squares = [s1, s2]
        Square.save_to_file(input_squares)

        output_squares = Square.load_from_file()

        square_pairs = zip(input_squares, output_squares)

        for in_sq, out_sq in square_pairs:
            self.assertIsNot(in_sq, out_sq)
            self.assertNotEqual(in_sq, out_sq)
            self.assertEqual(in_sq.to_dictionary(), out_sq.to_dictionary())
            self.assertEqual(in_sq.__dict__, out_sq.__dict__)

    def test_load_from_file_edge(self):
        '''Test load_from_file() class method in edge cases'''

        # Passing wrong arguments number:

        with self.assertRaises(TypeError):
            output_squares = Square.load_from_file(0)

        # <Class>.json doesn't exist:

        output_rects = Rectangle.load_from_file()
        self.assertEqual(output_rects, [])

        # Rectangle.json with squares JSON representations:

        s1 = Square(4, 6, 3)
        s2 = Square(1, 1, 3, 6)

        input_objs = [s1, s2]
        Rectangle.save_to_file(input_objs)

        output_objs = Rectangle.load_from_file()

        objs_pairs = zip(input_objs, output_objs)

        for in_obj, out_obj in objs_pairs:
            self.assertIsNot(in_obj, out_obj)
            self.assertIsNot(type(in_obj), type(out_obj))
            self.assertNotEqual(in_obj, out_obj)
            self.assertNotEqual(in_obj.to_dictionary(),
                                out_obj.to_dictionary())
            self.assertNotEqual(in_obj.__dict__, out_obj.__dict__)

    def tearDown(self):
        '''Runs after every test function'''

        for file in glob.glob('*.json'):
            try:
                os.remove(file)
            except OSError:
                pass


class TestBaseCSV(unittest.TestCase):
    '''
    This class gathers test cases to ensure that
    the Base class handles CSV operations conveniently
    '''

    def setUp(self):
        '''Method that runs before every test'''
        Base._Base__nb_objects = 0

    def test_csv_rectangles(self):
        '''Test serializing and deserializing rectangles in CSV format'''

        r1 = Rectangle(3, 4, 7, 1)
        r2 = Rectangle(1, 2, id=3)

        input_rects = [r1, r2]
        Rectangle.save_to_file_csv(input_rects)

        expected_csv = "id,width,height,x,y\n"
        expected_csv += "1,3,4,7,1\n3,1,2,0,0\n"

        with open('Rectangle.csv', 'r', encoding='utf-8') as f:
            self.assertEqual(f.read(), expected_csv)

        output_rects = Rectangle.load_from_file_csv()

        rect_pairs = zip(input_rects, output_rects)

        for in_rect, out_rect in rect_pairs:
            self.assertIsNot(in_rect, out_rect)
            self.assertNotEqual(in_rect, out_rect)
            self.assertEqual(in_rect.to_dictionary(), out_rect.to_dictionary())
            self.assertEqual(in_rect.__dict__, out_rect.__dict__)

    def test_csv_squares(self):
        '''Test serializing and deserializing squares in CSV format'''

        s1 = Square(7)
        s2 = Square(1, 5, 3)

        input_sqs = [s1, s2]
        Square.save_to_file_csv(input_sqs)

        expected_csv = "id,size,x,y\n"
        expected_csv += "1,7,0,0\n2,1,5,3\n"

        with open('Square.csv', 'r', encoding='utf-8') as f:
            self.assertEqual(f.read(), expected_csv)

        output_sqs = Square.load_from_file_csv()

        sq_pairs = zip(input_sqs, output_sqs)

        for in_sq, out_sq in sq_pairs:
            self.assertIsNot(in_sq, out_sq)
            self.assertNotEqual(in_sq, out_sq)
            self.assertEqual(in_sq.to_dictionary(), out_sq.to_dictionary())
            self.assertEqual(in_sq.__dict__, out_sq.__dict__)

    def test_save_to_file_csv_edge(self):
        '''Test save_to_file_csv() class method in edge cases'''

        r = Rectangle(4, 3, id=5)
        s1 = Square(4, 2, 2)
        s2 = Square(8, id=3)

        d_r = r.to_dictionary()
        d_s1 = s1.to_dictionary()
        d_s2 = s2.to_dictionary()

        # Passing None:

        Rectangle.save_to_file_csv(None)
        expected_csv = "id,width,height,x,y\n"

        with open('Rectangle.csv', 'r', encoding='utf-8') as f:
            self.assertEqual(f.read(), expected_csv)

        # Square in Rectangle.csv:

        with self.assertRaises(ValueError):
            Rectangle.save_to_file_csv([s1, s2])

        # Passing wrong arguments number:

        with self.assertRaises(TypeError):
            Square.save_to_file_csv('98', 'Street')

    def test_load_from_file_csv_edge(self):
        '''Test load_from_file_csv() class method in edge cases'''

        # Passing wrong arguments number:

        with self.assertRaises(TypeError):
            output_squares = Square.load_from_file_csv(0)

        # <Class>.json doesn't exist:

        output_rects = Rectangle.load_from_file_csv()
        self.assertEqual(output_rects, [])

        # Rectangle.json with squares JSON representations:

        s1 = Square(4, 6, 3)
        s2 = Square(1, 1, 3, 6)

        input_objs = [s1, s2]
        Square.save_to_file_csv(input_objs)

        os.rename('Square.csv', 'Rectangle.csv')

        with self.assertRaises(KeyError):
            output_objs = Rectangle.load_from_file_csv()

    def tearDown(self):
        '''Runs after every test function'''

        for file in glob.glob('*.csv'):
            try:
                os.remove(file)
            except OSError:
                pass
