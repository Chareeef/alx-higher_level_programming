#include "lists.h"

/**
 * reverse_linked_list - reverse a singly linked list
 * @head: pointer of first node of listint_t list
 *
 * Return: a pointer of first node of listint_t list.
 */
listint_t *reverse_linked_list(listint_t *head)
{
	listint_t *current = NULL, *prev_node = NULL, *next_node = NULL;

	if (!head)
		return (NULL);

	current = head;
	while (current)
	{
		next_node = current->next;
		current->next = prev_node;
		prev_node = current;
		current = next_node;
		if (!next_node)
			head = prev_node;
	}

	return (head);
}

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to pointer of first node of listint_t list
 *
 * Return: 1 if the list is a palindrome (including empty ones), 0 otherwise.
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow = NULL, *fast = NULL;
	listint_t *end_first_list = NULL, *start_second_list = NULL;

	if (!head || !(*head) || !(*head)->next)
		return (1);
	slow = *head, fast = *head;
	/* Split the list at the middle */
	while (1)
	{
		fast =  fast->next->next;
		if (fast == NULL)
		{
			start_second_list = slow->next;
			end_first_list = slow;
			break;
		}
		else if (fast->next == NULL)
		{
			start_second_list = slow->next->next;
			end_first_list = slow->next;
			break;
		}
		slow = slow->next;
	}
	/* Reverse the second list */
	start_second_list = reverse_linked_list(start_second_list);
	end_first_list->next = start_second_list;
	/* Compare the two lists */
	for (slow = *head, fast = start_second_list; fast != NULL;
			fast = fast->next, slow = slow->next)
	{
		if (slow->n != fast->n)
		{
			end_first_list->next = reverse_linked_list(start_second_list);
			return (0);
		}
	}
	end_first_list->next = reverse_linked_list(start_second_list);

	return (1);
}
