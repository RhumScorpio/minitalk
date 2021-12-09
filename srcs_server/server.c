/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   server.c                                           :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: clesaffr <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2021/11/16 21:32:24 by clesaffr          #+#    #+#             */
/*   Updated: 2021/12/07 20:29:41 by clesaffr         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include "../libft/libft.h"
#define BUFF_SIZE 100

void	signal_sawp(int n)
{
	static char	c;
	static char	buff[BUFF_SIZE];
	static int	pos;
	static int	buff_pos;

	if (n == SIGUSR1)
		c |= 1 << pos;
	pos++;
	if (pos > 7)
	{
		if (buff_pos == BUFF_SIZE || c == '\0')
		{
			write(1, buff, buff_pos);
			buff_pos = 0;
		}
		else
			buff[buff_pos++] = c;
		pos = 0;
		c = 0x0;
	}
}

int	main(int argc, char **argv)
{
	int	pid;

	(void)argv;
	if (argc != 1)
		return (0);
	signal(SIGUSR1, signal_sawp);
	signal(SIGUSR2, signal_sawp);
	pid = getpid();
	printf("PID - %d\n", pid);
	while (1)
		(void)0;
}
