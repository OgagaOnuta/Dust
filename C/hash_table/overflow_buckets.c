#include "main.h"

/**
 * create_overflow_buckets - Creates the overflow buckets
 * @table: Hash table
 *
 * Return: Overflow buckets
 */

LinkedList **create_overflow_buckets(HashTable *table)
{
	LinkedList **buckets = calloc(table->size, sizeof(LinkedList *));
	int i;

	for (i = 0; i < table->size; i++)
		buckets[i] = NULL;

	return (buckets);
}

/**
 * free_overflow_buckets - Frees all overflow bucket lists
 * @table: Hash table
 *
 * Return: void
 */

void free_overflow_buckets(HashTable *table)
{
	LinkedList **buckets = table->overflow_buckets;
	int i;

	for (i = 0; i < table->size; i++)
		free_linkedlist(buckets[i]);

	free(buckets);
}
