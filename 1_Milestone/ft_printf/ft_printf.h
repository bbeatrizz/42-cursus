/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_printf.h                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: beamarti <beamarti@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/11 11:01:38 by beamarti          #+#    #+#             */
/*   Updated: 2026/01/15 13:21:40 by beamarti         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef FT_PRINTF_H
# define FT_PRINTF_H

# include <stdlib.h>
# include <unistd.h>
# include <stdarg.h>

int		ft_formats(va_list args, const char format);
int		ft_printf(const char *format, ...);
int		ft_printchar(int c);
int		ft_printf(const char *format, ...);
void	ft_putstr(char *s);
int		ft_printstr(char *str);
int		ft_printnbr(int n);
int		ft_printunisgned(unsigned int n);
int		ft_printhexa(unsigned long n, int uppercase);
int		ft_printptr(void *p);

#endif