/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_printnum.c                                      :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: beamarti <beamarti@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/04 13:24:12 by marvin            #+#    #+#             */
/*   Updated: 2025/12/11 12:33:51 by beamarti         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_printf.h"

int	ft_printnbr(int n)
{
	long int	num;
	char		c;
	int			len;

	len = 0;
	num = n;
	if (num < 0)
	{
		write(1, "-", 1);
		num = num * (-1);
		len++;
	}
	if (num > 9)
	{
		len += ft_printnbr (num / 10);
	}
	c = (num % 10) + '0';
	write(1, &c, 1);
	len++;
	return (len);
}
