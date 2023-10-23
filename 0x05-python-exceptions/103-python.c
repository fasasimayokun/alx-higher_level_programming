#include <stdio.h>
#include <stdlib.h>
#include <Python.h>
#include <floatobject.h>

/**
 * print_python_float - a func that prints the info about the python float
 * @p: the addrs  of pyobject struct
 * Return: void (nothing)
 */
void print_python_float(PyObject *p)
{
	double doub;

	setbuf(stdout, NULL);
	printf("{.} float object info\n");
	if (strcmp
