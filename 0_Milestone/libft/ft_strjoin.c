/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strjoin.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: beamarti <beamarti@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/18 12:25:09 by beamarti          #+#    #+#             */
/*   Updated: 2025/11/18 12:54:13 by beamarti         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

char	*ft_strjoin(char const *s1, char const *s2)
{
	size_t	s1_len;
	size_t	s2_len;
	char	*result;
	size_t	i;
	size_t	j;

	s1_len = ft_strlen(s1);
	s2_len = ft_strlen(s2);
	result = malloc(((s1_len + s2_len) + 1) * (sizeof(char)));
	if (!result || !s1 || !s2)
		return (NULL);
	i = 0;
	while (i < s1_len)
	{
		result[i] = s1[i];
		i++;
	}
	j = 0;
	while (j < s2_len)
	{
		result[i + j] = s2[j];
		j++;
	}
	result[i + j] = '\0';
	return (result);
}
