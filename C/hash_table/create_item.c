#include "main.h"

/**
 * create_item - Create an item for the Hash Table
 * @key: Item key
 * @value: Item value
 *
 * Return: Item
 */

Ht_item *create_item(char *key, char *value)
{
	/* Create a pointer to a new hash table item */
	Ht_item *item = malloc(sizeof(Ht_item));

	item->key = malloc(strlen(key) + 1);
	item->value = malloc(strlen(value) + 1);

	strcpy(item->key, key);
	strcpy(item->value, value);

	return (item);
}
