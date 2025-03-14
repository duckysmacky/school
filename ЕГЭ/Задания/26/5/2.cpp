#include <iostream>
#include <numeric>
#include <fstream>
#include <vector>
#include <array>
#include <string>

using namespace std;

bool is_triangle(int x, int y, int z)
{
	return (x + y > z) && (y + z > x) && (z + x > y);
}

vector<array<int, 3>> find_triples(vector<int> arr)
{
	vector<array<int, 3>> triples;
	for (size_t i = 0; i < arr.size(); i++)
	{
		cout << i << endl;
		for (size_t j = i + 1; j < arr.size(); j++)
		{
			for (size_t k = j + 1; k < arr.size(); k++)
			{
				if (is_triangle(arr[i], arr[j], arr[k]))
				{
					triples.push_back({arr[i], arr[j], arr[k]});
				}
			}
		}
	}
	return triples;
}

void find(vector<int> arr)
{
	vector<array<int, 3>> triples = find_triples(arr);
	cout << triples.size() << " - " << arr.size() << endl;
}

int main()
{
	ifstream file("26_10072.txt");
	// ifstream file("test");
	string line;
	getline(file, line);
	int n = stoi(line);

	vector<int> nums;
	while (getline(file, line)) {
		nums.push_back(stoi(line));
	}

	vector<array<int, 3>> triples = find_triples(nums);
	size_t total = triples.size();
	int max_sum = 0;
	for (const array<int, 3>& arr : triples)
	{
		int sum = accumulate(arr.begin(), arr.end(), 0, plus<int>());
		max_sum = max(max_sum, sum);
	}

	cout << total << " " << max_sum << endl;

	return 0;
}
