/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_putnbr_fd.c                                     :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: beamarti <beamarti@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/26 11:26:17 by beamarti          #+#    #+#             */
/*   Updated: 2025/11/26 12:38:35 by beamarti         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

void	ft_putnbr_fd(int n, int fd)
{
	long int	num;
	char		c;

	num = n;
	if (num < 0)
	{
		ft_putchar_fd('-', fd);
		num = num * (-1);
	}
	if (num > 9)
		ft_putnbr_fd ((num / 10), fd);
	c = num % 10 + '0';
	ft_putchar_fd (c, fd);
}
