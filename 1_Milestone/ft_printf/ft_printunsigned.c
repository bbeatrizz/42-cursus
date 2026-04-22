/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_printunsigned.c                                 :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: marvin <marvin@student.42.fr>              +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/12 10:37:48 by marvin            #+#    #+#             */
/*   Updated: 2025/12/12 10:37:48 by marvin           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_printf.h"

int	ft_printunisgned(unsigned int n)
{
	char	c;
	int		count;

	count = 0;
	if (n >= 10)
		count += ft_printunisgned(n / 10);
	c = (n % 10) + '0';
	count += write(1, &c, 1);
	return (count);
}
