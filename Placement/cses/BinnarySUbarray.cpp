#include <iostream>
#include <bits/stdc++.h>

using namespace std;

int soln(vector<int> &arr, int N, int target)
{
    int i = 0, j = 0, res = 0;
    int s = 0;
    while (j <= N && j >= i)
    {
        if (j < N)
        {
            s += arr[j];
            j++;
        }
        else
        {
            s -= arr[i];
            i++;
        }
        while (s > target)
        {
            s -= arr[i];
            i++;
        }
        if (s == target)
            res++;
    }
    return res;
}
int main()
{
    vector<int> arr = {1, 0, 1, 0, 1};
    int target = 2;
    cout << soln(arr, arr.size(), target);
}