#include "lists.h"
/**
 * insert_node - a func that inserts a num into a sorted linked list
 * @head: the address to the first node
 * @num: the int data to insert
 * Return: NULL else (ptr to the newnode)
 */
listint_t *insert_node(listint_t **head, int num)
{
	listint_t *node_list = *head, *newnode;

	newnode = malloc(sizeof(listint_t));
	if (newnode == NULL)
	{
		return (NULL);
	}
	newnode->n = num;

	if (node_list == NULL || node_list->n >= num)
	{
		newnode->next = node_list;
		*head = newnode;
		return (newnode);
	}

	while (node_list && node_list->next && node_list->next->n < num)
	{
		node_list = node_list->next;
	}
	newnode->next = node_list->next;
	node_list->next = newnode;

	return (newnode);
}
