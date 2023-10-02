#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
#include <string.h>

/**
 * check_cycle - check if there is a cycle in list
 * @list: the list
 * Return: 0 if there is no cycle and 1 if failed
 */

int check_cycle(listint_t *list)
{
	listint_t *t = list, *g = list;

	if (!list)
		return (0);
	while (t && g)
	{
		if (!g->next)
			break;
		t = t->next;
		g = g->next->next;
		if (t == g)
			return (1);
	}
	return (0);
}
