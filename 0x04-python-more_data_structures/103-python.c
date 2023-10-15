#include <stdio.h>
#include <Python.h>

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);

/**
 * print_python_bytes - a func that prints bytes info
 * @p: the python obj
 * Return: void(nothing)
 */
void print_python_bytes(PyObject *p)
{
	char *st;
	long int len, n, lmt;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf(" [ERROR] Invalid Bytes Object\n");
		return;
	}

	len = ((PyVarObject *)(p))->ob_size;
	st = ((PyBytesObject *)p)->ob_sval;

	printf(" size: %ld\n", len);
	printf(" trying string: %s\n", st);

	if (len >= 10)
		lmt = 10;
	else
	{
		lmt = len + 1;
	}

	printf(" first %ld bytes:", lmt);
	for (n = 0; n < lmt; n++)
	{
		if (st[n] >= 0)
			printf(" %02x", st[n]);
		else
			printf(" %02x", 256 + st[n]);
	}
	printf("\n")
}

/**
 * print_python_list - a func that prints list infor
 * @p: the python obj
 * Return: void(nothing)
 */
void print_python_list(PyObject *p)
{
	long int len, nm;
	PyListObject *ls;
	PyObject *inst;

	len = ((PyVarObject *)(p))->ob_size;
	ls = (PyListObject *)p;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", len);
	printf("[*] Allocated = %ld\n", ls->allocated);

	for (nm = 0; nm < len; nm++)
	{
		inst = ((PyListObject *)p)->ob_item[nm];
		printf("Element %ld: %s\n", nm, ((inst)->ob_type)->tp_name);
		if (PyBytes_Check(inst))
		{
			print_python_bytes(inst);
		}
	}
}
