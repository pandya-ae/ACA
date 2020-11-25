#include <iostream>
using namespace std;

int main()
{
	int n = 600000;
	int test = 0;
	for (int i = 0; i < n; i++)
	{
		for (int j = 0; j <= i; j++)
		{
		test++;
		}
	}
	return 0;
}
