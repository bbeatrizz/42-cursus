/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strlcat.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: beamarti <beamarti@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/13 12:28:36 by beamarti          #+#    #+#             */
/*   Updated: 2025/11/13 13:26:54 by beamarti         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

size_t	ft_strlcat(char *dest, const char *src, size_t size)
{
	size_t	src_len;
	size_t	dest_len;

	src_len = ft_strlen(src);
	dest_len = ft_strlen(dest);
	if (dest_len >= size)
		dest_len = size;
	if (dest_len == size)
		return (size + src_len);
	if (src_len < (size - dest_len))
	{
		ft_memcpy (dest + dest_len, src, src_len +1);
	}
	else
	{
		ft_memcpy (dest + dest_len, src, size - dest_len - 1);
		dest[size -1] = '\0';
	}
	return (dest_len + src_len);
}
