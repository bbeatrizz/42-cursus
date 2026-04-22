/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_printptr.c                                      :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: beamarti <beamarti@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/04 13:09:30 by marvin            #+#    #+#             */
/*   Updated: 2025/12/11 13:07:17 by beamarti         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_printf.h"

int	ft_printptr(void *p)
{
	unsigned long	ptr;
	int				len;

	if (!p)
	{
		ft_putstr("(nil)");
		return (5);
	}
	ptr = (unsigned long)p;
	len = ft_printstr("0x");
	len += ft_printhexa(ptr, 0);
	return (len);
}
