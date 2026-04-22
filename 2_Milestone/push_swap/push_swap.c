/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   push_swap.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: beamarti <beamarti@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/03/03 11:16:43 by beamarti          #+#    #+#             */
/*   Updated: 2026/03/09 10:46:40 by beamarti         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

int	fill_stack(t_list **stack, int ac, char **av)
{
	int		i;
	int		j;
	long	n;
	char	**token;

	i = 1;
	while (i < ac)
	{
		token = ft_split(av[i], ' ');
		if (!check_split(token))
			return (0);
		j = 0;
		while (token[j] != NULL)
		{
			if (!validate_and_convert(token[j], &n, token, stack))
				return (0);
			if (!insert_into_stack(n, stack, token))
				return (0);
			j++;
		}
		free_split(token);
		i++;
	}
	return (1);
}

void	ft_process_stack(t_list **stack_a, t_list **stack_b)
{
	int	size;

	size = ft_lstsize(*stack_a);
	if (size > 5)
	{
		ft_index(stack_a);
		ft_radix_sort(stack_a, stack_b);
	}
	else if (size == 2)
		ft_sort_two(stack_a);
	else if (size == 3)
		ft_sort_three(stack_a);
	else
		ft_sort_five(stack_a, stack_b);
}

int	ft_is_sorted(t_list *stack_a)
{
	while (stack_a && stack_a->next != NULL)
	{
		if (stack_a->value > stack_a->next->value)
			return (0);
		stack_a = stack_a->next;
	}
	return (1);
}

int	main(int ac, char **av)
{
	t_list	*stack_a;
	t_list	*stack_b;

	stack_a = NULL;
	stack_b = NULL;
	if (ac > 1)
	{
		if (!fill_stack(&stack_a, ac, av))
		{
			write(1, "Error\n", 6);
			ft_lstclear(&stack_a);
			return (1);
		}
		if (!ft_is_sorted(stack_a))
			ft_process_stack(&stack_a, &stack_b);
	}
	ft_lstclear(&stack_a);
	ft_lstclear(&stack_b);
	return (0);
}
