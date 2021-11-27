NAME	=	client

CC		=	gcc

CFLAGS	=	-Wall -Werror -Wextra

SRCS	=	client.c

LIBFT	=	../libft/

INCLUDES	=	-I $(LIBFT)

all	:	lib $(NAME)

lib	:	
		make -C $(LIBFT)

$(NAME)	:	
			$(CC) $(CFLAGS) $(SRCS) $(INCLUDES) -o $(NAME)
			mv $(NAME) ..
fclean	:	
			rm -f ../$(NAME)
re		:	fclean all

.PHONY: fclean all re
