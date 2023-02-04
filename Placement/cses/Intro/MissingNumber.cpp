#include <iostream>
#include <bits/stdc++.h>

typedef long long ll; // shorthand for long long

using namespace std;
int main()
{
    // solution comes here
    // removes bottleneck of cin and cout
    ios::sync_with_stdio(0);
    cin.tie(0);

    int n, a = 0, b = 0;
    cin >> n;
    int arr[n];
    for (int i = 1; i <= n; i++)
        a = a ^ i;
    for (int i = 0; i < n - 1; i++)
    {
        cin >> arr[i];
        b = b ^ arr[i];
    }

    cout << (a ^ b);
    return 0;
}