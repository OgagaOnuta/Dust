#include "main.h"

/**
 * create_table - Create an empty Hash Table
 * @size: Table size
 *
 * Return: Hash Table
 */

HashTable *create_table(int size)
{
	/* Create a new Hash Table */
	HashTable *table = malloc(sizeof(HashTable));
	int i;

	table->size = size;
	table->count = 0;
	table->items = calloc(table->size, sizeof(Ht_item *));

	for (i = 0; i < table->size; i++)
		table->items[i] = NULL;

	table->overflow_buckets = create_overflow_buckets(table);

	return (table);
}
