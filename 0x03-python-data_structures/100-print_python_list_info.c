#include <Python.h>
/**
 * print_python_list_info - a prog that prints a basic info about python
 * lists using c function
 * @p: the pyobject list
 * Return: void(nothing)
 */
void print_python_list_info(PyObject *p)
{
	int sz, mem_alloc, nm;
	PyObject *inst;

	sz = Py_SIZE(p);
	mem_alloc = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %d\n", sz);
	printf("[*] Allocated = %d\n", mem_alloc);
	for (nm = 0; nm < sz; nm++)
	{
		printf("Element %d: ", nm);
		inst = PyList_GetItem(p, nm);
		printf("%s\n", Py_TYPE(inst)->tp_name);
	}
}
