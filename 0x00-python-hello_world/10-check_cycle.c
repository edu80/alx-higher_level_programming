#include "lists.h"

/**
* check_cycle - Check if a linked list has a cycle in it.
* @list: Value check.
* Return: 0 if there is no cycle, 1 if there is a cycle.
*/

int check_cycle(listint_t *list)
{
listint_t *tortuga = list;
listint_t *conejo = list;
while (conejo && conejo->next)
{
tortuga = tortuga->next;
conejo = conejo->next->next;
if(tortuga == conejo)
return (1);
}
return (0);
}
