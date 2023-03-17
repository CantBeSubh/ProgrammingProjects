#include <iostream>
#include <bits/stdc++.h>

using namespace std;

bool soln(int N, vector<int> &bills)
{
    bool ans = true;
    map<int, int> m;
    for (auto i : bills)
    {
        m[i]++;
        if (i == 20)
        {
            if (m[10] >= 1 && m[5] >= 1)
            {
                m[10]--;
                m[5]--;
            }
            else if (m[5] >= 3)
                m[5] -= 3;
            else
            {
                ans = false;
                break;
            }
        }
        else if (i == 10)
        {
            if (m[5] >= 1)
            {
                m[5]--;
            }
            else
            {
                ans = false;
                break;
            }
        }
    }
    return ans;
}

int main()
{
    vector<int> bills = {5, 5, 5, 10, 20};
    int N = bills.size();
    cout << (soln(N, bills) ? "True" : "False") << endl;
    return 0;
}