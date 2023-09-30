#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <unistd.h>

int infinite_while(void);

/**
 * infinite_while - Run an infinite while loop.
 *
 * Return: Always 0.
*/

int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}

	return (0);
}

/**
 * main - main function that creates 5 child processes
 *
 * Return: 0 onsuccess, else 1
*/

int main(void)
{
	pid_t child_pid;
	int count = 0;

	while (count < 5)
	{
		child_pid = fork();
		if (child_pid > 0)
		{
			printf("Zombie process created, PID: %d\n", child_pid);
			sleep(1);
			count++;
		}
		else
			exit(0);
	}

	infinite_while();

	return (EXIT_SUCCESS);
}
