#include "lists.h"

/**
 * check_cycle - function in C that checks if a singly linked list has a cycle in it
 * @list: linked list
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *aux = list, *p_list = list;

	while (aux != NULL && p_list != NULL && p_list->next != NULL)
	{
		aux = aux->next;
		p_list = p_list->next->next;
		if (aux == p_list)
        {
			return (1);
        }
	}
	return (0);
}
