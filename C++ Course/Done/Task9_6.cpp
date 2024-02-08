#include <iostream>

using namespace std;

int main() {

	for (int i = 1; i <= 999; i++)
	{
		if (i % 15 == 0 && i % 30 != 0) {
			cout << i << endl;
		}
	}

}