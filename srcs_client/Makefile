NAME	=	client

CC		=	gcc

CFLAGS	=	-Wall -Werror -Wextra

SRCS	=	client.c

LIBRARY =	../libft/libft.a

LIBFT	=	../libft/

INCLUDES	=	-I $(LIBFT)

all	:	lib $(NAME)

lib	:	
		make -C $(LIBFT)

$(NAME)	:	
			$(CC) $(CFLAGS) $(SRCS) $(INCLUDES) -o $(NAME) $(LIBRARY)
			mv $(NAME) ..
clean	:	
			rm -f ../$(NAME)
fclean	:	clean

re		:	fclean all

.PHONY: clean fclean all re
