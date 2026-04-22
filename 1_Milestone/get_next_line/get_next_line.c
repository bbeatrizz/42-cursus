/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   get_next_line.c                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: beamarti <beamarti@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/16 10:54:14 by beamarti          #+#    #+#             */
/*   Updated: 2026/01/21 12:57:43 by beamarti         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "get_next_line.h"

char	*set_line(char **line_buffer)
{
	int		i;
	char	*nline;
	char	*new_buffer;

	i = 0;
	if (!*line_buffer)
		return (NULL);
	while ((*line_buffer)[i] != '\0' && (*line_buffer)[i] != '\n')
		i++;
	if ((*line_buffer)[i] == '\n')
		i++;
	nline = ft_substr(*line_buffer, 0, i);
	if (ft_strlen(*line_buffer) > (size_t)i)
		new_buffer = ft_substr(*line_buffer, i,
				ft_strlen(*line_buffer) - i);
	else
		new_buffer = NULL;
	free(*line_buffer);
	*line_buffer = new_buffer;
	return (nline);
}

char	*join_buffer(char *buffer, char *buffer_temp)
{
	char	*old_buffer;

	if (!buffer)
		buffer = ft_strdup(buffer_temp);
	else
	{
		old_buffer = buffer;
		buffer = ft_strjoin(buffer, buffer_temp);
		free(old_buffer);
	}
	return (buffer);
}

char	*read_and_join(int fd, char *buffer, ssize_t *bytes)
{
	char	*buffer_temp;

	buffer_temp = malloc(sizeof(char) * (BUFFER_SIZE + 1));
	if (!buffer_temp)
		return (NULL);
	*bytes = read(fd, buffer_temp, BUFFER_SIZE);
	if (*bytes == -1)
	{
		free(buffer_temp);
		free(buffer);
		buffer = NULL;
		return (NULL);
	}
	if (*bytes == 0)
	{
		free(buffer_temp);
		return (buffer);
	}
	buffer_temp[*bytes] = '\0';
	buffer = join_buffer(buffer, buffer_temp);
	free(buffer_temp);
	return (buffer);
}

char	*get_next_line(int fd)
{
	static char	*buffer;
	ssize_t		bytes;
	char		*line_to_return;

	if (fd < 0 || BUFFER_SIZE <= 0)
		return (NULL);
	bytes = 1;
	while (bytes > 0 && (!buffer || !ft_strchr(buffer, '\n')))
	{
		buffer = read_and_join(fd, buffer, &bytes);
		if (!buffer)
			return (NULL);
	}
	if (bytes == 0 && (!buffer || *buffer == '\0'))
	{
		free(buffer);
		buffer = NULL;
		return (NULL);
	}
	line_to_return = set_line(&buffer);
	return (line_to_return);
}
