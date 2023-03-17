#include "main.h"

/**
 * allocate_list - Allocates memory for a LinkedList pointer
 *
 * Return: Allocated memory
 */

LinkedList *allocate_list()
{
	LinkedList *list = malloc(sizeof(LinkedList));

	return (list);
}

/**
 * linkedlist_insert - Inserts item into a linked List
 * @list: Linked list
 * @item: Item to be inserted
 *
 * Return: Linked list
 */

LinkedList *linkedlist_insert(LinkedList *list, Ht_item *item)
{
	LinkedList *temp = list;
	LinkedList *node = allocate_list();

	if (!list)
	{
		LinkedList *head = allocate_list();

		head->item = item;
		head->next = NULL;
		list = head;

		return (list);
	}
	else if (list->next == NULL)
	{
		LinkedList *node = allocate_list();

		node->item = item;
		node->next = NULL;
		list->next = node;

		return (list);
	}

	while (temp->next->next)
		temp = temp->next;

	node->item = item;
	node->next = NULL;
	temp->next = node;

	return (list);
}

/**
 * linkedlist_remove - Removes the head from the linked list
 * @list: Linked list to remove
 *
 * Return: Item of the popped element
 */

Ht_item *linkedlist_remove(LinkedList *list)
{
	LinkedList *node = list->next;
	LinkedList *temp = list;
	Ht_item *it = NULL;

	if (!list)
		return (NULL);
	if (!list->next)
		return (NULL);

	temp->next = NULL;
	list = node;
	memcpy(temp->item, it, sizeof(Ht_item));
	free(temp->item->key);
	free(temp->item->value);
	free(temp->item);
	free(temp);

	return (it);
}

/**
 * free_linkedlist - Frees a linked List
 * @list: Linked list to be freed
 *
 * Return: void
 */

void free_linkedlist(LinkedList *list)
{
	LinkedList *temp = list;

	while (list)
	{
		temp = list;
		list = list->next;
		free(temp->item->key);
		free(temp->item->value);
		free(temp->item);
		free(temp);
	}
}
