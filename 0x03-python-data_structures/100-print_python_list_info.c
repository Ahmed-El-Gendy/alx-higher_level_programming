#include <Python.h>
#include <object.h>
#include <listobject.h>

void print_python_list_info(PyObject *p) {
	long int size;
	PyListObject *list_obj;
	int i;
	PyObject *item;
	const char *type_name;

	list_obj = (PyListObject *)p;
	size = PyList_Size(p);

	printf("[*] Size of the Python List = %li\n", size);
	printf("[*] Allocated = %li\n", list_obj->allocated);

	for (i = 0; i < size; i++) {
		item = list_obj->ob_item[i];
		type_name = Py_TYPE(item)->tp_name;
		printf("Element %i: %s\n", i, type_name);
	}
}
