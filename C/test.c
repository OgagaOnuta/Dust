#include <stdio.h>

int raised_to_power(int num, int power)
{
	int x = 1, result = 1;

	while (x <= power)
	{
		result = result * num;
		x++;
	}

	return (result);
}

int main(void)
{
	int answer;

	answer = raised_to_power(2, 2);
	printf("2 ^ 2 = %d\n", answer);
	answer = raised_to_power(3, 3);
	printf("3 ^ 3 = %d\n", answer);
	answer = raised_to_power(2, 5);
	printf("2 ^ 5 = %d\n", answer);

	return (0);
}
