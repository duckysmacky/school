#include <iostream>

using namespace std;

int main() {
	int x, count;
	cin >> x;
	count = 0;

	while (x <= 100)
	{
		x += 10;
		count += 1;
	}

	cout << count << endl;
}