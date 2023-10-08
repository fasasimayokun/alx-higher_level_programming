#include "lists.h"

listint_t *reverse_listint(listint_t **head);
int is_palindrome(listint_t **head);

/**
 * is_palindrome -  a func that check if a linked list is palindrome
 * @head: the starting point of the linked list
 * Return: -1(if linked list palindrome) else 0
 */
int is_palindrome(listint_t **head)
{
	listint_t *aux, *revs, *cen;
	size_t sz = 0, nm;

	if (*head == NULL || (*head)->next == NULL)
		return (1);
	aux = *head;
	while (aux)
	{
		sz++;
		aux = aux->next;
	}
	aux = *head;
	for (nm = 0; nm < (sz / 2) - 1; nm++)
		aux = aux->next;

	if ((sz % 2) == 0 && aux->n != aux->next->n)
		return (0);
	aux = aux->next->next;
	revs = reverse_listint(&aux);
	cen = revs;

	aux = *head;
	while (revs)
	{
		if (aux->n != revs->n)
			return (0);
		aux = aux->next;
		revs = revs->next;
	}
	reverse_listint(&cen);
	return (1);
}

/**
 * reverse_listint - a func that reverses the linked list
 * @head: the starting point of the linked list to reverse
 * Return: the head of the reversed list
 */
listint_t *reverse_listint(listint_t **head)
{
	listint_t *nd = *head, *next, *prv = NULL;

	while (nd)
	{
		next = nd->next;
		nd->next = prv;
		prv = nd;
		nd = next;
	}
	*head = prv;
	return (*head);
}
