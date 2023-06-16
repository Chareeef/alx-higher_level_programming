#include <Python.h>
#include <stdio.h>

/**
 * print_python_bytes - print infos about a Python bytes
 * @p: a Python Object
 */
void print_python_bytes(PyObject *p)
{
	unsigned int size, i;
	char *string;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("\t[ERROR] Invalid Bytes Object\n");
		return;
	}
	size = (unsigned int) ((PyVarObject *) p)->ob_size;
	string = PyBytes_AsString(p);

	printf("\tsize: %u\n", size);
	printf("\ttrying string: %s\n", string);
	printf("\tfirst 9 bytes:");
	for (i = 0; i < 9 && string[i] != '\0'; i++)
		printf(" %x", string[i]);
	printf("\n");
}

/*
[.] bytes object info
  size: 8
  trying string: �
  first 9 bytes: ff f8 00 00 00 00 00 00 00
*/

/* ----- */

/**
 * print_python_list - print infos about a Python list
 * @p: a Python Object
 */
void print_python_list(PyObject *p)
{
	PyListObject *list = (PyListObject *) p;
	PyObject *item;
	unsigned int size = (unsigned int) ((PyVarObject *) p)->ob_size;
	unsigned int allocated = (unsigned int) list->allocated;
	const char *type_name;
	unsigned int i;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %u\n", size);
	printf("[*] Allocated = %u\n", allocated);

	for (i = 0; i < size; i++)
	{
		item = list->ob_item[i];
		type_name = item->ob_type->tp_name;
		printf("Element %u: %s\n", i, type_name);
		if (PyBytes_Check(item))
				print_python_bytes(item);
	}
}
/*
[*] Python list info
[*] Size of the Python List = 2
[*] Allocated = 2
Element 0: bytes
*/
