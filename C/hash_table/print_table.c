#include "main.h"

/**
 * print_table - Prints a Hash Table
 * @table: Table to be printed
 *
 * Return: void
 */

void print_table(HashTable *table)
{
	int i;

	printf("\nHash Table\n----------------------------------------\n");
	for (i = 0; i < table->size; i++)
	{
		if (table->items[i])
		{
			printf("Index: %d, Key: %s, Value: %s",
			       i, table->items[i]->key, table->items[i]->value);
			if (table->overflow_buckets[i])
			{
				LinkedList *head = table->overflow_buckets[i];

				printf(" => Overflow Bucket => ");
				while (head)
				{
					printf("Key: %s, Value: %s",
					       head->item->key, head->item->value);
					head = head->next;
				}
			}
			printf("\n");
		}
	}
	printf("----------------------------------------\n\n");
}
