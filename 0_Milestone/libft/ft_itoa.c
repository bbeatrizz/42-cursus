/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_itoa.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: beamarti <beamarti@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/24 11:29:25 by beamarti          #+#    #+#             */
/*   Updated: 2025/11/26 12:43:04 by beamarti         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

static int	is_negative(int n)
{
	int	sign;

	if (n < 0)
		sign = -1;
	else
		sign = 1;
	return (sign);
}

static int	number_len(int n)
{
	long	nb;
	int		len;

	len = 1;
	nb = n;
	if (nb < 0)
		nb = nb * (-1);
	while (nb >= 10)
	{
		nb = nb / 10;
		len++;
	}
	return (len);
}

static char	*allocate_itoa(int n)
{
	int		len;
	int		total;
	char	*s;

	len = number_len(n);
	if (is_negative(n) == -1)
		total = len + 1;
	else
		total = len;
	s = malloc((total + 1) * sizeof(char));
	if (!s)
		return (NULL);
	s[total] = '\0';
	return (s);
}

char	*ft_itoa(int n)
{
	int		total;
	char	*s;
	int		i;
	long	nb;

	nb = n;
	if (nb < 0)
		nb = nb * (-1);
	s = allocate_itoa(n);
	if (!s)
		return (NULL);
	total = number_len(n) + (is_negative(n) == -1);
	i = total - 1;
	if (nb == 0)
		s[i] = '0';
	while (nb > 0)
	{
		s[i] = nb % 10 + '0';
		nb = nb / 10;
		i--;
	}
	if (is_negative(n) == -1)
		s[0] = '-';
	return (s);
}
