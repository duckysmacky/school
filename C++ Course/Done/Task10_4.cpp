#include <iostream>
#include <random>
#include <string>

using namespace std;

int main() {
	int num1;
	string num2;
	double x, y;
	cin >> num1;
	x = num1;

	while (x > 0) {
		x = x / 10;
		y = (x - floor(x)) * 10;
		x = floor(x);

		int z = round(y);
		num2 += to_string(z);
	}

	cout << num2 << endl;
}