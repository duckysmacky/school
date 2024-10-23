#include <iostream>
#include <string>

int main() {
    std::string s, t, x;
    std::cin >> s;
    s = s.substr(0, s.find_last_not_of(" ") + 1);
    std::cin >> t;
    t = t.substr(s.length(), t.find_last_not_of(" ") + 1);

    int i = s.length();
    x = s + "";
    int counter = 1;
    while (x == s) {
        s = s.substr(0, i - 1);
        i -= 1;
        counter += 1;
    }
    
    std::cout <<counter;

    return 0;
}