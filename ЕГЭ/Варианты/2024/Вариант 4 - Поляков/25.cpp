#include <istream>
#include <iostream>
#include <math.h>
#include <vector>

using namespace std;

vector<int> find_divs(int num)
{
    vector<int> divs;
    divs.reserve(6);
    for (int div = 1; div < (int)sqrt(num) + 1; div += 2)
    {
        if (num % div == 0)
        {
            divs.push_back(div);
            if (div != (num / div))
                divs.push_back(num / div);
        }

        if (divs.size() > 5)
            return {};
    }
    return divs;
}

int max_val(const vector<int> &vec)
{
    int max = vec[0];
    for (int i = 1; i < vec.size(); i++)
    {
        if (vec[i] > max)
            max = vec[i];
    }
    return max;
}

int main()
{
    for (int num = 105000000; num < 115000000 + 1; num++)
    {
        vector<int> num_divs = find_divs(num);
        if (num_divs.size() == 5)
        {
            cout << num << " " << max_val(num_divs) << endl;
        }
    }
    return 0;
}