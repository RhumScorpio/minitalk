NAME	=	server

CC		=	gcc

CFLAGS	=	-Wall -Werror -Wextra

SRCS	=	server.c

LIBFT	=	../libft/

INCLUDES = -I $(LIBFT)

all	:	$(NAME)

$(NAME)	:	
			$(CC) $(CFLAGS) $(SRCS) $(INCLUDES) -o $(NAME)
			mv $(NAME) ..
clean	:
			rm -f ../$(NAME)
fclean	:	clean

re		:	fclean all

.PHONY: clean fclean all re
