#include <iostream>

using namespace std;

int main() {
    double nums[3];
    cin >> nums[0] >> nums[1] >> nums[2];
    
    for (double num : nums) {
        if (num >= 1.0 && num < 3.0) { cout << num << " "; }
    }
    
    return 0;
}