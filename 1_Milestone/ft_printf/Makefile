NAME = libftprintf.a
FLAGS = -Wall -Werror -Wextra

FILES = \
	ft_printf.c\
	ft_printnbr.c\
	ft_printptr.c\
	ft_printhexa.c\
	ft_printstr.c\
	ft_printunsigned.c

OBJS = $(FILES:.c=.o)

$(NAME): $(FILES) $(OBJS)
	@cc -c $(FLAGS) $(FILES)
	@ar rcs $(NAME) $(OBJS)

all: $(NAME)

clean:
	@rm -f $(OBJS)

fclean: clean
	@rm -f $(NAME)

re: fclean all

.PHONY: all clean fclean re
