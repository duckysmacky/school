#include <iostream>
#include <random>
#include <string>

using namespace std;

int main() {
	double x1, x2, offset, y;
	cin >> x1 >> x2 >> offset;

	for (double x = x1; x < x2; x += offset) {

		y = sqrt(x) / 2 - 0.5;
		cout << x << " | " << y << endl;

	}
}