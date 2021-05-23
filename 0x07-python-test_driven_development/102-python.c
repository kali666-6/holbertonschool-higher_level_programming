#include <Python.h>

void print_python_string(PyObject *p)
{
	long int len;

	printf("[.] string object info\n");

	if (strcmp(p->ob_type->tp_name, "str") != 0)
	{
		printf("  [ERROR] Invalid String Object\n");
		return;
	}

	if (PyUnicode_IS_COMPACT_ASCII(p))
		printf("  type: compact ascii\n");
	else
		printf("  type: compact unicode object\n");
	len = ((PyASCIIObject*)p)->length;
	printf("  length: %ld\n", len);
	printf("  value: %s\n", PyUnicode_AsUTF8AndSize(p, &len));
}
