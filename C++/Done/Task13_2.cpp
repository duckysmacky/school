#include <iostream>
#include <random>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int nod(int a, int b) {
	int x;
	while (a != 0 && b != 0) {
		if (a > b) {
			a = a % b;
		} else {
			b = b % a;
		}
	}
	return a + b;
}

int nok(int a, int b) {
	int x = a * b / nod(a, b);
	return x;
}

int main() {
	
	int a, b, choice;
	cin >> a >> b;
	cout << "NOD(1) or NOK(2): ";
	cin >> choice;
	if (choice == 1) {
		cout << nod(a, b) << endl;
	} else {
		cout << nok(a, b) << endl;
	}
	return 0;
}