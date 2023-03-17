#include "main.h"

/**
 * print_search - Searches for a key in a Hash Table
 * and prints the key and value
 * @table: Table to be searched
 * @key: Key to be searched for
 *
 * Return: void
 */

void print_search(HashTable *table, char *key)
{
	char *val = ht_search(table, key);

	if (val == NULL)
	{
		printf("Key: %s does not exist\n", key);
		return;
	}
	else
	{
		printf("Key: %s, Value: %s\n", key, val);
	}
}
