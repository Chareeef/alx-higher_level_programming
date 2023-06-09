#include <Python.h>
#include <stdio.h>

/**
 * print_python_bytes - print infos about a Python bytes
 * @p: a Python Object
 */
void print_python_bytes(PyObject *p)
{
	unsigned int size, str_length, i;
	char *string;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	size = (unsigned int) ((PyVarObject *) p)->ob_size;
	string = ((PyBytesObject *) p)->ob_sval;
	str_length = size + 1;
	if (str_length > 10)
		str_length = 10;

	printf("  size: %u\n", size);
	printf("  trying string: %s\n", string);
	printf("  first %u bytes:", str_length);
	for (i = 0; i < str_length; i++)
		printf(" %02x", (unsigned char) string[i]);
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
