#include "lists.h"

/**
 * check_cycle - checks if there is a cycle in a singly linked list using
 * Floyd's algorithm
 * @list: pointer to singly linked list's head
 *
 * Return: 1 if there is a cycle, 0 otherwise.
 */
int check_cycle(listint_t *list)
{
	listint_t *hare = list;
	listint_t *tortoise = list;

	while (hare && hare->next)
	{
		hare = hare->next->next;
		tortoise = tortoise->next;
		if (hare == tortoise)
		{
			return (1);
		}
	}

	return (0);
}
