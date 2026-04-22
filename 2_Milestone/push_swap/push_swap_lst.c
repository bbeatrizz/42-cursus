/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   push_swap_lst.c                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: beamarti <beamarti@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/03/03 11:17:03 by beamarti          #+#    #+#             */
/*   Updated: 2026/03/05 12:32:56 by beamarti         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

t_list	*ft_lstnew(int value)
{
	t_list	*node;

	node = malloc(sizeof(t_list));
	if (!node)
		return (NULL);
	node->value = value;
	node->next = NULL;
	return (node);
}

t_list	*ft_lstlast(t_list *lst)
{
	t_list	*temp;

	if (!lst)
		return (NULL);
	temp = lst;
	while (temp->next != NULL)
		temp = temp->next;
	return (temp);
}

void	ft_lstadd_back(t_list **lst, t_list *new)
{
	if (!lst || !new)
		return ;
	if (*lst)
		(ft_lstlast(*lst))->next = new;
	else
		*lst = new;
}

void	ft_printlst(t_list *stack)
{
	t_list	*temp;

	temp = stack;
	while (temp != NULL)
	{
		ft_putnbr(temp -> value);
		if (temp->next != NULL)
			write(1, " ", 1);
		temp = temp->next;
	}
	write(1, "\n", 1);
}

int	ft_lstsize(t_list *lst)
{
	size_t	count;
	t_list	*temp;

	temp = lst;
	count = 0;
	while (temp)
	{
		count++;
		temp = temp->next;
	}
	return (count);
}
