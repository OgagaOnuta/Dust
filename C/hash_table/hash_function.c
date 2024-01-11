#include "main.h"

/**
 * hash_function - Index a Hash Table
 * @str: Data or arbitrary size
 *
 * Return: Hash Table index
 */

unsigned long hash_function(char *str)
{
	unsigned long i = 0;
	int j;

	for (j = 0; str[j]; j++)
		i += str[j];
	return (i % CAPACITY);
}
