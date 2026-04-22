/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   push_swap_utils.c                                  :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: beamarti <beamarti@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/03/03 11:17:05 by beamarti          #+#    #+#             */
/*   Updated: 2026/03/03 11:19:41 by beamarti         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

long	ft_atoi(const char *nptr)
{
	size_t	i;
	int		isnegative;
	long	result;

	result = 0;
	isnegative = 1;
	i = 0;
	while (nptr[i] == ' ' || (nptr[i] >= 9 && nptr[i] <= 13))
		i++;
	if (nptr[i] == '-' || nptr[i] == '+')
	{
		if (nptr[i] == '-')
			isnegative = -1 * isnegative;
		i++;
	}
	while (nptr[i] >= '0' && nptr[i] <= '9')
	{
		result = (result * 10) + (nptr[i] - '0');
		i++;
	}
	return (result * isnegative);
}

void	ft_putnbr(int n)
{
	long int	num;
	char		c;

	num = n;
	if (num < 0)
	{
		write(1, "-", 1);
		num = num * (-1);
	}
	if (num > 9)
		ft_putnbr(num / 10);
	c = num % 10 + '0';
	write(1, &c, 1);
}
