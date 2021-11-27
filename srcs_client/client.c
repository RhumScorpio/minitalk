/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   client.c                                           :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: clesaffr <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2021/11/16 21:57:50 by clesaffr          #+#    #+#             */
/*   Updated: 2021/11/17 21:38:22 by clesaffr         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <signal.h>
#include "../libft/libft.h"
#define TIME 300

void	chartobinary(char c, int pid)
{
	int	i;

	i = 0;
	while (i < 8)
	{
		if (c & 0x01)
			kill(pid, SIGUSR1);
		else
			kill(pid, SIGUSR2);
		usleep(TIME);
		c >>= 1;
		i++;
	}
}

int	main(int argc, char **argv)
{
	int		pid;
	char	*str;

	if (argc != 3)
		return (0);
	str = argv[2];
	pid = 0;
	pid = atoi(argv[1]);
	while (*str)
	{
		chartobinary(*str, pid);
		str++;
	}
	chartobinary('\0', pid);
}
