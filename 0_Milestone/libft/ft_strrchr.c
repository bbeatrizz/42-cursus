/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strrchr.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: beamarti <beamarti@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/14 12:49:36 by beamarti          #+#    #+#             */
/*   Updated: 2025/11/14 13:20:31 by beamarti         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

char	*ft_strrchr(const char *s, int c)
{
	size_t	len_s;

	len_s = ft_strlen(s);
	while (1)
	{
		if ((unsigned char)s[len_s] == (unsigned char)c)
			return ((char *)&s[len_s]);
		if (len_s == 0)
			break ;
		len_s--;
	}
	return (NULL);
}
