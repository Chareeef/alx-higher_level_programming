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
	PyTypeObject *itemType = NULL;
	const char *typeName = NULL;

        len = PyList_Size(p);

        printf("[*] Size of the Python List = %ld\n", len);
        printf("[*] Allocated = %ld\n", list_ob->allocated);
        for (i = 0; i < len; i++)
        {
		itemType = Py_TYPE(list_ob->ob_item[i]);
		typeName = itemType->tp_name;

                printf("Element %ld: %s\n", i, typeName);
        }
}
