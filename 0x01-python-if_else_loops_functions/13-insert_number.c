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
	listint_t *temp = NULL;

	temp = *head;
	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);
	new_node->n = number;
	if (*head == NULL)
	{
		new_node->next = *head;
		*head = new_node;
	}
	else
	{
		while (temp->next != NULL)
		{
			temp = temp->next;
		}
		temp->next = new_node;
	}
	return (new_node);
}
