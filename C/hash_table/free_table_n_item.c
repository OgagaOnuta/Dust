#include "main.h"

/**
 * free_item - Free items from a table
 * @item: Item to be freed
 *
 * Return: void
 */

void free_item(Ht_item *item)
{
	/* Free an item */
	free(item->key);
	free(item->value);
	free(item);
}

/**
 * free_table - Free a table
 * @table: Table to be freed
 *
 * Return: void
 */

void free_table(HashTable *table)
{
	int i;

	/* Free the table */
	for (i = 0; i < table->size; i++)
	{
		Ht_item *item = table->items[i];

		if (item != NULL)
			free_item(item);
	}

	/* Free the overflow bucket linked list and it's items */
	free_overflow_buckets(table);
	free(table->items);
	free(table);
}
