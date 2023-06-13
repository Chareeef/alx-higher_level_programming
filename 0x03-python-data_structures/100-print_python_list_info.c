#include <stdio.h>
#include <Python.h>
#include <object.h>
#include <listobject.h>

/**
 * print_python_list_info - prints some basic info about Python lists
 * @p: a Python list object
 */
void print_python_list_info(PyObject *p)
{
        Py_ssize_t i, len;
	PyListObject *list_ob = (PyListObject *) p;
        PyObject *item = NULL;

        len = PyList_Size(p);

        printf("[*] Size of the Python List = %ld\n", len);
        printf("[*] Allocated = %ld\n", list_ob->allocated);
        for (i = 0; i < len; i++)
        {
                item = PyList_GetItem(p, i);
		if (PyLong_Check(item))
                	printf("Element %ld is: int\n", i);
		else if (PyFloat_Check(item))
                	printf("Element %ld is: float\n", i);
		else if (PyUnicode_Check(item))
                	printf("Element %ld is: str\n", i);
		else if (PyList_Check(item))
                	printf("Element %ld is: list\n", i);
		else if (PyTuple_Check(item))
                	printf("Element %ld is: tuple\n", i);
		else if (PySet_Check(item))
                	printf("Element %ld is: set\n", i);
		else if (PyDict_Check(item))
                	printf("Element %ld is: dict\n", i);
        }
}
