/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_split_utils.c                                   :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: beamarti <beamarti@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/03/05 10:54:43 by beamarti          #+#    #+#             */
/*   Updated: 2026/03/05 10:54:44 by beamarti         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

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

size_t	ft_strlen(const char *s)
{
	size_t	i;

	i = 0;
	while (s[i] != '\0')
	{
		i++;
	}
	return (i);
}

char	*ft_strdup(const char *s)
{
	char	*result;
	size_t	s_len;

	s_len = ft_strlen(s);
	result = malloc((s_len + 1) * sizeof * result);
	if (result == NULL)
		return (NULL);
	ft_memcpy(result, s, s_len + 1);
	return (result);
}
