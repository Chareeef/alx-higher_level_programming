#include "lists.h"

/**
 * insert_nodeint - inserts a number into a sorted singly linked list
 * @head: pointer to pointer to singly linked list's head
 * @n: new number
 *
 * Return: pointer to the new node, NULL if an error occurs.
 */
listint_t *insert_node(listint_t **head, int n)
{
	listint_t *new;
	listint_t *current;

	if (!head)
		return (NULL);

	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);
	new->n = n;

	current = *head;

	/* if we must add the new node at the list's head */
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

	/* We are at the end of the list */
	current->next = new;
	new->next = NULL;

	return (new);
}
