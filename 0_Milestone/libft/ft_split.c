/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_split.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: beamarti <beamarti@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/19 13:25:56 by beamarti          #+#    #+#             */
/*   Updated: 2025/11/26 13:24:25 by beamarti         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

static int	count_words(char *str, char c)
{
	size_t	i;
	size_t	token;

	i = 0;
	token = 0;
	while (str[i] != '\0')
	{
		while (str[i] == c)
			i++;
		if (str[i] != '\0')
		{
			token++;
			while (str[i] != c && str[i] != '\0')
				i++;
		}
	}
	return (token);
}

static char	**ft_free_memory(char **matrix)
{
	int	i;

	i = 0;
	while (matrix[i])
	{
		free((void *)matrix[i]);
		i++;
	}
	free((void **)matrix);
	return (NULL);
}

static int	len_word(char *str, char c)
{
	size_t	len;

	len = 0;
	while (str[len] != c && str[len] != '\0')
		len++;
	return (len);
}

char	**ft_split(char const *s, char c)
{
	size_t	i;
	size_t	len_s;
	char	**matrix;

	matrix = malloc((count_words((char *)s, c) + 1) * (sizeof(char *)));
	if (!matrix || !s)
		return (NULL);
	i = 0;
	while (*s)
	{
		while (*s == c && *s)
			s++;
		len_s = len_word((char *)s, c);
		if (len_s > 0)
		{
			matrix[i] = ft_substr(s, 0, len_s);
			if (!matrix[i])
				return (ft_free_memory(matrix));
			s += len_s;
			i++;
		}
	}
	matrix[i] = NULL;
	return (matrix);
}
