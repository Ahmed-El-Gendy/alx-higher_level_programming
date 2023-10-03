#include "lists.h"

/**
 * insert_nodeint_at_index - insert node at index
 * @head: pointer
 * @idx: index
 * @n: int
 * Return: pointer
 */

listint_t *insert_node(listint_t **head, int n)
{
	listint_t *temp, *list;

	list = malloc(sizeof(listint_t));

	temp = *head;
	if (list == NULL)
		return (NULL);
	list->n = n;
	if (temp == NULL || temp->n >= n)
	{
		list->next = (*head);
		(*head) = list;
		return (*head);
	}
	while (temp->next)
	{
		if (temp->next->n >= n || temp->next == NULL)
		{
			list->next = temp->next;
			temp->next = list;
			return (list);
		}
		temp = temp->next;
	}
	temp->n = n;
	temp->next = NULL;
	temp->next = list;
	free(list);
	return (NULL);
}
