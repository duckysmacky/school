#include <iostream>
#include <random>
#include <string>

using namespace std;

int main() {
	int x1, y1, x2, y2;
	cin >> x1 >> y1 >> x2 >> y2;
	string dir = "";

	while (x1 != x2) {

		if (x1 < x2) {
			x1 += 1;
			dir += "E";

		}
		else if (x1 > x2) {
			x1 -= 1;
			dir += "W";

		}
	}

	while (y1 != y2) {
		if (y1 < y2) {
			y1 += 1;
			dir += "N";
		}
		else if (y1 > y2) {
			y1 -= 1;
			dir += "S";
		}
	}

	cout << dir << endl;
}