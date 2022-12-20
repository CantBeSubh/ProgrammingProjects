#include <iostream>
#include <bits/stdc++.h>
using namespace std;
int findFloor(vector<long long> v, long long n, long long x)
{
    int max;
    int ind = -1;
    for (int i = 0; i < n; i++)
    {
        if (v[i] <= x)
        {
            if (ind == -1)
            {
                max = v[i];
                ind = i;
            }
            else if (v[i] > max)
            {
                max = v[i];
                ind = i;
            }
        }
    }
    return ind;
}

int main()
{
    cout << "Hello World!" << endl;
    vector<long long> v = {1, 2, 8, 10, 10, 12, 19};
    int n = v.size();
    int x = 5;
    cout << findFloor(v, n, x) << endl;
    return 0;
}