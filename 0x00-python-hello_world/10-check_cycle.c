#include "lists.h"
/**
 *check_cycle - checks a single linked list for a cycle or not
 *@list: linked list to be checked
 *Return: 0 if no cyle and 1 if there is cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *check1 = list;
	listint_t *check2 = list;

	while (check2 != NULL && check2->next != NULL)
	{
		check1 = check1->next;
		check2 = check2->next->next;
		if (check1 == check2)
			return (1);
	}
	return (0);
}
