#include <iostream>
#include <random>
#include <string>

using namespace std;

int main() {

	int x[13];
	int y = 0;
	srand(time(0));

	for (int i = 0; i < 13; i++) {

		x[i] = rand() % 1001 - 500;

		if (i != 0) {

			if (x[i] < x[i - 1] && y < x[i - 1]) {

				y = x[i - 1];

			}

		}

		cout << x[i] << " ";

	}

	cout << endl << y << endl;

}