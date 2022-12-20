#include <iostream>
#include <bits/stdc++.h>
using namespace std;
int findFloor(vector<long long> v, long long n, long long x)
{
    int low = 0, high = n - 1;
    while (low <= high)
    {
        int mid = (low + high) / 2;
        if (v[mid] == x)
            return mid;
        else if (v[mid] > x)
            high = mid - 1;
        else
            low = mid + 1;
    }
    return high;
}

int main()
{
    cout << "Hello World!" << endl;
    vector<long long> v = {1, 2, 8, 10, 11, 12, 19};
    int n = v.size();
    int x = 5;
    cout << findFloor(v, n, x) << endl;
    return 0;
}