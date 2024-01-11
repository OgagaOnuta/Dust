#include "main.h"

/**
 * ht_delete - Deletes an item from a Hash table
 * @table: Hash table
 * @key: Key of item to be deleted
 *
 * Return: void
 */

void ht_delete(HashTable *table, char *key)
{
	int index = hash_function(key);
	Ht_item *item = table->items[index];
	LinkedList *head = table->overflow_buckets[index];

	if (item != NULL)
	{
		if (head == NULL && strcmp(item->key, key) == 0) /* No collision chain. */
		{
			table->items[index] = NULL; /* Set table index to NULL */
			free_item(item);
			table->count--;
			return;
		}
		else if (head != NULL) /* Collision chain exists */
		{
			LinkedList *curr = head;
			LinkedList *prev = NULL;

			/* Remove the item and set the head of the list as the new item */
			if (strcmp(item->key, key) == 0)
			{
				LinkedList *node = head;

				free_item(item);
				head = head->next;
				node->next = NULL;
				table->items[index] = create_item(node->item->key, node->item->value);
				free_linkedlist(node);
				table->overflow_buckets[index] = head;
				return;
			}
			while (curr)
			{
				if (strcmp(curr->item->key, key) == 0)
				{
					if (prev == NULL) /* First element of the chain */
					{
						free_linkedlist(head); /* Remove the chain */
						table->overflow_buckets[index] = NULL;
						return;
					}
					else if (prev != NULL)
					{
						prev->next = curr->next;
						curr->next = NULL;
						free_linkedlist(curr);
						table->overflow_buckets[index] = head;
						return;
					}
				}
				curr = curr->next;
				prev = curr;
			}
		}
	}
}
