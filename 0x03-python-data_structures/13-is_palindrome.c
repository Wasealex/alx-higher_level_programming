#include "lists.h"
/**
 *is_palindrome - checks if a singly linked list is a palindrome
 *@head: is a pointer pointing to the first node
 *Return: 0 if it is not a palindrome
 *1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *current = NULL, *temp = NULL;
	int *array_data;
	int count = 0;
	int i;

	current = temp = *head;
	if (current == NULL)
	{
		return (1);
	}
	while (temp != NULL)
	{
		count++;
		temp = temp->next;
	}
	array_data = malloc(sizeof(int) * count);
	if (array_data == NULL)
		return (-1);
	for (i = 0; i < count; i++)
	{
		array_data[i] = current->n;
		current = current->next;
	}
	for (i = 0; i <= count / 2; i++)
	{
		if (array_data[i] != array_data[count - i - 1])
		{
			free(array_data);
			return (0);
		}
	}

	free(array_data);
	return (1);
}
