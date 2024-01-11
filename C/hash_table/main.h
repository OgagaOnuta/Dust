#ifndef MAIN_H
#define MAIN_H

#define CAPACITY 50000 /* Size of the Hash Table */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stddef.h>

/**
 * struct Ht_item - Create type Ht_item
 * @key: Item key
 * @value: Item value
 */

/* Define the Hash Table Item */
typedef struct Ht_item
{
	char *key;
	char *value;
} Ht_item;

/**
 * struct LinkedList - Create type LinkedList
 * @item: Pointer to current item in the list
 * @next: Pointer to next item in the list
 */

/* Define the Linked List */
typedef struct LinkedList
{
	Ht_item *item;
	struct LinkedList *next;
} LinkedList;

/**
 * struct HashTable - Create type HashTable
 * @items: Double pointer to items in the table
 * @overflow_buckets: Array of LinkedList pointers
 * @size: Table size
 * @count: Number of elements in the Hash Table
 */

/* Define the Hash Table */
typedef struct HashTable
{
	Ht_item **items;
	LinkedList **overflow_buckets;
	int size;
	int count;
} HashTable;

unsigned long hash_function(char *str);

Ht_item *create_item(char *key, char *value);
void free_item(Ht_item *item);

HashTable *create_table(int size);
void free_table(HashTable *table);

void ht_insert(HashTable *table, char *key, char *value);
char *ht_search(HashTable *table, char *key);
void ht_delete(HashTable *table, char *key);

void handle_collision(HashTable *table, unsigned long index, Ht_item *item);

void print_search(HashTable *table, char *key);
void print_table(HashTable *table);

LinkedList *allocate_list();
LinkedList *linkedlist_insert(LinkedList *list, Ht_item *item);
Ht_item *linkedlist_remove(LinkedList *list);
void free_linkedlist(LinkedList *list);

LinkedList **create_overflow_buckets(HashTable *table);
void free_overflow_buckets(HashTable *table);

#endif /* MAIN_H */
