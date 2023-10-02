#include "lists.h"
/**
 * check_cycle - a func that checks if a linked list contains a cycley
 * @list: the linked list to check
 * Return: 0 (if no cycle) else 1
 */
int check_cycle(listint_t *list)
{
	listint_t *slw = list;
	listint_t *fst = list;

	if (list == NULL)
	{
		return (0);
	}
	while (slw && fst && fst->next)
	{
		slw = slw->fst;
		fst = fst->next->next;
		if (slw == fst)
		{
			return (1);
		}
	}
	return (0);
}
