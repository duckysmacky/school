#include <iostream>

using namespace std;

int main() {
	int m, a, b, c, count;
	cin >> m;
	count = 0;

	for (int i = 100; i <= 999; i++) {

		//cout << i << endl;
		a = i / 100;
		b = (i - a * 100) / 10;
		c = (i - a * 100 - b * 10);
		//cout << a << " " << b << " " << c << "\n\n";

		if (a + b + c == m) {

			cout << i << endl;
			count += 1;

		}

	}

	if (count > 0) {

		cout << "Total " << count << endl;

	}
	else {
		
		cout << "Don't exist" << endl;

	}


}