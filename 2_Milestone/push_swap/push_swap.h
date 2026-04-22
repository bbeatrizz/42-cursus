/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   push_swap.h                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: beamarti <beamarti@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/03/03 11:17:15 by beamarti          #+#    #+#             */
/*   Updated: 2026/03/09 10:46:09 by beamarti         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef PUSH_SWAP_H
# define PUSH_SWAP_H

# include <stdlib.h>
# include <unistd.h>

typedef struct s_list
{
	int				value;
	int				index;
	struct s_list	*next;
}					t_list;

long	ft_atoi(const char *nptr);
void	ft_putnbr(int n);
t_list	*ft_lstnew(int value);
t_list	*ft_lstlast(t_list *lst);
void	ft_lstadd_back(t_list **lst, t_list *new);
int		ft_lstsize(t_list *lst);
void	ft_lstclear(t_list **lst);
void	ft_printlst(t_list *stack);
void	ft_push(t_list **stack_a, t_list **stack_b);
void	ft_pa(t_list **stack_b, t_list **stack_a);
void	ft_pb(t_list **stack_a, t_list **stack_b);
void	ft_rotate(t_list **stack);
void	ft_ra(t_list **stack_a);
void	ft_revrotate(t_list **stack);
void	ft_swap(t_list **stack);
void	ft_radix_sort(t_list **stack_a, t_list **stack_b);
int		ft_maxbit(t_list *stack);
void	ft_index(t_list **stack);
void	ft_sort_three(t_list **stack);
t_list	*ft_findmin(t_list **stack);
int		ft_locatemin(t_list **stack);
void	ft_movemin(t_list **stack_a, t_list **stack_b);
void	ft_sort_five(t_list **stack_a, t_list **stack_b);
void	ft_sort_two(t_list **stack);
int		ft_isdigit(int c);
int		ft_is_number(char *str);
void	ft_process_stack(t_list **stack_a, t_list **stack_b);
char	*ft_substr(char const *s, unsigned int start, size_t len);
char	**ft_split(char const *s, char c);
void	free_split(char **token);
int		check_split(char **token);
int		validate_and_convert(char *str, long *n, char **token, t_list **stack);
int		insert_into_stack(long n, t_list **stack, char **token);
size_t	ft_strlen(const char *s);
void	*ft_memcpy(void *dest, const void *src, size_t n);
char	*ft_strdup(const char *s);
int		ft_is_sorted(t_list *stack_a);

#endif