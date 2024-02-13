#include <iostream>
#include <random>
#include <string>

using namespace std;

int main() {
	int n, x;
	cin >> n;

	while (n > 1) {
		if (n % 2 != 0) {
			
			n = (n * 3) + 1;

		}

		n /= 2;
		cout << n << " ";

	}

	cout << endl;

}