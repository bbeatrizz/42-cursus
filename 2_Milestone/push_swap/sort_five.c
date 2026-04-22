/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   sort_five.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: beamarti <beamarti@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/03/03 11:17:21 by beamarti          #+#    #+#             */
/*   Updated: 2026/03/05 11:03:20 by beamarti         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

void	ft_sort_three(t_list **stack)
{
	int	a;
	int	b;
	int	c;

	if (!stack || !*stack || !(*stack)->next || !(*stack)->next->next)
		return ;
	a = (*stack)->value;
	b = (*stack)->next->value;
	c = (*stack)->next->next->value;
	if (a < b && b < c)
		return ;
	else if (a > b && a > c)
		ft_ra(stack);
	else if (b > a && b > c)
		ft_revrotate(stack);
	if ((*stack)->value > (*stack)->next->value)
		ft_swap(stack);
}

t_list	*ft_findmin(t_list **stack)
{
	t_list	*temp;
	t_list	*min_node;

	if (!stack || !*stack)
		return (NULL);
	temp = *stack;
	min_node = temp;
	while (temp != NULL)
	{
		if (temp->value < min_node->value)
			min_node = temp;
		temp = temp->next;
	}
	return (min_node);
}

int	ft_locatemin(t_list **stack)
{
	t_list	*temp;
	t_list	*min_node;
	int		pos;

	if (!stack || !*stack)
		return (-1);
	min_node = ft_findmin(stack);
	temp = *stack;
	pos = 0;
	while (temp != min_node)
	{
		temp = temp->next;
		pos++;
	}
	return (pos);
}

void	ft_movemin(t_list **stack_a, t_list **stack_b)
{
	t_list	*min_node;
	int		pos;

	if (!stack_a || !*stack_a)
		return ;
	while (ft_lstsize(*stack_a) > 3)
	{
		min_node = ft_findmin(stack_a);
		while (*stack_a != min_node)
		{
			pos = ft_locatemin(stack_a);
			if (pos <= ft_lstsize(*stack_a) / 2)
				ft_ra(stack_a);
			else
				ft_revrotate(stack_a);
		}
		ft_pb(stack_a, stack_b);
	}
}

void	ft_sort_five(t_list **stack_a, t_list **stack_b)
{
	ft_movemin(stack_a, stack_b);
	ft_sort_three(stack_a);
	while (*stack_b)
	{
		ft_pa(stack_b, stack_a);
	}
}
