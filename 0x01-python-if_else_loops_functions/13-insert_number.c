#include "lists.h"
#include <stdlib.h>
#include <stddef.h>
/**
 *inser_node - inserts a number into sorted linked list
 *@head: a pointer head pointing to the first node
 *@number: a number to be inserted
 *Return: address of new node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node = NULL;
	listint_t *temp = *head;
	listint_t *prev = NULL;

	new_node = malloc(sizeof(listint_t));
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
		while (temp != NULL && temp->n < number)
		{
			prev = temp;
			temp = temp->next;
		}
		new_node->next = temp;
		prev->next = new_node;
	}
	return (new_node);
}
