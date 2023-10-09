#include <Python.h>
#include <object.h>
#include <listobject.h>

/**
 * print_python_list_info - print
 * @PyObject: object
 * Return: void
 */
void print_python_list_info(PyObject *p)
{
	Py_ssize_t size;
	const char *type;

	size = PyList_Size(p);
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);
	for (Py_ssize_t i = 0; i < size; i++)
	{
		PyObject *item = PyList_GetItem(p, i);
		type_name = Py_TYPE(item)->tp_name;
		printf("Element %ld: %s\n", i, type_name);
	}
}
