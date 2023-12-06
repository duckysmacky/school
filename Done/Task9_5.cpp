#include <iostream>

using namespace std;

int main() {
    int n, k;
    double num;

    cin >> n >> k;
    num = n;

    for (int i = 1; i < k; i++) {

        num = num / 10;

    }

    cout << int(num) % 10 << endl;

}