#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

listint_t *reverse_list(listint_t *head)
{
	listint_t *prev = NULL;
	listint_t *curr = head;
	listint_t *next;

	while (curr != NULL)
	{
		next = curr->next;
		curr->next = prev;
		prev = curr;
		curr = next;
	}
	return (prev);
}

int is_palindrome(listint_t **head)
{
	listint_t *fast = *head;
	listint_t *slow = *head;
	listint_t *first_half = *head;
	listint_t *second_half = slow;

	if (head == NULL || (*head)->next == NULL)
		return (1);

	while (fast != NULL && fast->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;
	}

	slow = reverse_list(slow);

	while (second_half != NULL)
	{
		if (first_half->n != second_half->n)
		{
			return (0);
		}
	first_half = first_half->next;
	second_half = second_half->next;
	}
	return (1);
}
