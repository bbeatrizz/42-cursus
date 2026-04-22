NAME = push_swap

CC = gcc

FLAGS = -Wall -Werror -Wextra

FILES = \
	mov_push.c\
	mov_rotate.c\
	mov_revrotate.c\
	mov_swap.c\
	push_swap_lst.c\
	push_swap_utils.c\
	push_swap_clear.c\
	push_swap.c\
	sort_radix.c\
	sort_five.c\
	push_swap_isn.c\
	sort_two.c\
	check_errors.c\
	ft_split.c\
	ft_split_utils.c

OBJS = $(FILES:.c=.o)

all: $(NAME)

$(NAME): $(OBJS)
	$(CC) $(FLAGS) $(OBJS) -o $(NAME)

$(OBJS): %.o: %.c
	$(CC) $(FLAGS) -c $< -o $@

clean:
	@rm -rf $(OBJS)

fclean: clean
	@rm -f $(NAME)

re: fclean all

.PHONY: all clean fclean re