#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

typedef struct instructions{
	char input[10];
	struct instructions *next;
}instructions;

bool is_stop(char input[])
{
	if (atoi(input) == 99999)
	{
		return true;
	}
	return false;
}

bool is_even(char result[])
{
		if ( (((result[0]) - '0') + ((result[1])) - '0') % 2 == 0 )
		{
			return true;
		}else
		{
			return false;
		}
}

void right(char input[], int size)
{
	char temp[size];
	int i = 0;
	while (input[i+2] != '\0')
	{
		temp[i] = input[i+2];
		if (input[i+3] == '\0')
		{
			temp[i+1] = '\0';
		}
		i++;
	}
	printf("right %d\n", atoi(temp));
}
void left(char input[], int size)
{
	char temp[size];
	int i = 0;
	while (input[i+2] != '\0')
	{
		temp[i] = input[i+2];
		if (input[i+3] == '\0')
		{
			temp[i+1] = '\0';
		}
		i++;
	}
	printf("left %d\n", atoi(temp));
}

void answer(bool temp, char input[], int size)
{
	if (temp)
	{
		right(input, size);
	}else
	{
		left(input, size);
	}
}
int main()
{
	instructions head;
	instructions *turning = &head;

	while (turning != NULL)
	{
		scanf("%s", turning->input);
		if (is_stop(turning->input))
		{
			turning->next = NULL;
			break;
		}
		turning -> next = (instructions *)malloc(sizeof(instructions));
		turning = turning->next;
	}

	instructions *result = &head;
	int temp = 1;
	while (result->next != NULL)
	{
		if (is_stop(result->input))
		{
			exit(0);

		}else if ( (((result->input[0]) -'0') == 0) && (((result->input[1]) - '0') == 0) )
		{
			answer(temp, result->input, sizeof(result->input)/sizeof(char));
		}else if (is_even(result->input))
		{
			temp = 1;
			answer(temp, result->input, sizeof(result->input)/sizeof(char));
		}else
		{
			temp = 0;
			answer(temp, result->input, sizeof(result->input)/sizeof(char));
		}
		result = result->next;

	}
	return 0;
}
