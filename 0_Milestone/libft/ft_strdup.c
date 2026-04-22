/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strdup.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: beamarti <beamarti@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/17 11:22:00 by beamarti          #+#    #+#             */
/*   Updated: 2025/11/17 11:43:56 by beamarti         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

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
