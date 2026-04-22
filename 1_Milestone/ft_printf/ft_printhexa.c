/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_printhexa.c                                     :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: marvin <marvin@student.42.fr>              +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/12 10:39:20 by marvin            #+#    #+#             */
/*   Updated: 2025/12/12 10:39:20 by marvin           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_printf.h"

int	ft_printhexa(unsigned long n, int uppercase)
{
	char	*hex;
	char	c;
	int		count;

	if (uppercase == 1)
		hex = "0123456789ABCDEF";
	else
		hex = "0123456789abcdef";
	count = 0;
	if (n >= 16)
		count += ft_printhexa(n / 16, uppercase);
	c = hex[n % 16];
	write(1, &c, 1);
	return (count + 1);
}
