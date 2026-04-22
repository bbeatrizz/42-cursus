/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_printf.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: beamarti <beamarti@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/04 11:06:09 by marvin            #+#    #+#             */
/*   Updated: 2026/01/19 11:15:39 by beamarti         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_printf.h"

int	ft_printchar(int c)
{
	write(1, &c, 1);
	return (1);
}

int	ft_formats(va_list args, const char format)
{
	int	len;

	len = 0;
	if (format == 'c')
		len += ft_printchar(va_arg(args, int));
	else if (format == 's')
		len += ft_printstr(va_arg(args, char *));
	else if (format == 'p')
		len += ft_printptr(va_arg(args, void *));
	else if (format == 'd' || format == 'i')
		len += ft_printnbr(va_arg(args, int));
	else if (format == 'u')
		len += ft_printunisgned(va_arg(args, unsigned int));
	else if (format == 'x')
		len += ft_printhexa(va_arg(args, unsigned int), 0);
	else if (format == 'X')
		len += ft_printhexa(va_arg(args, unsigned int), 1);
	else if (format == '%')
		len += ft_printchar('%');
	return (len);
}

int	ft_printf(const char *format, ...)
{
	size_t	i;
	int		len;
	va_list	args;

	va_start(args, format);
	i = 0;
	len = 0;
	while (format[i])
	{
		if (format[i] != '%')
		{
			len += ft_printchar(format[i]);
			i++;
		}
		else
		{
			len += ft_formats(args, format[i + 1]);
			i = i + 2;
		}
	}
	va_end(args);
	return (len);
}
