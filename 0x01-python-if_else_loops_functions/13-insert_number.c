#include "lists.h"
listint_t *insert_node(listint_t **head, int number)
{
	listint_t* ptr;
	if (*head == NULL)
	{
		return NULL;
	}
	if (*head->next == NULL)
	{
		add_nodeint_end(head, number);
	}

