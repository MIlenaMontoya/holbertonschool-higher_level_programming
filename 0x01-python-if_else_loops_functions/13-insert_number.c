#include "lists.h"
/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: head of linked list
 * @number: number insert in the linked list
 *
 * Return: Address of the new node or null if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node_aux = *head, *new;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
	{
		return (NULL);
	}
	new->n = number;
	if (*head == NULL || node_aux->n >= number)
	{
		new->next = node_aux;
		*head = new;
		return (new);
	}
	while (node_aux->next != NULL && node_aux->next->n <= number)
	{
		node_aux = node_aux->next;
	}
	new->next = node_aux->next;
	node_aux->next = new;
	return (new);
}
