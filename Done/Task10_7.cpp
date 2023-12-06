#include <iostream>
#include <random>
#include <string>

using namespace std;

int main() {
	int n;
	int s = 0;
	int m = 1;
	double x, y;
	cin >> n;
	x = n;

	while (x > 0) {
		x = x / 10;
		y = (x - floor(x)) * 10;
		x = floor(x);

		if (round(y) != 0) {

			s += round(y);
			m *= round(y);

		}
	}

	cout << "Summa :" << s << "\nProizvedenie: " << m << endl;
}