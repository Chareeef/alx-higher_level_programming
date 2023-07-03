#!/usr/bin/python3 -u

import ctypes

lib = ctypes.CDLL('./libPython.so')
lib.print_python_list.argtypes = [ctypes.py_object]
lib.print_python_bytes.argtypes = [ctypes.py_object]
lib.print_python_float.argtypes = [ctypes.py_object]

f = 3.14
lib.print_python_float(f);
l = [-1.0, -0.1, 0.0, 1.0, 3.14, 3.14159, 3.14159265, 3.141592653589793238462643383279502884197169399375105820974944592307816406286]
print(l)
lib.print_python_list(l);
f = 3.141592653589793238462643383279502884197169399375105820974944592307816406286
print('\n## looong ##\n')
lib.print_python_float(f);
f = 3.1
print('\n## invalid ##\n')
lib.print_python_float(l);
print('\n## 3.1 ##\n')
lib.print_python_float(f);
