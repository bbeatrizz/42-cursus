/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_memcpy.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: beamarti <beamarti@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/12 12:23:42 by beamarti          #+#    #+#             */
/*   Updated: 2025/11/13 11:16:49 by beamarti         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

/**
 * @brief Copies n bytes from the memory area src to the memory area dest.
 * 
 * @param dest 
 * @param src 
 * @param n 
 * @return void* 
 */
void	*ft_memcpy(void *dest, const void *src, size_t n)
{
	unsigned char			*temp_dest;
	const unsigned char		*temp_src;
	size_t					i;

	if (dest == NULL && src == NULL)
		return (dest);
	i = 0;
	temp_dest = (unsigned char *) dest;
	temp_src = (const unsigned char *) src;
	while (i < n)
	{
		temp_dest[i] = temp_src[i];
		i++;
	}
	return (dest);
}
