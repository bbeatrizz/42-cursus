/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   get_next_line_utils.c                              :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: beamarti <beamarti@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/16 10:54:16 by beamarti          #+#    #+#             */
/*   Updated: 2026/01/15 12:26:59 by beamarti         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "get_next_line.h"

char	*ft_strdup(const char *s)
{
	char			*result;
	size_t			s_len;
	unsigned int	i;

	s_len = ft_strlen(s);
	result = malloc((s_len + 1) * sizeof * result);
	if (result == NULL)
		return (NULL);
	i = 0;
	while (s[i])
	{
		result[i] = s[i];
		i++;
	}
	result[i] = 0;
	return (result);
}

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

char	*ft_strchr(const char *s, int c)
{
	size_t	i;

	i = 0;
	while (s[i] != '\0')
	{
		if (s[i] == (char)c)
			return ((char *)&s[i]);
		i++;
	}
	if ((char )c == '\0')
		return ((char *)&s[i]);
	return (NULL);
}
