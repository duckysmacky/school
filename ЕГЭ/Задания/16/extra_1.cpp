#include <iostream>

size_t F(size_t n)
{
    if (n == 0) return 0;
    return F(n - 1) + 5 * n;
}

int main(int argc, char const *argv[])
{
    size_t i;
    int c = 0;
    for (i = 189456678; i <= 567654322; i++)
    {
        if (F(i) % 7 != 0) c++;
    }

    std::cout << c;
    return 0;
}