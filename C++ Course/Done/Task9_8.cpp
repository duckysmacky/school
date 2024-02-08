#include <iostream>

using namespace std;

int main() {
	int n, sum;
	cin >> n;
	sum = 0;

	for (int i = 1; i < n; i++) {

		if (n % i == 0) {

			sum += i;

		}

	}

	if (n == sum) {

		cout << n << " sovershennoe" << endl;

	}
	else {

		cout << n << " ne sovershennoe" << endl;

	}


}