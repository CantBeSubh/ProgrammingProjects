#include <iostream>
#include <bits/stdc++.h>
using namespace std;

int sum(vector<int> arr)
{
    int sum = 0;
    for (auto i : arr)
        sum += i;
    return sum;
}

void soln(vector<int> c, int K, int S, vector<vector<int>> &res)
{
    if (sum(c) > S or c.size() > K)
        return;

    if (sum(c) == S and c.size() == K)
    {
        sort(c.begin(), c.end());
        res.push_back(c);
        return;
    }

    for (int i = 1; i < 10; i++)
    {
        if (c.size() > 0 and i <= c.back())
            continue;
        c.push_back(i);
        soln(c, K, S, res);
        c.pop_back();
    }
    return;
}

vector<vector<int>> combinationSum(int K, int N)
{
    vector<int> c;
    vector<vector<int>> res;
    soln(c, K, N, res);
    return res;
}
int main()
{
    int K = 3, N = 9;
    vector<vector<int>> r = combinationSum(K, N);
    for (auto i : r)
    {
        for (auto j : i)
            cout << j << " ";
        cout << endl;
    }
    return 0;
}