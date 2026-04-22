/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   mov_push.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: beamarti <beamarti@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/03/03 11:16:50 by beamarti          #+#    #+#             */
/*   Updated: 2026/03/03 11:39:28 by beamarti         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

void	ft_push(t_list **stack_a, t_list **stack_b)
{
	t_list	*first;

	if (!stack_a || !*stack_a)
		return ;
	first = *stack_a;
	*stack_a = first->next;
	first->next = *stack_b;
	*stack_b = first;
}

void	ft_pa(t_list **stack_b, t_list **stack_a)
{
	ft_push(stack_b, stack_a);
	write(1, "pa\n", 3);
}

void	ft_pb(t_list **stack_a, t_list **stack_b)
{
	ft_push(stack_a, stack_b);
	write(1, "pb\n", 3);
}
