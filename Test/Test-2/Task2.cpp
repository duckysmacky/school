#include <iostream>

using namespace std;

int main() {
    int x, y, p;
    cin >> x >> p;
    y = x;

    for (int i = 0; i < p - 1; i++)
    {
        x *= y;
    }
    cout << x;
    
    return 0;
}