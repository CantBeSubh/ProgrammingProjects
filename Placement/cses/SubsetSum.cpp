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

void soln(vector<int> op, vector<int> ip, vector<int> &res)
{
    if (ip.size() == 0)
    {
        res.push_back(sum(op));
        return;
    }
    vector<int> op1 = op;
    vector<int> op2 = op;
    op2.push_back(ip[0]);
    ip.erase(ip.begin() + 0);
    soln(op1, ip, res);
    soln(op2, ip, res);
    return;
}

vector<int> SubsetSum(vector<int> &A, int N)
{
    vector<int> op;
    vector<int> res;
    soln(op, A, res);
    sort(res.begin(), res.end());
    res.erase(unique(res.begin(), res.end()), res.end());
    return res;
}
int main()
{
    vector<int> A = {5, 2, 1};
    int N = 3;
    vector<int> res = SubsetSum(A, N);
    for (auto i : res)
        cout << i << " ";
}