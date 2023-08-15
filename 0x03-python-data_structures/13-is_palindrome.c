#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * reverse_list - function that reverses a list
 * @head: head of linked list
 * Return: Pointer to the new head of reversed list
 */
listint_t *reverse_list(listint_t *head)
{
	listint_t *prev = NULL;
	listint_t *current = head;
	listint_t *next;

	while (current != NULL)
	{
		next = current->next;
		current->next = head;
		prev = current;
		current = next;
	}
	return (prev);
}

/**
 * is_palindrome - function that checks if a linked list is a palindrome
 * @head: head of linked list
 *
 * Return: 0 if it's not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow = *head;
	listint_t *fast = *head;

	if (head == NULL || (*head)->next == NULL)
		return (1);

	while (fast != NULL && fast->next != NULL)
	{
		slow = slow-> next;
		fast = fast->next->next;
	}

	listint_t *firstHalf = *head;
	listint_t *secondHalf = slow;
	while (secondHalf != NULL)
	{
		if (firstHalf->n != secondHalf->n)
		return (0);
	}
	firstHalf = firstHalf->next;
	secondHalf = secondHalf->next;

	return (1);
}
