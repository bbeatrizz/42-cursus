/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_memmove.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: beamarti <beamarti@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/12 12:41:23 by beamarti          #+#    #+#             */
/*   Updated: 2025/11/13 11:19:07 by beamarti         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

void	*ft_memmove(void *dest, const void *src, size_t n)
{
	unsigned char		*temp_dest;
	const unsigned char	*temp_src;
	size_t				i;

	temp_dest = (unsigned char *)dest;
	temp_src = (const unsigned char *) src;
	if (dest == NULL && src == NULL)
		return (NULL);
	if (temp_dest > temp_src)
	{
		while (n--)
		{
			temp_dest[n] = temp_src[n];
		}
	}
	else
	{
		i = 0;
		while (i < n)
		{
			temp_dest[i] = temp_src[i];
			i++;
		}
	}
	return (dest);
}
