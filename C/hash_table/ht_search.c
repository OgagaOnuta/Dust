#include "main.h"

/**
 * ht_search - Searches a Hash Table for a key
 * @table: Hash Table to be searched
 * @key: Key to be searched for
 *
 * Return: Value of key if found, NULL if not found
 */

char *ht_search(HashTable *table, char *key)
{
	int index = hash_function(key);
	Ht_item *item = table->items[index];
	LinkedList *head = table->overflow_buckets[index];

	/* Ensure that we move to items which are not NULL */
	while (item != NULL) /* Search for non-NULL items */
	{
		if (strcmp(item->key, key) == 0) /* Compare Keys */
			return (item->value); /* Key found */
		if (head == NULL)
			return (NULL);
		item = head->item;
		head = head->next;
	}
	return (NULL); /* Key not found */
}
