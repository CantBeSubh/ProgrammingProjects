#include <iostream>
#include <bits/stdc++.h>

using namespace std;
int soln(int arr[], int n)
{
    if (n <= 1)
        return 0;

    int mini;
    map<int, int> m;
    for (int i = 0; i < n; i++)
        m[arr[i]]++;
    mini = m.begin()->second;
    int maxi = n - mini;
    if (mini < maxi)
        return mini;
    else
        return maxi;
    return 0;
}
int main()
{
    int t;
    int arr[101];
    cin >> t;
    for (int i = 0; i < t; i++)
    {
        int n;
        cin >> n;
        for (int j = 0; j < n; j++)
            cin >> arr[j];
        cout << soln(arr, n) << endl;
    }
    return 0;
}