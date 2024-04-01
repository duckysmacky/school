#include <iostream>
#include <vector>

using namespace std;

void out(string name, vector<unsigned long> val) {
    cout << name << ": ";
    for (unsigned long o : val) cout << o << " ";
    cout << "\n";
}

// 21 108 1
// 5 12 4

int main() {
    unsigned long n, k, d;
    cin >> n >> k >> d;

    vector<unsigned long> buff; 
    vector<unsigned long> results; 

    unsigned long x;
    for (unsigned long i = 0; i < d; i++) {
        buff.push_back(0);
        out("New loop", buff);

        x = buff.at(buff.size() - 1);
        while (x < 10) {
            if ((n * 10 + x) % k == 0) {
                // Found
                buff.insert(buff.end(), x);
                out("Found! buff", buff);
                break;
            } else if (x == 9) {
                // Not found anything
                buff.pop_back();
                out("Not found! buff", buff);
                break;
            }
            // Continue the search
            x++;
        }
        if (buff.size() > 0) {
            n = n * 10 + buff.at(buff.size() - 1);
            results.push_back(n);
        } else {
            break;
        }
    }
    if (results.size() > 0) out("results", results); else cout << "-1";
}