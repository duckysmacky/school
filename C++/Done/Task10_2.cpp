#include <iostream>
#include <random>

using namespace std;

int main() {
	int x, count;
	count = -1;

	srand(time(0));
	x = rand() % 501;

	while (x >= 0)
	{
		x -= 25;
		count += 1;
	}

	cout << count << endl;
}