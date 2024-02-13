#include <iostream>
#include <random>

using namespace std;

int main() {
	double x, y;
	cin >> x;
	int z = 0;
	int chet = 0;
	int nechet = 0;
	y = x;

	while (y > 1) {
		y = (x / 10 - (floor(x / 10))) * 10;
		z = floor(y + 0.1);
		if (z != 0) {
			if (z % 2 == 0) {
				chet += 1;
			}
			else {
				nechet += 1;
			}
		}
		x = floor(x / 10);
	}

	cout << "Chetnie: " << chet << "\nNechetnie: " << nechet << endl;

}