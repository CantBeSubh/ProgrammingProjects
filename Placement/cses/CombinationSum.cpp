#include <iostream>
#include <bits/stdc++.h>
using namespace std;

vector<vector<int>> res;

int sum(vector<int> arr)
{
    int sum = 0;
    for (auto i : arr)
        sum += i;
    return sum;
}

void soln(vector<int> c, int b, vector<int> arr)
{
    if (sum(c) == b)
    {
        sort(c.begin(), c.end());
        res.push_back(c);
        return;
    }
    if (sum(c) > b)
        return;

    for (int i = 0; i < arr.size(); i++)
    {
        c.push_back(arr[i]);
        soln(c, b, arr);
        c.pop_back();
    }
    return;
}

vector<vector<int>> combinationSum(vector<int> &A, int B)
{
    vector<int> c;
    soln(c, B, A);
    return res;
}
int main()
{
    vector<int> A = {7, 2, 6, 5};
    int B = 16;
    vector<vector<int>> res = combinationSum(A, B);
    for (auto i : res)
    {
        for (auto j : i)
            cout << j << " ";
        cout << endl;
    }
    return 0;
}