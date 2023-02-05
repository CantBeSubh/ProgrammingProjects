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
    if (arr.size() == 0)
        return;
    vector<int> c1 = c;
    vector<int> c2 = c;
    c2.push_back(arr[0]);
    arr.erase(arr.begin() + 0);
    soln(c1, b, arr);
    soln(c2, b, arr);
    return;
}

vector<vector<int>> combinationSum(vector<int> &A, int B)
{
    vector<int> c;
    soln(c, B, A);
    sort(res.begin(), res.end());
    // res.erase(unique(res.begin(), res.end()), res.end());
    return res;
}
int main()
{
    vector<int> A = {10, 1, 2, 7, 6, 1, 5};
    int B = 8;
    cout << "SOLUTION:" << endl;
    vector<vector<int>> res = combinationSum(A, B);
    for (auto i : res)
    {
        for (auto j : i)
            cout << j << " ";
        cout << endl;
    }
    return 0;
}