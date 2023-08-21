#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - function that inserts a number into a sorted linked list
 * @head: pointer to linked list
 * @number: number to insert
 *
 * Return: the address of the new node or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node = (listint_t *)malloc(sizeof(listint_t));
	listint_t *current;

	if (new_node == NULL)
		return (NULL);

	new_node->n = number;
	new_node->next = NULL;

	if (*head == NULL || (*head)->n >= number)
	{
		new_node->next = *head;
		*head = new_node;
	}
	else
	{
		current = *head;
		while (current->next != NULL && current->next->n < number)
		{

			current = current->next;
		}
		new_node->next = current->next;
		current->next = new_node;
	}
	return (new_node);
}
