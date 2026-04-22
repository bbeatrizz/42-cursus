/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strlcpy.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: beamarti <beamarti@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/13 11:21:42 by beamarti          #+#    #+#             */
/*   Updated: 2025/11/14 11:10:08 by beamarti         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

size_t	ft_strlcpy(char *dest, const char *src, size_t size)
{
	size_t	src_len;

	src_len = ft_strlen(src);
	if (src_len + 1 < size)
	{
		ft_memcpy(dest, src, src_len +1);
	}
	else if (size != 0)
	{
		ft_memcpy(dest, src, size -1);
		dest[size -1] = 0;
	}
	return (src_len);
}
