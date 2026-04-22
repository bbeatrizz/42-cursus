/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_split.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: beamarti <beamarti@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/03/05 10:54:35 by beamarti          #+#    #+#             */
/*   Updated: 2026/03/05 11:38:52 by beamarti         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

char	*ft_substr(char const *s, unsigned int start, size_t len)
{
	size_t	len_s;
	size_t	i;
	char	*result;

	if (!s)
		return (NULL);
	len_s = ft_strlen(s);
	if (start > len_s)
		return (ft_strdup(""));
	if (len > len_s - start)
		len = len_s - start;
	result = malloc((len + 1) * (sizeof(char)));
	if (result == NULL)
		return (NULL);
	i = 0;
	while (i < len)
	{
		result[i] = s[start + i];
		i++;
	}
	result[i] = '\0';
	return (result);
}

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
