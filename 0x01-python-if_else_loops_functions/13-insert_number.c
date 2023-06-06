#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: pointer to pointer to singly linked list's head
 * @n: new number
 *
 * Return: pointer to the new node, NULL if an error occurs.
 */
listint_t *insert_node(listint_t **head, int n)
{
	listint_t *new;
	listint_t *current = *head;

	if (!head)
		return (NULL);

	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);
	new->n = n;
	/* If we must add the new node at the list is empty */
	if (!current)
	{
		new->next = current;
		*head = new;
		return (new);
	}
	/* If we must add it at the beginnig */
	if (n <= current->n)
	{
		new->next = current;
		*head = new;
		return (new);
	}
	/* In other cases */
	while (current->next)
	{
		if (n <= current->next->n)
		{
			new->next = current->next;
			current->next = new;
			return (new);
		}
		current = current->next;
	}
	/* We are at the end of the list*/
	current->next = new;
	new->next = NULL;

	return (new);
}
