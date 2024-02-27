#include <iostream>
#include <random>
#include <string>

using namespace std;

int main() {

	int x[20];
	int y = 0;
	srand(time(0));

	for (int i = 0; i < 17; i++) {

		x[i] = rand() % 181 - 90;

		if (i != 0) {

			if (x[i] < x[i - 1]) {

				y = x[i];
				x[i] = x[i - 1];
				x[i - 1] = y;

			}

		}

		cout << x[i] << " ";

	}

}