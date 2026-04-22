/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   sort_radix.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: beamarti <beamarti@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/03/03 11:17:24 by beamarti          #+#    #+#             */
/*   Updated: 2026/03/03 11:44:59 by beamarti         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

static void	init_index(t_list *stack)
{
	while (stack)
	{
		stack->index = -1;
		stack = stack->next;
	}
}

void	ft_index(t_list **stack)
{
	int		n;
	t_list	*temp;
	t_list	*min_node;

	if (!stack || !*stack)
		return ;
	init_index(*stack);
	n = 0;
	while (n < ft_lstsize(*stack))
	{
		temp = *stack;
		min_node = NULL;
		while (temp != NULL)
		{
			if (temp->index == -1)
			{
				if (!min_node || temp->value < min_node->value)
					min_node = temp;
			}
			temp = temp->next;
		}
		min_node->index = n;
		n++;
	}
}

int	ft_maxbit(t_list *stack)
{
	int		bit;
	int		max_bits;
	t_list	*temp;

	bit = 0;
	if (!stack)
		return (0);
	temp = stack;
	max_bits = temp->index;
	temp = temp->next;
	while (temp != NULL)
	{
		if (temp->index > max_bits)
			max_bits = temp->index;
		temp = temp->next;
	}
	while (max_bits > 0)
	{
		max_bits = max_bits / 2;
		bit++;
	}
	return (bit);
}

void	ft_radix_sort(t_list **stack_a, t_list **stack_b)
{
	int	size;
	int	i;
	int	count;
	int	max_bits;

	if (!stack_a || !*stack_a)
		return ;
	max_bits = ft_maxbit(*stack_a);
	i = 0;
	while (i < max_bits)
	{
		size = ft_lstsize(*stack_a);
		count = 0;
		while (count < size)
		{
			if (((*stack_a)->index >> i) & 1)
				ft_ra(stack_a);
			else
				ft_pb(stack_a, stack_b);
			count++;
		}
		while (*stack_b)
			ft_pa(stack_b, stack_a);
		i++;
	}
}
