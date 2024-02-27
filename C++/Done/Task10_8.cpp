#include <iostream>
#include <random>
#include <string>

using namespace std;

int main() {
	int n, m, p, x;
	cin >> p >> x;
	n = 1;

	while (pow(n, p) < x) {
		m = pow(n, p);
		cout << m << " ";
		n += 1;
	}
}