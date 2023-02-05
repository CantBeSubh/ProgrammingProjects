#include <iostream>
#include <bits/stdc++.h>
using namespace std;

map<int, string> m = {{2, "abc"}, {3, "def"}, {4, "ghi"}, {5, "jkl"}, {6, "mno"}, {7, "pqrs"}, {8, "tuv"}, {9, "wxyz"}};

void soln(string op, vector<int> ip, vector<string> &res)
{
    if (ip.size() == 0)
    {
        res.push_back(op);
        return;
    }
    int digit = ip[0];
    ip.erase(ip.begin());
    string letters = m[digit];
    for (int i = 0; i < letters.length(); i++)
    {
        string op1 = op;
        op1.push_back(letters[i]);
        soln(op1, ip, res);
    }
    return;
}
vector<string> possibleWords(int a[], int N)
{
    vector<string> res;
    vector<int> nums(a, a + N);
    soln("", nums, res);
    return res;
}

int main()
{
    int a[] = {2, 3, 4};
    vector<string> res = possibleWords(a, 3);
    for (int i = 0; i < res.size(); i++)
    {
        cout << res[i] << " ";
    }
    return 0;
}