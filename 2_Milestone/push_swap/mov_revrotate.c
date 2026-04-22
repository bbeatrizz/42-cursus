/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   mov_revrotate.c                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: beamarti <beamarti@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/03/03 11:16:53 by beamarti          #+#    #+#             */
/*   Updated: 2026/03/03 11:39:47 by beamarti         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

void	ft_revrotate(t_list **stack)
{
	t_list	*first;
	t_list	*last;
	t_list	*temp;

	if (!stack || !*stack || !(*stack)->next)
		return ;
	temp = *stack;
	while (temp->next && temp->next->next)
	{
		temp = temp->next;
	}
	last = temp->next;
	first = *stack;
	last->next = first;
	temp->next = NULL;
	*stack = last;
	write(1, "rra\n", 4);
}
