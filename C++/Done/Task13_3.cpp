#include <iostream>
#include <random>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int generateNumber(int min, int max) {
	return rand() % (abs(max - min) + 1) + min;
}

int checkForMax(int max, int num) {
	if (num > max) { max = num; }
	return max;
}

int main() {
	int N, max, maxI;
	srand(time(0));

	cin >> N;
	max = 0;
	int biggestList[N];

	for (int listI = 1; listI <= 10; listI++)
	{
		int x[N];
		int sum = 0;
		cout << endl << "List " << listI << ": ";
		for (int num : x)
		{
			num = generateNumber(0, 100);
			cout << num << " ";
			sum += num;
		}
		cout << "- " << sum;
		max = checkForMax(max, sum);
		if (sum == max)
		{ 
			maxI = listI;
			for (int j = 0; j < N; j++) { biggestList[j] = x[j]; }
		}
	}
	cout << endl << "Biggest index: " << maxI << endl;
	cout << "Biggest list: ";
	for (int num : biggestList) { cout << num << " "; }
	cout << endl << "Biggest sum: " << max << endl;
	

	return 0;
}