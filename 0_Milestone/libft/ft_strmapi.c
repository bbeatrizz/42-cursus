/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strmapi.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: beamarti <beamarti@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/24 17:14:28 by beamarti          #+#    #+#             */
/*   Updated: 2025/11/26 12:36:54 by beamarti         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

char	*ft_strmapi(char const *s, char (*f)(unsigned int, char))
{
	char		*temp;
	size_t		i;
	size_t		len;

	len = ft_strlen(s);
	temp = malloc(sizeof(char) * (len + 1));
	if (!temp)
		return (NULL);
	i = 0;
	while (i < len)
	{
		temp[i] = f(i, s[i]);
		i++;
	}
	temp[i] = '\0';
	return (temp);
}
