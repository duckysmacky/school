#include <iostream>

using namespace std;

int main() {
	int a, b, c, d;

	for (int i = 2000; i <= 3000; i++)
	{

		a = i / 1000;
		b = (i - a * 1000) / 100;
		c = (i - a * 1000 - b * 100) / 10;
		d = (i - a * 1000 - b * 100 - c * 10);

		if (a != b && a != c && a != d && b != c && b != d && c != d)
		{

			cout << i << " ";

		}

	}

}