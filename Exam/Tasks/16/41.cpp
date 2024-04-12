#include <iostream>
#include <string>

using namespace std;

long G(long n);
long F(long cls);

int main(int argc, char const *argv[])
{
    string result = to_string(G(36));
    int i;
    long sum = 0;
    for (i = 0; i < result.length(); i++)
    {
        sum += result[i] - '0';
    }
    cout << result << " " << sum;

    return 0;
}

long F(long n)
{
    if (n == 1) return 1;
    if (n > 1) return F(n - 1) - 2 * G(n - 1);
}

long G(long n)
{
    if (n == 1) return 1;
    if (n > 1) return F(n - 1) + G(n - 1) + n;
}
