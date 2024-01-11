#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>

/* ADD POSITIVE NUMBERS
 * PRINT RESULT FOLLOWED BY A NEW LINE
 * IF ARGC == 1, PRINT 0, FOLLOWED BY A NEW LINE
 * IF THERE'S A SYMBOL, PRINT ERROR, FOLLOWED BY A NEW LINE, AND RETURN 1
 *
 * ARGC ==> NUMBER OF ARGUMENTS
 * ARGV ==> ARRAY OF STRINGS, WHERE ARGC IS THE TOTAL NUMBER OF THE ARRAY
 */

int main(int argc, char *argv[])
{
	int sumResult = 0, i = 1, j;
    
	while (i < argc)
	{
		j = 0;
		while (argv[i][j])
		{
			if (isdigit(argv[i][j]) == 0)
			{
				printf("Error\n");
				return (1);
			}
			j++;
		}
		i++;
	}
	if (argc != 1)
	{
		i = 1;
		while (i < argc)
		{
			if (atoi(argv[i]) >= 0)
				sumResult += atoi(argv[i]);
			i++;
		}
	}
	printf("%i\n", sumResult);
	return (0);
}
