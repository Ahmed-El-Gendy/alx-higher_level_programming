#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * is_palindrome - check if list is palindrome
 * @head: head
 * Return: int
 */

int is_palindrome(listint_t **head)
{
	int i, n, *arr;
	const listint_t *current;

	n = 0;
	arr = malloc(sizeof(int) * 5000);
	current = *(head);
	while (current != NULL)
	{
		arr[n] = current->n;
		current = current->next;
		n++;
	}
	for (i = 0; i < n; i++)
	{
		if (arr[i] != arr[n - i - 1])
		{
			free(arr);
			return (0);
		}
	}
	free(arr);
	return (1);
}
