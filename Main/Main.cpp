#include <iostream>
#include <random>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

void toBit(int x) {

	vector<int> bits;

	while (x > 1)
	{
		if (x % 2 == 0) { bits.push_back(0); }
		else { bits.push_back(1); }
		x /= 2;
	}
	bits.push_back(1);
	reverse(bits.begin(), bits.end());

	for (int bit : bits) {
		cout << bit;
	}
}

int main() {

	int x, y;
	cin >> x;

	toBit(x);
	return 0;
}