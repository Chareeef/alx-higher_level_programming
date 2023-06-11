#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to pointer of first node of listint_t list
 *
 * Return: 1 if the list is a palindrome (including empty ones), 0 otherwise.
 */
int is_palindrome(listint_t **head)
{
	listint_t *current = NULL;
	int *numbers;
	int size = 0, i, j;

	if (!head || !(*head))
		return (1);

	current = *head;
	while (current)
	{
		size++;
		current = current->next;
	}

	numbers = malloc(sizeof(int) * size);

	current = *head;
	for (i = 0; current; i++)
	{
		numbers[i] = current->n;
		current = current->next;
	}

	for (i = 0, j = size - 1; i <= size / 2; i++, j--)
	{
		if (numbers[i] != numbers[j])
			return (0);
	}

	free(numbers);

	return (1);
}
