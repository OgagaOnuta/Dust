#include "main.h"

/**
 * handle_collision - Handles collision in a hash table
 * @table: Hash table
 * @index: Index of item in hash table
 * @item: Item in hash table
 *
 * Return: void
 */

void handle_collision(HashTable *table, unsigned long index, Ht_item *item)
{
	LinkedList *head = table->overflow_buckets[index];

	if (head == NULL)
	{
		head = allocate_list(); /* Create list */
		head->item = item;
		table->overflow_buckets[index] = head;
		return;
	}
	else
	{
		/* Insert into the list */
		table->overflow_buckets[index] = linkedlist_insert(head, item);
		return;
	}
}
