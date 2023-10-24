#include <stdio.h>
#include <stdlib.h>
#include <Python.h>
#include <floatobject.h>

/**
 * print_python_float - a func that prints the info about the python float
 * @p: the addrs of pyobject struct
 * Return: void (nothing)
 */
void print_python_float(PyObject *p)
{
	double doub;

	setbuf(stdout, NULL);
	printf("{.} float object info\n");
	if (strcmp(p->ob_type->tp_name, "float"))
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}

	doub = ((PyFloatObject *)p)->ob_fval;
	printf("  value: %s\n", PyOS_double_to_string(doub, 'r',
				0, Py_DTSF_ADD_DOT_0, NULL));
}

/**
 * print_python_bytes - a func that prints the info about the python bytes
 * @p: the addrs of the Pyobject structure
 * Return: void(nothing)
 */
void print_python_bytes(PyObject *p)
{
	size_t nm, cnt, siz;
	char *st;

	setbuf(stdout, NULL);
	printf("[.] bytes object info\n");
	if (strcmp(p->ob_type->tp_name, "bytes"))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	siz = ((PyVarObject *)p)->ob_size;
	st = ((PyBytesObject *)p)->ob_sval;
	cnt = siz + 1 > 10 ? 10 : siz + 1;
	printf(" size: %lu\n", siz);
	printf(" trying string: %s\n", st);
	printf(" first %lu bytes: ", cnt);
	for (nm = 0; nm < cnt; nm++)
	{
		printf("%02hhx%s", st[nm], nm + 1 < cnt ? " " : "");
	}
	printf("\n");
}

/**
 * print_python_list - a func that prints the info about a python lists
 * @p: the addrs of the pyobject structure
 * Return: void(nothing)
 */
void print_python_list(PyObject *p)
{
	int nm;

	setbuf(stdout, NULL);
	printf("[*] Python list info\n");
	if (strcmp(p->ob_type->tp_name, "list"))
	{
		printf("  [ERROR] Invalid List Object\n");
		return;
	}
	printf("[*] Size of the Python List = %lu\n", ((PyVarObject *)p)->ob_size);
	printf("[*] Allocated = %lu\n", ((PyListObject *)p)->allocated);
	for (nm = 0; nm < ((PyVarObject *)p)->ob_size; nm++)
	{
		printf("Element %d: %s\n", nm,
				((PyListObject *)p)->ob_item[nm]->ob_type->tp_name);
		if (!strcmp(((PyListObject *)p)->ob_item[nm]->ob_type->tp_name, "bytes"))
		{
			print_python_bytes(((PyListObject *)p)->ob_item[nm]);
		}
		else if (!strcmp(((PyListObject *)p)->ob_item[nm]->ob_type->tp_name,
					"float"))
		{
			print_python_float(((PyListObject *)p)->ob_item[nm]);
		}
	}
}
