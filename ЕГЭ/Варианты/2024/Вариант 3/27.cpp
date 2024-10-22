#include <iostream>
#include <fstream>
#include <string>
#include <vector>

using namespace std;

int main()
{
    string buffer;
    ifstream file("27-A.txt");
    vector<int> nums;

    while (getline(buffer, file))
    {
        nums.push_back((int) buffer.);
    }

    for (auto num : nums)
    {
        cout << num << endl;
    }
}