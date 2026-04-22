/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_memchr.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: beamarti <beamarti@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/14 13:24:15 by beamarti          #+#    #+#             */
/*   Updated: 2025/11/14 13:46:27 by beamarti         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

void	*ft_memchr(const void *s, int c, size_t n)
{
	unsigned char	*temp_s;
	unsigned char	uc;
	size_t			i;

	temp_s = (unsigned char *) s;
	uc = (unsigned char) c;
	i = 0;
	while (i < n)
	{
		if (temp_s[i] == uc)
			return ((void *) &temp_s[i]);
		i++;
	}
	return (NULL);
}
