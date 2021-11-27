NAME	=	server

CC		=	gcc

CFLAGS	=	-Wall -Werror -Wextra

SRCS	=	server.c

LIBFT	=	../libft/

all	:	$(NAME)

$(NAME)	:	
			$(CC) $(CFLAGS) $(SRCS) $(INCLUDES) -o $(NAME)
			mv $(NAME) ..
fclean	:	
			rm -f ../$(NAME)
re		:	fclean all

.PHONY: fclean all re
