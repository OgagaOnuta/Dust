#include "main.h"

/**
 * ht_insert - Insert an item into a Hash Table
 * @table: Hast Table to be inserted
 * @key: Item key
 * @value: Item value
 *
 * Return: void
 */

void ht_insert(HashTable *table, char *key, char *value)
{
	Ht_item *item = create_item(key, value); /* Create the item */
	int index = hash_function(key); /* Compute the index */
	Ht_item *current_item = table->items[index];

	if (current_item == NULL) /* Key does not exist */
	{
		if (table->count == table->size) /* Hash Table full */
		{
			printf("Insert Error: Hash Table is full\n");
			free_item(item);
			return;
		}

		table->items[index] = item; /* Insert directly */
		table->count++;
	}
	else /* Key already exists */
	{
		if (strcmp(current_item->key, key) == 0) /* Compared keys are the same */
		{
			strcpy(table->items[index]->value, value); /* Update value */
			return;
		}
		else /* Compared keys are different */
		{
			handle_collision(table, index, item); /* Handle the collision */
			return;
		}
	}
}
