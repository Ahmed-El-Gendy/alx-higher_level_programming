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
	if (temp == NULL)
	{
		list->next = (*head);
		(*head) = node;
		return (*head);
	}
	while (temp)
	{
		if (temp->n < n && (temp->next->n >= n || temp->next == NULL))
		{
			list->next = temp->next;
			temp->next = list;
			return (list);
		}
		temp = temp->next;
	}
	free(list);
	return (NULL);
}
