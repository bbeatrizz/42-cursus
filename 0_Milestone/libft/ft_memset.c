/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_memset.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: beamarti <beamarti@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/11 12:12:40 by beamarti          #+#    #+#             */
/*   Updated: 2025/11/12 12:31:26 by beamarti         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

void	*ft_memset(void *s, int c, size_t n)
{
	unsigned char	*temp_s;

	temp_s = (unsigned char *) s;
	while (n > 0)
	{
		*temp_s = (unsigned char) c;
		n--;
		temp_s++;
	}
	return (s);
}
